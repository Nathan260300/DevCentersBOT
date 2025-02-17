import random
from discord.ext import commands

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def dé(self, ctx):
        result = random.randint(1, 6)
        await ctx.send(f"**{ctx.author.name} lance un dé et obtient : __{result}__**")

    @commands.hybrid_command()
    async def pileouface(self, ctx):
        result = random.choice(["pile", "face"])
        await ctx.send(f"**Résultat obtenu : __{result}__**")

    @commands.hybrid_command()
    async def addition(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} + {b} = __{a + b}__**")

    @commands.hybrid_command()
    async def soustraire(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} - {b} = __{a - b}__**")

    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send("**Pong 🏓 !**")

    @commands.hybrid_command()
    async def multiplication(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"**{a} x {b} = __{a * b}__**")

async def setup(bot):
    await bot.add_cog(GamesCog(bot))
