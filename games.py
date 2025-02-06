import random
from discord.ext import commands

class GamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def dé(self, ctx):
        result = random.randint(1, 6)
        await ctx.send(f"{ctx.author.name} lance un dé et obtient : {result}")

    @commands.hybrid_command()
    async def pileouface(self, ctx):
        result = random.choice(["pile", "face"])
        await ctx.send(f"Résultat obtenu : {result}")

    @commands.hybrid_command()
    async def soustraire(self, ctx: commands.Context, a: int, b: int):
        await ctx.send(f"La différence entre {a} et {b} est {a - b}")

    @commands.hybrid_command()
    async def ping(self, ctx):
        await ctx.send("Pong !")

    @commands.hybrid_command(name="multiplication", with_app_command=True)
    async def multiplication(self, ctx: commands.Context, a: int, b: int):
        result = a * b
        await ctx.send(f"{a} x {b} = {result}")

async def setup(bot):
    await bot.add_cog(GamesCog(bot))
