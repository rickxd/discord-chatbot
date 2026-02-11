import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

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

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *, mensagem: str):
    await ctx.send(mensagem)

@bot.command()
async def about(ctx):
    await ctx.send(
        "Olá! Sou um bot desenvolvido na linguagem python.\n"
        "Possuo funções simples, sendo um projeto pessoal para aprender discord.py e boas maneiras."
    )

bot.run(TOKEN)