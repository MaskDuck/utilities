from __future__ import annotations
from typing import Any, Optional
import nextcord
from nextcord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self._bot: commands.Bot = bot

    @nextcord.slash_command()
    async def scream(
        self,
        interaction: nextcord.Interaction,
        quote: str = nextcord.SlashOption(description="Quote to scream"),
    ) -> Any:
        if len(quote) > 45:
            return await interaction.send("You seems to be trying to spam, don't you?")
        y = ""
        for x in quote:
            y += f":regional_indicator_{x}: "
        await interaction.send(y)


def setup(bot: commands.Bot):
    bot.add_cog(Fun(bot))
