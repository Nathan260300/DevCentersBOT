import discord
from discord.ext import commands

token = "MTMzMzA0MTI4NjcwNTQ0NjkzMg.GBCkuq.Dhmg82UGd6yJkueyJjuMQvbAUNB3Aqqqc-JvJo"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.hybrid_command()
async def ping(ctx):
    await ctx.send("Pong !")

@bot.hybrid_command()
async def soustraire(ctx, a: int, b: int):
    await ctx.send(f"La différence entre {a} et {b} est {a - b}")

@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run(token=token)