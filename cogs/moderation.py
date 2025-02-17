import asyncio
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

    @commands.hybrid_command(help="Supprime un nombre de messages spécifié.")
    async def clear(self, ctx, nombre: int):
        if nombre <= 0:
            await ctx.send("**Veuillez entrer un nombre valide de messages à supprimer.**", delete_after=5)
            return
        deleted = await ctx.channel.purge(limit=nombre)
        if len(deleted) == 0:
            await ctx.send("**Aucun message à supprimer.**", delete_after=5)
            return
        confirmation_msg = await ctx.channel.send(f"**{len(deleted)} messages supprimés.**")
        await asyncio.sleep(1)
        await confirmation_msg.delete()
        try:
            await ctx.message.delete()
        except discord.errors.NotFound:
            pass 
    
    @commands.hybrid_command(help="Répète un message un nombre spécifié de fois.")
    @commands.has_permissions(manage_messages=True)
    async def repete(self, ctx: commands.Context, nombre: int, message: str):
        await ctx.send(message)
        for _ in range(1, nombre):
            await ctx.send(message)
    @repete.error
    async def repete_error(self, ctx: commands.Context, error: Exception):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("**Vous n'avez pas la permission d'exécuter cette commande.**", delete_after=5)
        
async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
