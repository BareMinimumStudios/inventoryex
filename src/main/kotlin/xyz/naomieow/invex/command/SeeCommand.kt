package xyz.naomieow.invex.command

import com.mojang.brigadier.context.CommandContext
import me.lucko.fabric.api.permissions.v0.Permissions
import net.minecraft.commands.CommandSourceStack
import net.minecraft.commands.arguments.GameProfileArgument
import net.minecraft.network.chat.Component
import net.minecraft.server.level.ServerPlayer
import xyz.naomieow.invex.InvExPermissions
import xyz.naomieow.invex.gui.SeeGUI
import xyz.naomieow.invex.getOfflinePlayer

object SeeCommand {
    fun executes(guiFn: (player: ServerPlayer, target: ServerPlayer) -> SeeGUI): (CommandContext<CommandSourceStack>) -> Int {
        return cb@ { ctx ->
            val player = ctx.source.player
            if (player == null) {
                ctx.source.sendFailure(Component.translatableWithFallback(
                    "invex.command.error.non_player_env",
                    "Attempted to call command from non-player environment"
                ))
                return@cb 0
            }

            val profiles = GameProfileArgument.getGameProfiles(ctx, "target")
            // Selectors must resolve to exactly one profile.
            if (profiles.size != 1) {
                ctx.source.sendFailure(Component.translatableWithFallback(
                    "invex.command.error.one_player",
                    "Select exactly one player"
                ))
                return@cb 0
            }

            val targetPlayerProfile = profiles.first()

            val targetPlayer = ctx.source.server.getOfflinePlayer(targetPlayerProfile)

            if (targetPlayer == null) {
                ctx.source.sendFailure(Component.translatableWithFallback(
                    "invex.command.error.data_not_found",
                    "Data for player %s not found",
                    targetPlayerProfile.name
                ))
                return@cb 0
            }

            if (Permissions.check(targetPlayer, InvExPermissions.IMMUNE_VIEW, false)) {
                ctx.source.sendFailure(Component.translatableWithFallback(
                    "invex.command.error.immune",
                    "%s is immune to being viewed",
                    targetPlayer.name.string
                ))
                return@cb 0
            }

            val gui = guiFn(player, targetPlayer)
            if (gui.open()) {
                return@cb 1
            }
            ctx.source.sendFailure(Component.translatableWithFallback(
                "invex.command.error.gui_fail",
                "Failed to open menu"
            ))
            return@cb 0
        }
    }
}