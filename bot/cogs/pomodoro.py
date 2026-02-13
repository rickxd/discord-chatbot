from discord.ext import commands

class Pomodoro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pomodoro(self, ctx):
        await ctx.send("WIP")

async def setup(bot):
    await bot.add_cog(Pomodoro(bot))