<p align="center">
  <img src="docs/assets/inventory-ex-banner.png" alt="Inventory EX" />
</p>

<p align="center">
  <a href="LICENSE"><img alt="BML 1.0 License" src="https://img.shields.io/badge/LICENSE-BML%201.0-FFFFFF?style=for-the-badge&labelColor=1A1A1A" /></a>
  <a href="https://github.com/BareMinimumStudios/invex/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/BareMinimumStudios/invex?style=for-the-badge&logo=github&labelColor=1A1A1A&color=FFFFFF" /></a>
</p>

<p align="center">
  <a href="https://www.curseforge.com/minecraft/mc-mods/inventoryex"><img alt="Available on CurseForge" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/curseforge_vector.svg" /></a>
  <a href="https://modrinth.com/mod/inventoryex"><img alt="Available on Modrinth" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/available/modrinth_vector.svg" /></a>
  <img alt="Fabric" src="https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/supported/fabric_vector.svg" />
</p>

<p align="center"><strong>Minecraft 1.20.1 + 1.21.1 · Fabric · Server-side</strong></p>

# Inventory EX

Inventory EX lets server staff inspect and manage player inventories and Ender Chests, including saved inventories of offline players. It also supports Trinkets and Accessories when those mods are installed. Players can use ordinary Minecraft clients; install Inventory EX and its required dependencies on the server.

Maintained by **Bare Minimum Studios**. Authors: [naomieow](https://github.com/naomieow) and [pokesmells](https://github.com/pokesmells).

## Commands

| Command | Opens |
| --- | --- |
| `/invsee <name>` | Main inventory, armor, and offhand |
| `/endsee <name>` | Ender Chest |
| `/trinketsee <name>` | Trinkets; hidden when the Accessories compatibility layer is active |
| `/accsee <name>` | Accessories |

Commands must be used by a player and target exactly one player. Offline targets need existing saved player data. Name suggestions include online players and saved offline players whose profiles are cached by Minecraft.

## Permissions

With vanilla permissions, **operator level 2 can view** and **level 3 can edit**. Operators can have their inventories viewed and edited by authorized staff; operator status does not grant immunity.

With a permissions provider such as LuckPerms, grant individual permissions:

| Viewer permission | Editing permission |
| --- | --- |
| `invex.invsee.command` | `invex.invsee.modify` |
| `invex.endsee.command` | `invex.endsee.modify` |
| `invex.trinketsee.command` | `invex.trinketsee.modify` |
| `invex.accsee.command` | `invex.accsee.modify` |

Explicitly granting `invex.immune.view` protects a target from viewing. Granting `invex.immune.modify` allows viewing but blocks editing. Neither permission is granted by vanilla operator status. Wildcard permissions can grant immunity too; set these nodes to false if staff should remain inspectable.

## Requirements

| Minecraft | Java | Required mods |
| --- | --- | --- |
| 1.20.1 | 17 or newer | Fabric API, Fabric Language Kotlin |
| 1.21.1 | 21 or newer | Fabric API, Fabric Language Kotlin |

Trinkets and Accessories are optional. SGUI and Fabric Permissions API are bundled. Offline player lookup uses Minecraft's own profile cache and saved player files.

## Building and publishing

The project uses Gradle **9.8.0**, Kotlin, and Cloche. Install Java 17 and 21 and expose their installation directories through `JDK17` and `JDK21` when Gradle cannot discover them.

```sh
./gradlew build
```

On Windows, use `gradlew.bat build`. Both Minecraft targets are built together.

GitHub Actions validates pushes and pull requests, then uses **MC Publish** to upload each target to CurseForge and Modrinth on a matching `v<version>` tag. Manual runs build by default; select **Publish** to upload. Set repository secrets `CURSEFORGE_TOKEN` and `MODRINTH_TOKEN` before publishing. See [PUBLISHING.md](PUBLISHING.md) for project IDs, release steps, and listing assets.

## Links

- [CurseForge](https://www.curseforge.com/minecraft/mc-mods/inventoryex)
- [Modrinth](https://modrinth.com/mod/inventoryex)
- [Source](https://github.com/BareMinimumStudios/invex)
- [Issues](https://github.com/BareMinimumStudios/invex/issues)
- [Discord](https://discord.gg/pcRw79hwey)

## Sponsor

[![Sponsor Banner](https://www.bisecthosting.com/partners/custom-banners/db76a74a-a111-4660-98b7-5a75c15a5951.png)](https://bisecthosting.com/bareminimum)

Use code **`bareminimum`** to get **25% off your first month**!

## License

Inventory EX is licensed under the **Bare Minimum License v1.0**. See [LICENSE](LICENSE).
