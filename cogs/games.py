import random
from discord.ext import commands
import discord

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Lance un dé à 6 faces et affiche le résultat.")
    async def dé(self, ctx):
        result = random.randint(1, 6)
        embed = discord.Embed(
            title="Lancer de dé 🎲",
            description=f"**{ctx.author.name} lance un dé et obtient :** {result}",
            color=discord.Color.blue()
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(help="Effectue un tirage de pile ou face et affiche le résultat.")
    async def pileouface(self, ctx):
        result = random.choice(["pile", "face"])
        embed = discord.Embed(
            title="Tirage Pile ou Face 🪙",
            description=f"**Résultat obtenu :** {result}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(help="Effectue l'addition de deux nombres et affiche le résultat.")
    async def addition(self, ctx: commands.Context, a: int, b: int):
        result = a + b
        embed = discord.Embed(
            title="Addition ➕",
            description=f"**{a} + {b} =** {result}",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(help="Effectue la soustraction de deux nombres et affiche le résultat.")
    async def soustraire(self, ctx: commands.Context, a: int, b: int):
        result = a - b
        embed = discord.Embed(
            title="Soustraction ➖",
            description=f"**{a} - {b} =** {result}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @commands.hybrid_command(help="Effectue la multiplication de deux nombres et affiche le résultat.")
    async def multiplication(self, ctx: commands.Context, a: int, b: int):
        result = a * b
        embed = discord.Embed(
            title="Multiplication ✖️",
            description=f"**{a} x {b} =** {result}",
            color=discord.Color.yellow()
        )
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.bot.user.mentioned_in(message):
            embed = discord.Embed(
                title="Réponse automatique ⚡",
                description="**Quoi 😠 ???!!!??**",
                color=discord.Color.red()
            )
            await message.reply(embed=embed, mention_author=True)
        await self.bot.process_commands(message)
        
    @commands.hybrid_command(help="Une blague...")
    async def ping(self, ctx):
      embed = discord.Embed(
        title="Blague 🤪",
        description="**Pong 🏓 !**",
        color=discord.Color.purple()
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GamesCog(bot))
