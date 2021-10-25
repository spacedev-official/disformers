import discord
from discord.ext import commands
from DisFormers import DisFormersBot

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("Bot is ready.")


my_bot = MyBot(command_prefix="!", intents=discord.Intents.all())
DisFormersBot(my_bot,prefix="!")

if __name__ == "__main__":
    my_bot.run("token")