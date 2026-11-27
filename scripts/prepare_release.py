"""Stage validated release JARs and this version's curated release notes."""
from pathlib import Path
import shutil

from release_notes import extract_release, read_version
from importlib.util import module_from_spec, spec_from_file_location


def main():
    root = Path(__file__).resolve().parents[1]
    spec = spec_from_file_location("verify_release", root / "scripts/verify-release.py")
    verifier = module_from_spec(spec)
    spec.loader.exec_module(verifier)
    verifier.main()
    version = read_version(root)
    notes = extract_release((root / "CHANGELOG.md").read_text(encoding="utf-8"), version)
    destination = root / "build/release"
    if destination.resolve() != root / "build" / "release":
        raise ValueError("Refusing to stage releases through a symlink or junction")
    # This directory belongs to this script; remove stale files from previous builds.
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    for minecraft in ("1.20.1", "1.21.1"):
        jar = root / "build/libs" / f"invex-{version}-{minecraft}.jar"
        shutil.copy2(jar, destination / jar.name)
    (destination / "RELEASE-NOTES.md").write_text(notes, encoding="utf-8")
    print(f"Staged both Minecraft JARs and release notes for {version}")


if __name__ == "__main__":
    main()
