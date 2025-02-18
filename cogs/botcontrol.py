import os
import sys
import asyncio
from discord.ext import commands
from discord import Embed
import discord

class BotControlCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Redémarre le bot.")
    @commands.is_owner()  
    async def restart(self, ctx):
       
        owner = self.bot.get_user(ctx.author.id)
        
        if owner:
            await ctx.interaction.response.defer()

            embed = discord.Embed(
                title="Redémarrage du bot 🔄",
                description="Le bot va redémarrer dans 5 secondes. Vous allez perdre cette session.",
                color=discord.Color.orange()
            )
          
            await owner.send(embed=embed)
            await asyncio.sleep(3)

            embed_confirm = discord.Embed(
                title="Redémarrage en cours...",
                description="Le bot redémarre maintenant.",
                color=discord.Color.green()
            )
          
            await owner.send(embed=embed_confirm)
            await asyncio.sleep(3)

          
            await asyncio.sleep(3)
            os.execv(sys.executable, ['python'] + sys.argv)  

    @restart.error
    async def restart_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Tu n'as pas la permission de redémarrer le bot.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tu n'as pas fourni d'argument nécessaire.")
        else:
            await ctx.send("Une erreur est survenue.")

    @commands.Cog.listener() 
    async def on_ready(self):
        
        owner = self.bot.get_user(1316068882154393693) 
        if owner:
            embed = Embed(
                title="Redémarrage du bot",
                description="Le bot a été redémarré avec succès et est de retour en ligne !",
                color=0x00FF00 
            )
            await owner.send(embed=embed)
            print("Le bot a été redémarré avec succès et est de retour en ligne !")
 
    @commands.hybrid_command(help="Arrête le bot.")
    @commands.is_owner()
    async def stop(self, ctx):
        """Commande pour arrêter le bot."""
        await ctx.interaction.response.defer()
        embed = discord.Embed(
            title="Arrêt du bot 🔴",
            description="Le bot va s'arrêter maintenant. À bientôt ! 👋",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(BotControlCog(bot))
