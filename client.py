import discord

token = "MTMzMzA0MTI4NjcwNTQ0NjkzMg.GBCkuq.Dhmg82UGd6yJkueyJjuMQvbAUNB3Aqqqc-JvJo"

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)