import discord
from discord.ext import commands
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@bot.command(name = 'query')
async def query(ctx, *, query):
    response = genai.generate_text(
        model="models/text-bison-001",
        prompt=query,
        temperature=0.7,
        max_output_tokens=800,
    )
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