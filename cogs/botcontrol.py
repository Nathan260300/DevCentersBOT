import os
import sys
import requests
import asyncio
from discord.ext import commands
import discord

class BotControlCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Redémarre le bot après un délai.")                                                                                                                                             
    @commands.is_owner()  
    async def restart(self, ctx):
        
        
        embed = discord.Embed(
            title="Redémarrage du bot 🔄",
            description="Le bot va redémarrer dans 5 secondes. Vous allez perdre cette session.",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

        
        await asyncio.sleep(5)

      
        embed_confirm = discord.Embed(
            title="Redémarrage en cours...",
            description="Le bot redémarre maintenant.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed_confirm)

        try:
            
            headers = {
                "Authorization": "YUSEBHSEBHSEBHSEBHSEBHSEBHSEBHVGN14561231"  # Le même token secret que dans `keep_alive.py`
            }
            requests.post("http://127.0.0.1:8080/restart", headers=headers)
        except requests.exceptions.RequestException as e:
            await ctx.send(f"Erreur lors du redémarrage via Flask: {e}")

     
        os.execv(sys.executable, ['python'] + sys.argv)  

    @restart.error
    async def restart_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Tu n'as pas la permission de redémarrer le bot.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Tu n'as pas fourni d'argument nécessaire.")
        else:
            await ctx.send("Une erreur est survenue.")


async def setup(bot):
    await bot.add_cog(BotControlCog(bot))
