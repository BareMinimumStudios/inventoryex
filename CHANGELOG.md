# Changelog

All notable changes to Inventory EX are documented here.

The format is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/),
and the project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.3] - 2026-11-27

### Added

- Publish one GitHub release containing both Minecraft builds, alongside CurseForge and Modrinth releases.
- Validate dated changelog entries and prepare release notes containing only the version being published.
- Check release JAR metadata, bundled libraries, author credits, artwork, and Java requirements before publishing.

### Changed

- Bump the mod version to 1.0.3, including the previously unpublished 1.0.2 development changes.
- Use release names such as `1.0.3+1.21.1-fabric` on CurseForge and Modrinth.
- Update Gradle to 9.9.2, Fabric Loader to 0.20.1, and Fabric API for Minecraft 1.21.1 to 0.116.18.
- Refresh the logo, banner, installation instructions, and permission reference.
- Use imports and descriptive aliases to keep inventory and build code readable.
- Check edit permissions once per click and save edited player data when the menu closes.
- Stream name-suggestion processing and omit duplicate online and offline player names.

### Fixed

- Reject console commands before loading offline player data.
- Identify online targets by UUID and simplify offline loading without redundant null checks.
- Prevent an offline inventory snapshot from overwriting a player who has since logged in.
- Keep selector and missing-data errors consistent with their translations and avoid forced nullable-player access.
- Handle missing saved dimensions safely and skip saving when no server is available.

## [1.0.1] - 2026-10-12

### Added

- Credit pokesmells as an author and refresh the project branding and documentation.
- Build both supported Minecraft targets and publish files through MC Publish.

### Changed

- Allow authorized staff to inspect operators; operator status no longer grants automatic immunity.
- Preserve explicitly assigned viewing and editing immunity permissions.
- Use vanilla operator level 2 for viewing and level 3 for editing.
- Use Minecraft's saved player data and profile cache instead of the unavailable Offline Player Cache dependency.
- Update Gradle to 9.8.0, Cloche to 0.18.10, and compatible Fabric dependencies.
- Declare the server environment and Minecraft and Java requirements in mod metadata.

### Removed

- Remove the unused Nix and direnv development setup.

### Fixed

- Enforce editing immunity without an asynchronous race.
- Block read-only transfers through shift-click, dragging, and double-click collection.
- Reject offline targets without saved data instead of creating an empty inventory.
- Close player-data output streams and handle invalid saved dimensions safely.
- Check container size before populating inventory menus.

## [1.0.0] - 2026-06-23

### Added

- Initial public Fabric release for Minecraft 1.20.1 and 1.21.1.
- Inspect player inventories and Ender Chests, including saved offline players.
- Integrate optional Trinkets and Accessories equipment views.
- Control viewing, editing, and immunity through vanilla operator levels or Fabric Permissions API.

[Unreleased]: https://github.com/BareMinimumStudios/invex/compare/v1.0.3...HEAD
[1.0.3]: https://github.com/BareMinimumStudios/invex/compare/35ba964...v1.0.3
[1.0.1]: https://github.com/BareMinimumStudios/invex/compare/v1.0.0...35ba964
[1.0.0]: https://github.com/BareMinimumStudios/invex/releases/tag/v1.0.0
