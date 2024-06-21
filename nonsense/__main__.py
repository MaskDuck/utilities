from __future__ import annotations
from nextcord.ext import commands
import nextcord

import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()


class NonsenseBot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        self.__doc__ = super().__doc__
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("on ready")


intents = nextcord.Intents.all()
intents.presences = False
intents.typing = False
intents.voice_states = False
bot = NonsenseBot(intents=intents)

bot.load_extension("extensions.docs")
bot.load_extension("extensions.fun")
bot.load_extension("extensions.wikis")

bot.run(os.environ["TOKEN"])
