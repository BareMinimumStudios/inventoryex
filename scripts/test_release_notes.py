"""Regression checks for release-note selection and publication safeguards."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from release_notes import extract_release, read_version

SAMPLE = """# Changelog

## [Unreleased]

### Added

- Future change.

## [1.0.3] - 2026-11-27

### Fixed

- Current fix.

## [1.0.1] - 2026-10-12

### Added

- Old change.

[1.0.3]: https://example.com/compare
[1.0.1]: https://example.com/old
"""


class ReleaseNotesTests(unittest.TestCase):
    def test_only_requested_release_is_published(self):
        notes = extract_release(SAMPLE, "1.0.3")
        self.assertIn("Current fix.", notes)
        self.assertIn("[1.0.3]: https://example.com/compare", notes)
        self.assertNotIn("Future change", notes)
        self.assertNotIn("Old change", notes)
        self.assertNotIn("example.com/old", notes)

    def test_missing_release_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE, "1.0.4")

    def test_invalid_date_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE.replace("2026-11-27", "2026-02-30"), "1.0.3")

    def test_missing_date_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE.replace(" - 2026-11-27", ""), "1.0.3")

    def test_unknown_category_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE.replace("### Fixed", "### Misc"), "1.0.3")

    def test_empty_category_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE.replace("- Current fix.", ""), "1.0.3")

    def test_duplicate_release_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE + "\n## [1.0.3] - 2026-11-27\n", "1.0.3")

    def test_missing_unreleased_is_rejected(self):
        with self.assertRaises(ValueError):
            extract_release(SAMPLE.replace("## [Unreleased]", "## [Future]"), "1.0.3")

    def test_invalid_source_version_is_rejected(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "build.gradle.kts").write_text('version = "main"\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                read_version(root)


if __name__ == "__main__":
    unittest.main()
