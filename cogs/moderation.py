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
        
    @commands.hybrid_command(help="Bannit un membre définitivement du serveur.")
    @commands.has_permissions(ban_members=True)  
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason: str = "Aucune raison spécifiée"):
        """Commande pour bannir un membre avec une raison"""
        if ctx.author == member:
            await ctx.send("❌ **Vous ne pouvez pas vous bannir vous-même !**", delete_after=5)
            return
        if ctx.guild.owner_id == member.id:
            await ctx.send("❌ **Vous ne pouvez pas bannir le propriétaire du serveur !**", delete_after=5)
            return
        if ctx.author.top_role <= member.top_role:
            await ctx.send("❌ **Vous ne pouvez pas bannir un membre ayant un rôle égal ou supérieur au vôtre !**", delete_after=5)
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(f"✅ **{member.mention} a été banni pour la raison :** {reason}")
        except discord.errors.Forbidden:
            await ctx.send("❌ **Je n'ai pas la permission de bannir ce membre.**", delete_after=5)
    @ban.error
    async def ban_error(self, ctx: commands.Context, error: Exception):
        """Gestion des erreurs pour la commande ban"""
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("🚫 **Vous n'avez pas la permission de bannir des membres !**", delete_after=5)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("⚠ **Veuillez mentionner un membre à bannir.**\nExemple : `/ban @membre raison`", delete_after=5)
        elif isinstance(error, commands.BadArgument):
            await ctx.send("⚠ **Membre introuvable. Veuillez mentionner un utilisateur valide.**", delete_after=5)


async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
