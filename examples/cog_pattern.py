"""Portfolio excerpt: simplified Discord interaction pattern.

This file is intentionally incomplete and is not a runnable bot module.
Production permissions, configuration, error handling and services are private.
"""

from __future__ import annotations

from typing import Protocol

import discord
from discord import app_commands
from discord.ext import commands


class StatusService(Protocol):
    async def get_public_snapshot(self) -> dict: ...


def build_status_embed(snapshot: dict) -> discord.Embed:
    """Reduced public example; production formatting is private."""
    embed = discord.Embed(title="Server status")
    embed.add_field(name="Status", value=str(snapshot.get("status", "unknown")))
    embed.add_field(name="Players", value=str(snapshot.get("players", "-")))
    return embed


class StatusCog(commands.Cog):
    """Small showcase excerpt, not the production cog."""

    def __init__(self, bot: commands.Bot, status_service: StatusService):
        self.bot = bot
        self.status_service = status_service

    @app_commands.command(name="server_status", description="Show a public status snapshot")
    async def server_status(self, interaction: discord.Interaction) -> None:
        snapshot = await self.status_service.get_public_snapshot()
        await interaction.response.send_message(
            embed=build_status_embed(snapshot),
            ephemeral=True,
        )
