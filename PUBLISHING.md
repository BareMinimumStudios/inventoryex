# Publishing Inventory EX

MC Publish uploads release files from `.github/workflows/build-and-publish.yml`.

| Platform | Project ID | GitHub Actions secret |
| --- | --- | --- |
| [CurseForge](https://www.curseforge.com/minecraft/mc-mods/inventoryex) | `1584857` | `CURSEFORGE_TOKEN` |
| [Modrinth](https://modrinth.com/mod/inventoryex) | `g1ph7wAM` | `MODRINTH_TOKEN` |

These IDs have been verified against the public CurseForge listing and Modrinth API. Configure tokens in GitHub repository Settings → Secrets and variables → Actions; never commit them.

1. Update `version` in `build.gradle.kts` and `CHANGELOG.md`.
2. Run `gradlew.bat build` or `./gradlew build` and test both server versions.
3. Commit and push the changes.
4. Create and push a matching tag, such as `v1.0.1`, or manually run **Build and Publish** with **Publish** selected.
5. Check both publishing jobs and both platform listings.

The build job produces both targets once. Publishing downloads those verified artifacts and uploads only the matching Minecraft JAR for each platform file. Sources and development JARs are excluded by exact filename.

## Listing artwork and copy

- Icon: `docs/assets/inventory-ex-icon.png` (also bundled in the mod).
- Banner: `docs/assets/inventory-ex-banner.png`.
- CurseForge description: `docs/CURSEFORGE.md`.
- Modrinth description: `docs/MODRINTH.md`.

Both descriptions include the full command and permission reference, installation steps, requirements, offline-player behavior, optional integrations, authors, support, sponsor, license, and build information. Their banner and repository links are absolute URLs suitable for platform descriptions. Upload the artwork before publishing the descriptions so the banner URL is available.

MC Publish publishes files and changelogs. Updating the listing description, icon, banner, or platform authorship requires project-owner access to each platform's project settings. CurseForge already lists **pokesmells** as owner. Mod metadata does not change platform membership.

The artwork was created with built-in ImageGen. Icon prompt: warm ivory chest with a 3×3 inventory grid and magnifying glass, thick near-black outlines, subtle print texture, transparent background. Banner prompt: matching chest emblem and the exact title “Inventory EX” in a wide layout.
