from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    async def echo(self, ctx, *, mensagem: str):
        await ctx.send(mensagem)

    @commands.command()
    async def about(self, ctx):
        await ctx.send(
            "Olá! Sou um bot desenvolvido na linguagem python.\n"
            "Possuo funções simples, sendo um projeto pessoal para praticar discord.py e boas maneiras."
        )

async def setup(bot):
    await bot.add_cog(Misc(bot))