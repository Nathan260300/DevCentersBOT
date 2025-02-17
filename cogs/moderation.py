import discord
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Expulse un utilisateur du serveur.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member.name} a été exclu(e) pour : {reason}")
        except Exception as e:
            await ctx.send(f"Impossible d'exclure {member.name}. Erreur : {str(e)}")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
