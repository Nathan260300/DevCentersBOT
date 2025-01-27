import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

# Charger le token depuis le fichier .env
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

bot.run(token)
