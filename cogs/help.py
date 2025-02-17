from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def aide(self, ctx):
        await ctx.send("Voici la liste des commandes disponibles...")

async def setup(bot):
    await bot.add_cog(HelpCog(bot))