import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!hello'):
      await message.channel.send('Hello!')

token = os.getenv('DISCORD_BOT_TOKEN')
if token is None:
    raise ValueError("No DISCORD_BOT_TOKEN provided in environment variables")
client.run(token)