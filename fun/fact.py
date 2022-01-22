import discord

from discord.ext import commands
from random import choice


aliases = ['facts', 'randfact', 'Random_Fact']
description = "It gives out a random fact!"


# Got to 140 on https://www.thefactsite.com/1000-interesting-facts/


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        '''def parse_list_file(file_path: str) -> list:
            with open(file_path) as f:
                return [l.strip() for l in f.readlines() if l.strip()]

        self.database = {
                "factsite": parse_list_file('./fun/FactDatabase/factsite.txt'),
        }

    @commands.command(aliases=aliases, description=description)
    async def fact(self, ctx):
        response = f"**Random Fact:** {choice(self.database['factsite'])}"
        e = discord.Embed(color=discord.Color.random(),
                          title=response,
                          description="From `https://www.thefactsite.com/1000-interesting-facts/`")
        await ctx.reply(embed=e, mention_author=False)'''


def setup(bot):
    bot.add_cog(Fun(bot))
