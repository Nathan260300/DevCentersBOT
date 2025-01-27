import discord

token = "MTMzMzA0MTI4NjcwNTQ0NjkzMg.GBCkuq.Dhmg82UGd6yJkueyJjuMQvbAUNB3Aqqqc-JvJo"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message: discord.Message):
  if message.author.bot:
    return
  elif message.content.lower().startswith("<@1333041286705446932>"):
    await message.channel.send("Bonjour, c'est le bot")

@client.event
async def on_message_delete(message: discord.Message):
  await message.channel.send(f"{message.author.name} a supprimé {message.content}")

@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
  await after.channel.send(f"{before.content} est devenu {after.content}")

@client.event
async def on_ready():
  print("Le bot est prêt !")

client.run(token=token)