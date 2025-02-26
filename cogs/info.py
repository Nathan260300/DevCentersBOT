import discord
from discord.ext import commands
from discord import app_commands
import psutil  # Module pour obtenir des informations sur les ressources système
import platform  # Module pour obtenir des informations sur le système d'exploitation
import os
import time

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="botinfo", description="Affiche des informations détaillées sur le bot et le système.")
    async def botinfo(self, interaction: discord.Interaction):
        # Informations sur la RAM
        memory_info = psutil.virtual_memory()
        ram_usage = memory_info.percent  # Pourcentage de RAM utilisée
        ram_total = memory_info.total / (1024 ** 3)  # Total de RAM en Go
        ram_used = memory_info.used / (1024 ** 3)  # RAM utilisée en Go
        ram_free = memory_info.available / (1024 ** 3)  # RAM disponible en Go

        # Informations sur la mémoire swap
        swap_info = psutil.swap_memory()
        swap_total = swap_info.total / (1024 ** 3)  # Total de mémoire swap en Go
        swap_used = swap_info.used / (1024 ** 3)  # Swap utilisé en Go
        swap_free = swap_info.free / (1024 ** 3)  # Swap libre en Go
        swap_percent = swap_info.percent  # Utilisation du swap en pourcentage

        # Informations sur le processeur
        cpu_percent = psutil.cpu_percent(interval=1)  # Utilisation du CPU en pourcentage
        cpu_count = psutil.cpu_count(logical=False)  # Nombre de cœurs physiques
        cpu_count_logical = psutil.cpu_count(logical=True)  # Nombre de cœurs logiques
        cpu_freq = psutil.cpu_freq()  # Fréquence du processeur

        # Informations sur le disque
        disk_info = psutil.disk_usage('/')
        disk_total = disk_info.total / (1024 ** 3)  # Espace disque total en Go
        disk_used = disk_info.used / (1024 ** 3)  # Espace disque utilisé en Go
        disk_free = disk_info.free / (1024 ** 3)  # Espace disque libre en Go
        disk_percent = disk_info.percent  # Pourcentage d'utilisation du disque

        # Informations sur les partitions de disque
        partitions = psutil.disk_partitions()

        # Informations sur les processus système
        processes = [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status', 'create_time'])]

        # Charge système (load averages)
        load_avg = os.getloadavg()  # Charge système sur 1, 5, 15 minutes

        # Informations sur le réseau
        net_info = psutil.net_io_counters()
        bytes_sent = net_info.bytes_sent / (1024 ** 2)  # Octets envoyés en Mo
        bytes_recv = net_info.bytes_recv / (1024 ** 2)  # Octets reçus en Mo

        # Interfaces réseau
        net_if_addrs = psutil.net_if_addrs()
        net_if_stats = psutil.net_if_stats()

        # Informations système
        system_info = platform.uname()  # Informations sur le système (OS, version)
        system_name = system_info.system
        system_version = system_info.version
        system_machine = system_info.machine
        system_processor = system_info.processor

        # Batterie (si applicable)
        battery = psutil.sensors_battery()
        battery_percent = battery.percent if battery else None
        battery_seconds_left = battery.secsleft if battery else None

        # Nombre de threads
        threads_count = psutil.cpu_count(logical=False)

        # Modules Python actifs
        python_modules = sorted([module for module in sys.modules.keys()])

        # Temps de fonctionnement du système
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_days = uptime_seconds // (24 * 3600)
        uptime_hours = (uptime_seconds % (24 * 3600)) // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60

        # Informations sur le bot
        embed = discord.Embed(title="Informations sur le Bot et le Système", color=discord.Color.blue())

        # Informations sur le bot
        embed.add_field(name="Nom du Bot", value=self.bot.user.name, inline=False)
        embed.add_field(name="ID du Bot", value=str(self.bot.user.id), inline=False)
        embed.add_field(name="Version de Discord.py", value=discord.__version__, inline=False)
        embed.add_field(name="Serveurs", value=len(self.bot.guilds), inline=False)
        embed.add_field(name="Utilisateurs", value=sum(len(guild.members) for guild in self.bot.guilds), inline=False)
        embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms", inline=False)

        # Informations système
        embed.add_field(name="Système d'Exploitation", value=f"{system_name} {system_version}", inline=False)
        embed.add_field(name="Machine", value=system_machine, inline=False)
        embed.add_field(name="Processeur", value=system_processor, inline=False)

        # CPU
        embed.add_field(name="Utilisation CPU", value=f"{cpu_percent}%", inline=False)
        embed.add_field(name="Cœurs Physiques", value=str(cpu_count), inline=False)
        embed.add_field(name="Cœurs Logiques", value=str(cpu_count_logical), inline=False)
        embed.add_field(name="Fréquence CPU", value=f"{cpu_freq.current} MHz", inline=False)

        # RAM
        embed.add_field(name="Mémoire RAM Totale", value=f"{ram_total:.2f} Go", inline=False)
        embed.add_field(name="RAM Utilisée", value=f"{ram_used:.2f} Go", inline=False)
        embed.add_field(name="RAM Disponible", value=f"{ram_free:.2f} Go", inline=False)
        embed.add_field(name="Utilisation RAM", value=f"{ram_usage}%", inline=False)

        # Swap
        embed.add_field(name="Mémoire Swap Totale", value=f"{swap_total:.2f} Go", inline=False)
        embed.add_field(name="Swap Utilisé", value=f"{swap_used:.2f} Go", inline=False)
        embed.add_field(name="Swap Libre", value=f"{swap_free:.2f} Go", inline=False)
        embed.add_field(name="Utilisation Swap", value=f"{swap_percent}%", inline=False)

        # Disque
        embed.add_field(name="Espace Disque Total", value=f"{disk_total:.2f} Go", inline=False)
        embed.add_field(name="Espace Disque Utilisé", value=f"{disk_used:.2f} Go", inline=False)
        embed.add_field(name="Espace Disque Libre", value=f"{disk_free:.2f} Go", inline=False)
        embed.add_field(name="Utilisation Disque", value=f"{disk_percent}%", inline=False)

        # Partitions de Disque
        embed.add_field(name="Partitions de Disque", value="\n".join([f"{part.device}: {part.mountpoint}, {part.fstype}" for part in partitions]), inline=False)

        # Réseau
        embed.add_field(name="Octets envoyés", value=f"{bytes_sent:.2f} Mo", inline=False)
        embed.add_field(name="Octets reçus", value=f"{bytes_recv:.2f} Mo", inline=False)

        # Interfaces réseau
        net_info_text = "\n".join([f"{iface}: {addr.address} ({net_if_stats[iface].speed} Mbps)" for iface, addrs in net_if_addrs.items() for addr in addrs if addr.family == psutil.AF_INET])
        embed.add_field(name="Interfaces Réseau", value=net_info_text, inline=False)

        # Batterie (si disponible)
        if battery_percent is not None:
            embed.add_field(name="Batterie", value=f"{battery_percent}% restant, {battery_seconds_left // 60} minutes restantes", inline=False)
        else:
            embed.add_field(name="Batterie", value="Pas de batterie détectée", inline=False)

        # Temps d'uptime du système
        embed.add_field(name="Uptime du système", value=f"{int(uptime_days)} jours, {int(uptime_hours)} heures, {int(uptime_minutes)} minutes", inline=False)

        # Temps d'activité du bot
        bot_uptime = time.time() - self.bot.start_time
        bot_uptime_days = bot_uptime // (24 * 3600)
        bot_uptime_hours = (bot_uptime % (24 * 3600)) // 3600
        bot_uptime_minutes = (bot_uptime % 3600) // 60
        embed.add_field(name="Temps d'activité du Bot", value=f"{int(bot_uptime_days)} jours, {int(bot_uptime_hours)} heures, {int(bot_uptime_minutes)} minutes", inline=False)

        # Nombre de threads
        embed.add_field(name="Nombre de Threads", value=str(threads_count), inline=False)

        # Modules Python actifs
        embed.add_field(name="Modules Python Chargés", value=", ".join(python_modules), inline=False)

        # Footer avec l'utilisateur qui a exécuté la commande
        embed.set_footer(text=f"Demande effectuée par {interaction.user}")

        # Envoi de l'embed
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(InfoCog(bot))
