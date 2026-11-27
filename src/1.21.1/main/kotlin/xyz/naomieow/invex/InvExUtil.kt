package xyz.naomieow.invex

import com.mojang.authlib.GameProfile
import com.mojang.serialization.Dynamic
import net.minecraft.Util
import net.minecraft.nbt.CompoundTag
import net.minecraft.nbt.NbtIo
import net.minecraft.nbt.NbtOps
import net.minecraft.server.MinecraftServer
import net.minecraft.server.level.ClientInformation
import net.minecraft.server.level.ServerPlayer
import net.minecraft.world.entity.player.Player
import net.minecraft.world.level.Level
import net.minecraft.world.level.dimension.DimensionType
import net.minecraft.world.level.storage.LevelResource
import java.io.File
import java.io.FileOutputStream

actual fun Player.`invex$saveData`() {
    val server = this.server ?: return
    val activePlayer = server.playerList.getPlayer(uuid)
    // An offline snapshot must never overwrite a player who has since logged in.
    if (activePlayer != null && activePlayer !== this) return
    val dir = server.getWorldPath(LevelResource.PLAYER_DATA_DIR).toFile()
    try {
        val tag = this.saveWithoutId(CompoundTag())
        val file = File.createTempFile("${this.stringUUID}.tmp", ".dat", dir)
        FileOutputStream(file).use { NbtIo.writeCompressed(tag, it) }
        val current = File(dir, "${this.stringUUID}.dat")
        val old = File(dir, "${this.stringUUID}.dat_old")
        Util.safeReplaceFile(current.toPath(), file.toPath(), old.toPath())
    } catch (e: Exception) {
        InvEx.warn("Failed to save player ${this.name.string}'s data. Error: $e")
    }
}

actual fun MinecraftServer.getOfflinePlayer(gameProfile: GameProfile): ServerPlayer? {
    playerList.getPlayer(gameProfile.id)?.let { return it }

    val targetPlayer = playerList.getPlayerForLogin(gameProfile, ClientInformation.createDefault())
    val tag = playerList.load(targetPlayer).orElse(null) ?: return null
    tag.get("Dimension")?.let { dimension ->
        val dimensionKey = DimensionType.parseLegacy(Dynamic(NbtOps.INSTANCE, dimension))
            .result().orElse(Level.OVERWORLD)
        getLevel(dimensionKey)?.let(targetPlayer::setServerLevel)
    }
    return targetPlayer
}

actual fun trinketsCompatLoaded(): Boolean {
    return InvEx.isModLoaded("accessories_compat_layer")
}