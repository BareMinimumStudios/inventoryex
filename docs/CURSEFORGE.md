# Inventory EX

**Inspect player inventories, Ender Chests, Trinkets, and Accessories from your server.**

Inventory EX is a server-side Fabric mod for Minecraft **1.20.1** and **1.21.1**. View and manage online players' items or inspect saved inventories while players are offline. Players do not need to install Inventory EX on their clients.

## Commands

- `/invsee <name>` — inventory, armor, and offhand.
- `/endsee <name>` — Ender Chest.
- `/trinketsee <name>` — Trinkets, when installed and its Accessories compatibility layer is inactive.
- `/accsee <name>` — Accessories, when installed.

## Staff permissions

Vanilla operator level **2** can view inventories; level **3** can edit them. Operators remain inspectable. LuckPerms and other Fabric Permissions API providers can assign access per command. Explicit `invex.immune.view` and `invex.immune.modify` permissions protect selected players when needed.

Offline players must have existing saved data. Commands are used in-game and accept one target at a time.

## Required dependencies

Install **Fabric API** and **Fabric Language Kotlin** on the server. Minecraft 1.20.1 requires Java 17 or newer; Minecraft 1.21.1 requires Java 21 or newer. Trinkets and Accessories are optional.

## Authors and support

By **naomieow** and **pokesmells**, maintained by **Bare Minimum Studios**.

- [Source and full permission reference](https://github.com/BareMinimumStudios/invex)
- [Report an issue](https://github.com/BareMinimumStudios/invex/issues)
- [Discord](https://discord.gg/pcRw79hwey)

Licensed under the **Bare Minimum License v1.0**.
