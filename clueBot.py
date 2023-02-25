# Clue discord bot

import os
import discord
from dotenv import load_dotenv

import secrets

load_dotenv()
TOKEN = os.getenv(secrets.botToken)

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)
