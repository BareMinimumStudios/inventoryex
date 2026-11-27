# Publishing Inventory EX

MC Publish uploads release files from `.github/workflows/build-and-publish.yml`.

| Platform | Project ID | GitHub Actions secret |
| --- | --- | --- |
| [CurseForge](https://www.curseforge.com/minecraft/mc-mods/inventoryex) | `1584857` | `CURSEFORGE_TOKEN` |
| [Modrinth](https://modrinth.com/mod/inventoryex) | `g1ph7wAM` | `MODRINTH_TOKEN` |
| GitHub Releases | This repository | `GITHUB_TOKEN` (provided automatically) |

These IDs have been verified against the public CurseForge listing and Modrinth API. Configure tokens in GitHub repository Settings → Secrets and variables → Actions; never commit them.

1. Track changes under `[Unreleased]` in `CHANGELOG.md`, grouped under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`. Omit empty categories.
2. Before releasing, bump `version` in `build.gradle.kts`, move the changes into `## [<version>] - YYYY-MM-DD`, and update the comparison links. The date is the intended release date; confirm it before publishing.
3. Run `gradlew.bat build` or `./gradlew build`, then `python scripts/prepare_release.py`, and test both server versions.
4. Commit and push the changes.
5. Create and push a matching tag, such as `v1.0.3`, or manually run **Build and Publish** with **Publish** selected.
6. Check the two Minecraft publishing jobs and the GitHub release job, then verify all three destinations.

The build job produces both targets once. Publishing downloads those verified artifacts and uploads only the matching Minecraft JAR for each platform file. Sources and development JARs are excluded by exact filename.

## Changelog and release notes

`CHANGELOG.md` follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/) and Semantic Versioning. Entries are curated for users, with the newest version first and an `[Unreleased]` section for future work. Only published versions have historical release dates; the next dated entry is prepared locally before tagging. The unpublished 1.0.2 development changes are included in 1.0.3.

`scripts/release_notes.py` validates the source version, matching tag, date, and category headings. `scripts/prepare_release.py` verifies both JARs and stages them with **only the current version's notes** in `build/release/`. Both mod platforms and GitHub use that `RELEASE-NOTES.md`; historical releases and `[Unreleased]` are excluded. CI builds and release staging fail when the current version's entry is missing or invalid.

Run the script tests with `python -m unittest discover -s scripts -p "test_*.py"`. Use `python scripts/release_notes.py --output build/RELEASE-NOTES.md` to preview the current release notes without uploading anything.

## Release naming

CurseForge and Modrinth use `<mod-version>+<minecraft-version>-<loader>` for both the visible release name and version number. For the current Fabric build:

- `1.0.3+1.20.1-fabric`
- `1.0.3+1.21.1-fabric`

Inventory EX currently publishes Fabric builds only. A loader name is added only for a loader the project actually builds.

GitHub has one combined release named **Inventory EX 1.0.3**, tagged **v1.0.3**, with both tested JARs attached. This separate job avoids two matrix jobs racing to create the same release. The release tag is validated against the source version before building; manual publication uses the same version tag and pins a newly created tag to the workflow commit.

Normal pushes and pull requests build and validate without publishing. A matching version tag or a manual run with **Publish** selected enables all three destinations. Only the GitHub release job receives `contents: write`; the other jobs retain read access. Repository policy must allow the workflow's GitHub token to create releases.

## Listing artwork and copy

- Icon: `docs/assets/inventory-ex-icon.png` (also bundled in the mod).
- Banner: `docs/assets/inventory-ex-banner.png`.
- CurseForge description: `docs/CURSEFORGE.md`.
- Modrinth description: `docs/MODRINTH.md`.

Both descriptions include the full command and permission reference, installation steps, requirements, offline-player behavior, optional integrations, authors, support, sponsor, and license information. Their banner and repository links are absolute URLs suitable for platform descriptions. Upload the artwork before publishing the descriptions so the banner URL is available.

MC Publish publishes files and changelogs. Updating the listing description, icon, banner, or platform authorship requires project-owner access to each platform's project settings. CurseForge already lists **pokesmells** as owner. Mod metadata does not change platform membership.
