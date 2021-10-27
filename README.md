# disformers
 - Huggingface transformers for discord
 - base source [butyr/huggingface-transformer-chatbots](https://github.com/butyr/huggingface-transformer-chatbots)

# install
```cmd
pip install -U disformers
```

# example
- see [example](examples) folder


- use client
```python
import discord
from DisFormers import DisFormersBot

client = discord.Client()
disformerbot = DisFormersBot(client, prefix="!")
# DisFormersBot(client,prefix="!",languague="en") default languague is English
# you can choose English(en) or Korean(ko) languague option

@client.event
async def on_ready():
    print("Bot is ready.")
    
@client.event
async def on_message(message):
    await disformerbot.client_message(message=message)

if __name__ == "__main__":
    client.run('token')
```

- use commands.Bot
```python
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
# DisFormersBot(client,prefix="!",languague="en") default languague is English
# you can choose English(en) or Korean(ko) languague option

if __name__ == "__main__":
    my_bot.run("token")
```

# contact
- [Discord](https://discord.gg/Jk6VRvsnqa)
- [Email](mailto:support@spacedev.space)
