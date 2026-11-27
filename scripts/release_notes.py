"""Read project versions and extract curated Keep a Changelog release notes."""
import argparse
from datetime import date
import os
from pathlib import Path
import re

CATEGORIES = {"Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"}


def read_version(root):
    matches = re.findall(r'^version = "([^"]+)"', (root / "build.gradle.kts").read_text(encoding="utf-8"), re.M)
    if len(matches) != 1 or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", matches[0]):
        raise ValueError("Expected one semantic release version in build.gradle.kts")
    return matches[0]


def extract_release(changelog, version):
    if not changelog.startswith("# Changelog\n"):
        raise ValueError("CHANGELOG.md must start with '# Changelog'")
    headings = list(re.finditer(r"^## \[([^\]]+)\](.*)$", changelog, re.M))
    if not headings or headings[0].group(1) != "Unreleased":
        raise ValueError("The first changelog section must be [Unreleased]")
    labels = [heading.group(1) for heading in headings]
    if len(labels) != len(set(labels)):
        raise ValueError("Duplicate changelog version headings")
    if version not in labels:
        raise ValueError(f"Missing dated changelog entry for {version}; prepare it before building a release")
    index = labels.index(version)
    heading = headings[index]
    suffix = heading.group(2)
    if not re.fullmatch(r" - \d{4}-\d{2}-\d{2}", suffix):
        raise ValueError(f"Version {version} needs an ISO release date: YYYY-MM-DD")
    date.fromisoformat(suffix[3:])
    end = headings[index + 1].start() if index + 1 < len(headings) else len(changelog)
    section = changelog[heading.start():end]
    section = re.split(r"^\[[^\]]+\]:", section, maxsplit=1, flags=re.M)[0].strip()
    categories = re.findall(r"^### (.+)$", section, re.M)
    if not categories or len(categories) != len(set(categories)) or not set(categories) <= CATEGORIES:
        raise ValueError(f"Version {version} needs unique Keep a Changelog category headings")
    for category in re.split(r"^### .+$", section, flags=re.M)[1:]:
        if not re.search(r"^- \S", category, re.M):
            raise ValueError(f"Version {version} contains an empty changelog category")
    definitions = dict(re.findall(r"^\[([^\]]+)\]:\s*(.+)$", changelog, re.M))
    references = dict.fromkeys(re.findall(r"\[([^\]]+)\](?!\()", section))
    links = [f"[{label}]: {definitions[label]}" for label in references if label in definitions]
    return section + ("\n\n" + "\n".join(links) if links else "") + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    version = read_version(root)
    notes = extract_release((root / "CHANGELOG.md").read_text(encoding="utf-8"), version)
    if os.environ.get("IS_TAG") == "true" and os.environ.get("RELEASE_TAG") != f"v{version}":
        raise ValueError(f"Release tag must match v{version}")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(notes, encoding="utf-8")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"version={version}\ntag=v{version}\n")
    print(f"Validated release notes for {version}")


if __name__ == "__main__":
    main()
