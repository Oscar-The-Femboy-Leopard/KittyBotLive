import ast
import discord
from discord.ext import commands
from config import Owner_ID, My_Paypal, My_Paypal_2


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

    @commands.command(name='Paypal', alias="paypal", hidden=True)
    @commands.is_owner()
    async def paypal(self, ctx):
        color = discord.colour.Color.blurple()
        pp = discord.Embed(color=color)
        pp.add_field(name="My Business paypal:", value=My_Paypal, inline=False)
        pp.add_field(name="Personal Paypal", value=My_Paypal_2, inline=False)
        pp.set_footer(text=f"Command run by: {ctx.author}")

        await ctx.send(embed=pp)


def setup(bot):
    bot.add_cog(OwnerCog(bot))
