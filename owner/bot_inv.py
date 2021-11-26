import ast
import datetime

import discord
from discord.ext import commands
from config import Owner_ID, INVITE, _blnk_value


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.author = Owner_ID
        self.bot = bot

    @commands.command(name='invite', alias='Bot Invite', hidden=True)
    @commands.is_owner()
    async def invite(self, ctx):
        color = discord.colour.Color.blurple()
        inv = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        inv.add_field(name=_blnk_value, value=f"Click [here]({INVITE}) to use my invite", inline=False)
        inv.set_footer(text=f"Command run by: {ctx.author}")

        await ctx.send(embed=inv)


def setup(bot):
    bot.add_cog(OwnerCog(bot))