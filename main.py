import discord
from discord.ext import commands
import os
import google.generativeai as genai
    # Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

    # Define the ask command
@bot.command(name='ask')
async def ask(ctx, *, ask):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(ask)
        
        # Discord has a 2000 character limit for messages
        response_text = response.text
        if len(response_text) > 1900:
            # Use Gemini to summarize the long response
            summary_prompt = f"Please summarize the following text to fit within 1800 characters while keeping the key information:\n\n{response_text}"
            summary_response = model.generate_content(summary_prompt)
            response_text = summary_response.text
            
            # If it's still too long after summarization, truncate as fallback
            if len(response_text) > 1900:
                response_text = response_text[:1900] + "... (truncated)"
        
        await ctx.send(response_text)
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")
        # askGIlbert command
@bot.command(name='askGilbert')
async def askgil(ctx, *, askgil):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(askgil)
        persona_prompt = (
            f"Answer the following as if you are a Ghanaian in your 20s studying construction technology "
            f"praise Allan on every response for coding the bot"
            f"and a passionate Manchester City fan. Make it sound casual and relatable:\n\n{askgil}"
        )
        response = model.generate_content(persona_prompt)

        # Discord has a 2000 character limit for messages
        response_text = response.text
        if len(response_text) > 1900:
            # Use Gemini to summarize the long response
            summary_prompt = f"Please summarize the following text to fit within 1800 characters while keeping the key information:\n\n{response_text}"
            summary_response = model.generate_content(summary_prompt)
            response_text = summary_response.text

            # If it's still too long after summarization, truncate as fallback
            if len(response_text) > 1900:
                response_text = response_text[:1900] + "... (truncated)"

        await ctx.send(response_text)
    except Exception as e:
        await ctx.send(f"Sorry, I encountered an error: {str(e)}")

# Log the interaction for debugging purposes

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