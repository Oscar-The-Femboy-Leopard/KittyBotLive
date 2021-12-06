import ast
import discord
import datetime

from discord.ext import commands
from config import _blnk_value, Owner_ID


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

    @commands.command(name='openpartner', alias="OpenPartner", hidden=True)
    @commands.is_owner()
    async def open(self, ctx):

        guild = self.bot.get_guild(913007198488133632)
        channel = self.bot.get_channel(841665459531415562)

        part = "> Must comply with Discord [TOS](https://discord.com/terms) and [Guidelines](" \
               "https://discord.com/guidelines)\n\n> If there is any NSFW content, there must be an appropriate NSFW " \
               "verification for it\n\n> Nice staff and community, no one likes toxicity.\n\n> No minimum member " \
               "requirements, but the server needs to be relitively active.\n\n> Needs to have a good verification " \
               "behind it to deter trolls and other unwelcome types from the server.\n\n\n**PLEASE NOTE:**\nThese are " \
               "subject to change, and if you don't meet the requirements, the staff can terminate the " \
               "partnership/affiliation. Updates will be sent to the Partner Announcements beforehand."

        img = 'https://media.discordapp.net/attachments/880852778124206180/913775775105302568/Partner_Requirements.gif'

        img_ = discord.Embed(color=discord.Color.green())
        img_.set_image(url=img)

        partner = discord.Embed(color=discord.Color.green())
        partner.add_field(name="We are open for partnerships! Below are the requirements", value=part, inline=False)
        partner.set_thumbnail(url=guild.icon_url)
        partner.set_footer(text=f"Revised on: {datetime.date.today()}")

        await self.bot.get_guild(913007198488133632).get_channel(913038686969548810).purge(limit=10)
        await self.bot.get_guild(913007198488133632).get_channel(913038686969548810).send(embed=img_)
        await self.bot.get_guild(913007198488133632).get_channel(913038686969548810).send(embed=partner)
        await ctx.send("Sent that partnerships are open along with the requirements.")

    '''@commands.command(name='closedpartner', alias="ClosedPartner", hidden=True)
    @commands.is_owner()
    async def closed(self, ctx):

        guild = self.client.get_guild(841496169556475975)
        channel = self.client.get_channel(841665459531415562)

        partner = discord.Embed(color=discord.Color.dark_red(),
                                description="We are currently closed for partnerships. Keep an eye on this channel to find out when they open back up.")
        partner.add_field(name="Even though your partnerships are currently closed to new partners, is there a way I "
                               "can still partner?",
                          value=f"Yes, you can still partner with us, just reach out to {Owner_ID.mention} and she will "
                                f"give a definitive answer.", inline=False)
        partner.set_thumbnail(url=guild.icon_url)
        partner.set_footer(text=f"Revised on: {datetime.date.today()}")

        await self.client.get_guild(841496169556475975).get_channel(841665459531415562).purge(limit=10)
        await self.client.get_guild(841496169556475975).get_channel(841665459531415562).send(embed=partner)
        await ctx.send("Sent that partnerships are closed.")'''


def setup(bot):
    bot.add_cog(OwnerCog(bot))
