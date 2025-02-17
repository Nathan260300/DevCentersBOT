from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(help="Affiche une liste d'aide avec les commandes disponibles.")
    async def aide(self, ctx):
        tableau = [
            ["**-------------------------------------------------------------------------------**"],
            ["**/aide**", "**__Affiche cette liste d'aide avec les commandes disponibles.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/addition**", "**__Additionne deux nombres donnés.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/dé**", "**__Lance un dé à 6 faces et affiche le résultat.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/kick**", "**__Expulse un utilisateur du serveur.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/multiplication**", "**__Multiplie deux nombres donnés.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/pileouface**", "**__Effectue un tirage de pile ou face.__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/ping**", "**__Une blague...__**"],
            ["**-------------------------------------------------------------------------------**"],
            ["**/soustraire**", "**__Soustrait deux nombres donnés.__**"],
            ["**-------------------------------------------------------------------------------**"]
        ]
        
        tableau_str = ""
        for ligne in tableau:
            if len(ligne) == 2:
                tableau_str += "{:<25} {:<50}\n".format(*ligne)
            else:
                tableau_str += f"{ligne[0]}\n"
        await ctx.send(f"**__Voici toutes les commandes disponibles__ :**\n{tableau_str}")

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
