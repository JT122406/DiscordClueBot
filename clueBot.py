# Clue discord bot

import os

import discord
from discord import app_commands
from discord.ext import commands
from config import DISCORD_TOKEN
import random

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
suspect = ["Colonel Mustard", "Miss Scarlet", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"]
weapon = ["Candlestick", "Knife", "Lead Pipe", "Revolver", "Rope", "Wrench"]
room = ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"]
deck = suspect + weapon + room

@bot.event
async def on_ready():
    print("Bot is ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!")


bot.run(DISCORD_TOKEN)
