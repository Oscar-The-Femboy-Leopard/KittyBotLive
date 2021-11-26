import ast
import discord
import datetime

from discord.ext import commands
from config import Owner_ID


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

    @commands.command(name='boostperks', alias="BoostPerks", hidden=True)
    @commands.is_owner()
    async def open(self, ctx):

        guild = self.bot.get_guild(841496169556475975)
        channel = self.bot.get_channel(841665459531415562)
        emoji = self.bot.get_emoji(id=880240953691082792)

        part = "> Passively gain server currency\n\n> Your own custom role\n\n> The booster role being hoisted " \
               "higher, showing your passion for the server"

        partner = discord.Embed(color=discord.Color.green())
        partner.add_field(name="What do you get for boosting us? This is what rewards you can get:", value=part, inline=False)
        partner.set_thumbnail(url=guild.icon_url)
        partner.set_footer(text=f"Revised on: {datetime.date.today()}")

        await self.bot.get_guild(841496169556475975).get_channel(850690984316370954).purge(limit=10)
        await self.bot.get_guild(841496169556475975).get_channel(850690984316370954).send(f"{emoji} Booster Perks! {emoji}", embed=partner)
        await self.bot.get_guild(841496169556475975).get_channel(850690984316370954).send("And more perks to come!")

        await ctx.send("Sent the Booster Perks")


def setup(bot):
    bot.add_cog(OwnerCog(bot))