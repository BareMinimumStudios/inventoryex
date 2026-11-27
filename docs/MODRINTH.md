![Inventory EX](https://raw.githubusercontent.com/BareMinimumStudios/invex/main/docs/assets/inventory-ex-banner.png)

**Fabric · Minecraft 1.20.1 and 1.21.1 · Server-side**

# Inventory EX

Inventory EX gives server staff a clear view of player inventories and Ender Chests, with permission-controlled editing and support for saved offline players. Optional Trinkets and Accessories integration brings equipment slots into the same workflow.

Install it on your Fabric server. Players do not need Inventory EX on their clients.

## Features

- Inspect a player's main inventory, hotbar, armor, and offhand.
- Open Ender Chests without asking the player to log in.
- View saved inventories for offline players who have existing world data.
- Keep viewing and editing permissions separate for each command.
- Inspect operators too; operator status does not grant immunity.
- Switch between available inventory and equipment menus using the menu buttons.
- Inspect Trinkets or Accessories when those mods are installed.

## Installation

1. Download the Inventory EX file for your server's Minecraft version.
2. Install Fabric Loader, Fabric API, and Fabric Language Kotlin on the server.
3. Put the Inventory EX JAR in the server's `mods` folder and restart it.
4. Grant staff the appropriate operator level or permission nodes, then use `/invsee <name>`.

### Supported versions

| Minecraft | Java | Fabric API |
| --- | --- | --- |
| 1.20.1 | 17 or newer | 0.92.12 or newer for 1.20.1 |
| 1.21.1 | 21 or newer | 0.116.18 or newer for 1.21.1 |

The current build uses Fabric Loader 0.20.1 and requires Fabric Language Kotlin 1.13.7+kotlin.2.2.21 or newer. Use dependency files matching your Minecraft version. SGUI and Fabric Permissions API are bundled with Inventory EX.

Trinkets and Accessories are optional. Install them only if your server uses their equipment systems; Inventory EX does not add those systems itself.

## Commands

| Command | Opens | Availability |
| --- | --- | --- |
| `/invsee <name>` | Main inventory, hotbar, armor, and offhand | Always |
| `/endsee <name>` | Ender Chest | Always |
| `/trinketsee <name>` | Trinkets equipment | Trinkets installed and its Accessories compatibility layer inactive |
| `/accsee <name>` | Accessories equipment | Accessories installed |

Run commands in-game as a player and select exactly one target. The menus include navigation buttons for the inventory types you have permission to open.

## Permissions

With vanilla operator permissions, **level 2 can view** and **level 3 can edit**. Authorized staff can inspect operators; becoming an operator does not make a player immune.

With a Fabric Permissions API provider such as LuckPerms, configure viewing and editing separately:

| Inventory type | View permission | Edit permission |
| --- | --- | --- |
| Inventory | `invex.invsee.command` | `invex.invsee.modify` |
| Ender Chest | `invex.endsee.command` | `invex.endsee.modify` |
| Trinkets | `invex.trinketsee.command` | `invex.trinketsee.modify` |
| Accessories | `invex.accsee.command` | `invex.accsee.modify` |

Grant the view permission to open a menu and the matching edit permission to change its contents. Viewing access alone blocks direct item moves, shift-click transfers, dragging, and double-click collection involving the target inventory.

### Optional immunity

| Target permission | Effect |
| --- | --- |
| `invex.immune.view` | Prevents the target's inventories from being opened |
| `invex.immune.modify` | Allows viewing but prevents editing |

Immunity is opt-in through your permissions provider. Wildcard grants can include these nodes; explicitly set them to `false` if those staff accounts should remain inspectable.

## Offline players and saving

Offline inventories are loaded from the world's saved player data. A player who has never joined that world has no saved inventory to inspect. Name suggestions include online players and saved offline players whose profiles Minecraft has cached.

Changes to a saved offline inventory are written back when an editable menu closes. Close the menu after editing before checking the saved result. Keep your normal world backups when managing player data.

## Equipment integration

Trinkets and Accessories commands appear only when the corresponding mod is installed. The Trinkets command is hidden when its Accessories compatibility layer is active, avoiding duplicate access to the same equipment system.

The current menus support up to **45 target slots**. Equipment layouts with more than 45 slots cannot be opened; there is no paginated equipment view in this version.

## Common questions

### Do players need the mod installed

No. Inventory EX is installed on the server and uses ordinary inventory menus. Other mods on your server may have their own client requirements.

### Why can I view an inventory but not edit it

Viewing and editing are separate permissions. Check the matching `.modify` node, your operator level, and whether the target has `invex.immune.modify`.

### Why is an operator still protected

Check explicit immunity permissions and wildcard grants in your permissions provider. Operator status alone does not enable immunity.

### Why is an offline name missing

The world must contain saved data for that player, and name suggestions depend on Minecraft's cached profiles. Inventory EX does not create an inventory for a player who has never joined.

## Authors and support

Maintained by **Bare Minimum Studios**. Authors: [naomieow](https://github.com/naomieow) and [pokesmells](https://github.com/pokesmells).

- [CurseForge](https://www.curseforge.com/minecraft/mc-mods/inventoryex)
- [Modrinth](https://modrinth.com/mod/inventoryex)
- [Source](https://github.com/BareMinimumStudios/invex)
- [Report an issue](https://github.com/BareMinimumStudios/invex/issues)
- [Discord](https://discord.gg/pcRw79hwey)

When reporting a problem, include your Minecraft and Inventory EX versions, the relevant command, your permissions setup, and whether the target was online or offline.

## Sponsor

[BisectHosting](https://bisecthosting.com/bareminimum) supports Bare Minimum Studios. Use code **`bareminimum`** for **25% off your first month**.

## License

Inventory EX is licensed under the **Bare Minimum License v1.0**. See the [license](https://github.com/BareMinimumStudios/invex/blob/main/LICENSE).
