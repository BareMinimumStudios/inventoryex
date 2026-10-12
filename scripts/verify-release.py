"""Validate the files MC Publish uploads; uses only the Python standard library."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

root = Path(__file__).resolve().parents[1]
version = re.search(r'^version = "([^"]+)"', (root / "build.gradle.kts").read_text(), re.M).group(1)
for minecraft, java in (("1.20.1", 17), ("1.21.1", 21)):
    jar = root / "build/libs" / f"invex-{version}-{minecraft}.jar"
    with zipfile.ZipFile(jar) as archive:
        metadata = json.loads(archive.read("fabric.mod.json"))
        assert metadata["id"] == "invex", jar
        assert metadata["version"] == version, jar
        assert metadata["environment"] == "server", jar
        assert metadata["depends"]["minecraft"] == f"~{minecraft}", jar
        assert metadata["depends"]["java"] == f">={java}", jar
        assert "pokesmells" in [a if isinstance(a, str) else a["name"] for a in metadata["authors"]], jar
        icon = archive.read(metadata["icon"])
        assert icon == (root / "src/main/resources/assets/invex/icon.png").read_bytes(), jar
        for nested in metadata.get("jars", []):
            assert nested["file"] in archive.namelist(), nested
        assert not any("opc" in nested["file"] for nested in metadata.get("jars", [])), jar
    print(f"Verified {jar.name} — SHA-256 {hashlib.sha256(jar.read_bytes()).hexdigest()}")
