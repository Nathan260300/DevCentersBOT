import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

# Charger le token depuis le fichier .env
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['games', 'moderation']:
            try:
                await self.load_extension(f"cogs.{extension}")
            except Exception as e:
                print(f"Erreur lors du chargement de l'extension {extension}: {e}")

intents = discord.Intents.all()
bot = MonBot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commande(s) synchronisée(s)")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes: {e}")

keep_alive()
if token:
    bot.run(token=token)
else:
    print("Erreur : Aucun token trouvé. Vérifiez vos variables d'environnement.")
