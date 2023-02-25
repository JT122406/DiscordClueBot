# Clue discord bot

import os

import discord
from discord import app_commands
from discord.ext import commands
from config import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


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
