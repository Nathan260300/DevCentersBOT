import random
from discord.ext import commands

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Lance un dé à 6 faces et affiche le résultat.")
    async def dé(self, ctx):
        result = random.randint(1, 6)
        await ctx.send(f"**{ctx.author.name} lance un dé et obtient : __{result}__**")

    @commands.hybrid_command(help="Effectue un tirage de pile ou face et affiche le résultat.")
    async def pileouface(self, ctx):
        result = random.choice(["pile", "face"])
        await ctx.send(f"**Résultat obtenu : __{result}__**")

    @commands.hybrid_command(help="Effectue l'addition de deux nombres et affiche le résultat.")
    async def addition(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} + {b} = __{a + b}__**")

    @commands.hybrid_command(help="Effectue la soustraction de deux nombres et affiche le résultat.")
    async def soustraire(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} - {b} = __{a - b}__**")

    @commands.hybrid_command(help="Une blague...")
    async def ping(self, ctx):
        await ctx.send("**Pong 🏓 !**")

    @commands.hybrid_command(help="Effectue la multiplication de deux nombres et affiche le résultat.")
    async def multiplication(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} x {b} = __{a * b}__**")

    @commands.Cog.listener()
    async def on_message(self, message):
      if message.author == self.bot.user:
        return
      if self.bot.user.mentioned_in(message):
        await message.reply("**Quoi 😠 ???!!!??**", mention_author=True)
      await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(GamesCog(bot))
