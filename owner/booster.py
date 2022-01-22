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
    async def perks(self, ctx):

        owner = [
            895656099376681011,
            670932463077556224,
        ]

        if ctx.author.id not in owner:
            return

        guild = self.bot.get_guild(913007198488133632)
        channel = self.bot.get_channel(841665459531415562)
        emoji = self.bot.get_emoji(id=880240953691082792)
        emoji2 = self.bot.get_emoji(id=930261475036131399)
        image = ""
        boosterrole = guild.get_role(925898132007563404).mention
        vipchat = guild.get_channel(930265775812534292).mention
        vipvc = guild.get_channel(930268986858414130).mention

        '''part = "> Passively gain server currency\n\n> Your own custom role\n\n> The booster role being hoisted " \
               "higher, just under the staff, showing your passion for the server"'''

        '''partner = discord.Embed(color=discord.Color.green())
        partner.add_field(name="What do you get for boosting us? This is what rewards you can get:", value=part, inline=False)
        partner.set_thumbnail(url=guild.icon_url)
        partner.set_footer(text=f"Revised on: {datetime.date.today()}")'''

        oboost = f"> {boosterrole} which is hoisted above other roles\n> Access to {vipchat} with the other boosters!\n> Access to {vipvc} with other boosters!"
        tboost = f"> Custom role with custom color (cannot be replicating a staff role and must be SFW)\n"

        partner = discord.Embed(title="Our Boosting Perks!", color=discord.Color.purple())
        partner.add_field(name="One Boost!", value=f"What do you get for boosting once? They are below:\n{oboost}")

        partner1 = discord.Embed(color=discord.Color.purple())
        partner1.add_field(name="Two Boosts!", value=f"What do you get for boosting twice? They are below:\n{tboost}")

        # await self.bot.get_guild(913007198488133632).get_channel(919639089832149002).purge(limit=10)
        # await self.bot.get_guild(913007198488133632).get_channel(919639089832149002).send(f"{emoji} Booster Perks! {emoji}", embed=partner)
        # await self.bot.get_guild(913007198488133632).get_channel(919639089832149002).send("And more perks to come!")
        await ctx.send(embed=partner)
        await ctx.send(embed=partner1)

        await ctx.send("Sent the Booster Perks")


def setup(bot):
    bot.add_cog(OwnerCog(bot))