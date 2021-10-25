"""
Adapted from:
https://www.machinecurve.com/index.php/2021/03/16/easy-chatbot-with-dialogpt-machine-learning-and-huggingface-transformers/
"""
from typing import Union

from transformers import AutoModelForCausalLM, AutoTokenizer
import os
from discord import (
    Message,
    Client
)
from discord.ext import commands

class DisFormersBot:
    def __init__(
        self,
        client: Union[commands.Bot,Client],
        prefix: str,
        languague: str = "en",
    ):
        if languague == "en":
            model_name = 'microsoft/DialoGPT-small'
            if not os.path.exists('./models/dialogpt'):
                AutoModelForCausalLM.from_pretrained(model_name).save_pretrained('./models/dialogpt')
                AutoTokenizer.from_pretrained(model_name).save_pretrained('./models/dialogpt')
        if languague == "ko":
            model_name = 'byeongal/Ko-DialoGPT'
            if not os.path.exists('./models/dialogpt'):
                AutoModelForCausalLM.from_pretrained(model_name).save_pretrained('./models/dialogpt')
                AutoTokenizer.from_pretrained(model_name).save_pretrained('./models/dialogpt')
        super().__init__()
        self.model = AutoModelForCausalLM.from_pretrained('./models/dialogpt')
        self.tokenizer = AutoTokenizer.from_pretrained('./models/dialogpt')
        self.bot = client
        self.prefix = prefix
        if type(self.bot) == commands.Bot:
            self.bot.add_listener(self.__hendle_messages, "on_message")


    def __call__(self, inputs: str) -> str:
        inputs_tokenized = self.tokenizer.encode(inputs+ self.tokenizer.eos_token, return_tensors='pt')
        reply_ids = self.model.generate(inputs_tokenized, max_length=1250, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(
            reply_ids[:, inputs_tokenized.shape[-1] :][0], skip_special_tokens=True
        )


    async def __hendle_messages(self, message: Message):
        if message.author.bot:
            return
        if message.content.startswith(self.prefix):
            async with message.channel.typing():
                user_input = message.content[len(self.prefix):]
            await message.reply(content=self(user_input))

    async def client_message(self,message:Message):
        if message.author.bot:
            return
        if message.content.startswith(self.prefix):
            async with message.channel.typing():
                user_input = message.content[len(self.prefix):]
            await message.reply(content=self(user_input))
