from discord.ext import commands

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def levels(self, ctx):
        await ctx.send("WIP")

async def setup(bot):
    await bot.add_cog(Levels(bot))