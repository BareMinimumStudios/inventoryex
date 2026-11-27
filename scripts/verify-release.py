"""Validate MC Publish release files using only the Python standard library."""
import hashlib
import json
from pathlib import Path
import re
import zipfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify_jar(jar, version, minecraft, java, icon):
    with zipfile.ZipFile(jar) as archive:
        require(archive.testzip() is None, f"Corrupt archive: {jar}")
        metadata = json.loads(archive.read("fabric.mod.json"))
        for key, expected in (("id", "invex"), ("version", version), ("environment", "server")):
            require(metadata.get(key) == expected, f"{jar.name}: expected {key}={expected}")
        for key, expected in (("minecraft", f"~{minecraft}"), ("java", f">={java}")):
            require(metadata.get("depends", {}).get(key) == expected, f"{jar.name}: invalid {key} requirement")
        authors = {author if isinstance(author, str) else author["name"] for author in metadata.get("authors", [])}
        require({"pokesmells", "naomieow"} <= authors, f"{jar.name}: missing author credits")
        require(archive.read(metadata["icon"]) == icon, f"{jar.name}: stale bundled icon")
        libraries = metadata.get("jars", [])
        require(libraries, f"{jar.name}: no bundled libraries")
        for nested in libraries:
            require(nested["file"] in archive.namelist(), f"{jar.name}: missing {nested['file']}")
        require(any("sgui-" in item["file"] for item in libraries), f"{jar.name}: SGUI missing")
        require(any("fabric-permissions-api-" in item["file"] for item in libraries), f"{jar.name}: permissions API missing")
        entrypoint = archive.read("xyz/naomieow/invex/InvEx.class")
        major = int.from_bytes(entrypoint[6:8], "big")
        require(major <= java + 44, f"{jar.name}: compiled for a newer Java than declared")
    print(f"Verified {jar.name} - SHA-256 {hashlib.sha256(jar.read_bytes()).hexdigest()}")


def main():
    root = Path(__file__).resolve().parents[1]
    match = re.search(r'^version = "([^"]+)"', (root / "build.gradle.kts").read_text(encoding="utf-8"), re.M)
    require(match is not None, "Cannot read release version from build.gradle.kts")
    version = match.group(1)
    icon = (root / "src/main/resources/assets/invex/icon.png").read_bytes()
    for minecraft, java in (("1.20.1", 17), ("1.21.1", 21)):
        jar = root / "build/libs" / f"invex-{version}-{minecraft}.jar"
        verify_jar(jar, version, minecraft, java, icon)


if __name__ == "__main__":
    main()
