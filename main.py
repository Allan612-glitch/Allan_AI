import discord
from discord.ext import commands
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name='query')
async def query(ctx, *, query):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(query)
        await ctx.send(response.text)
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    await bot.process_commands(message)

token = os.getenv('DISCORD_BOT_TOKEN')
if token is None:
    raise ValueError("No DISCORD_BOT_TOKEN provided in environment variables")
bot.run(token)