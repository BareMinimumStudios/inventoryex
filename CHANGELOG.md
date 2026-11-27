# Inventory EX 1.0.2

- Upgrade Gradle to 9.9.2 with checksum verification and download retries.
- Update Fabric Loader to 0.20.1 and Fabric API for Minecraft 1.21.1 to 0.116.18.
- Update build, artifact transfer, and MC Publish actions.
- Replace fully qualified code references with imports and a clear ClickType alias.
- Check editing permissions once per click and save inventory changes on menu close.
- Skip malformed missing-dimension data safely and avoid saving without a server.
- Strengthen release validation, including when Python assertions are disabled.

# Inventory EX 1.0.1

- Operators no longer gain inventory viewing or editing immunity by default.
- Explicit immunity permissions remain available through a permissions provider.
- Fix editing immunity checks and enforce level 3 editing defaults.
- Block read-only shift-click, dragging, and double-click transfers.
- Reject offline targets without saved data instead of creating an empty inventory.
- Close the player-data output stream and handle invalid saved dimensions safely.
- Replace unavailable Offline Player Cache dependency with native profile-cache suggestions.
- Check inventory size before populating GUI slots.
- Upgrade Gradle to 9.8.0 with distribution checksum verification.
- Update Cloche to 0.18.10, Fabric Loader to 0.19.5, and Fabric API for both targets.
- Declare server-only environment and enforce Minecraft/Java requirements in release metadata.
- Add pokesmells as an author, refresh branding and documentation.
- Build once and publish separate Minecraft files through MC Publish.
- Remove unused Nix/direnv setup.
