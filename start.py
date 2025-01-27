import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

class MonBot(commands.Bot):
    async def setup_hook(self):
        try:
            await self.load_extension("cogs.games")
            print("Extension 'games' chargée avec succès")
        except Exception as e:
            print(f"Erreur lors du chargement de l'extension 'games' : {e}")

intents = discord.Intents.all()
bot = MonBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisée(s)")
    except Exception as e:
        print(e)

keep_alive()
bot.run(token)
