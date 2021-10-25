import discord
from DisFormers import DisFormersBot

client = discord.Client()
disformerbot = DisFormersBot(client, prefix="!")

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    await disformerbot.client_message(message=message)


if __name__ == "__main__":
    client.run('token')