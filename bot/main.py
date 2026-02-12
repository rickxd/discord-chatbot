import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"O bot {bot.user} está conectado!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Você esqueceu de passar a mensagem.")
    else:
        raise error

async def main():
    await bot.load_extension("cogs.misc")
    await bot.start(TOKEN)

asyncio.run(main())