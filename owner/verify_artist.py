import ast
import asyncio
import datetime
import random
import discord
import os

from discord.ext import commands
from config import Owner_ID, random_color


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
        self.guild = None
        self.author = Owner_ID
        self.bot = bot

    @commands.command(name='verify_artist', alias="VA", hidden=True)
    @commands.is_owner()
    async def verifiedartist(self, ctx):

        guild = 841496169556475975
        channel = 880919061163302942

        staff_role = self.bot.get_guild(guild).get_role(841497322138632222).mention
        verified_artist_role = self.bot.get_guild(guild).get_role(855406836463173653).mention

        color = random.choice(random_color)

        _guild = self.bot.get_guild(guild)

        img = "https://media.discordapp.net/attachments/880852778124206180/880959182822588456/Verified_Artist.png"

        impInfo = f"Verifying isn't that difficult! Please just DM your Twitter, Furaffinity and/or Deviantart to any " \
                  f"staff member or create create a ticket if you desire that instead.\n\nWhat do you get for " \
                  f"verifying that you are an actual artist, you might ask? Well, people would know you are an artist " \
                  f"and may actually go to you for commissions over unverified artists. A cool role only obtainable " \
                  f"by verifying, {verified_artist_role}, and access to a private chat with other verified artists " \
                  f"and staff for all of the possible enquires you may want to make. "

        image = discord.Embed(timestamp=datetime.datetime.utcnow(), color=color)
        image.set_image(url=img)

        imp = discord.Embed(color=random.choice(random_color))
        imp.add_field(name="Verifying that you're an artist", value=impInfo, inline=False)
        imp.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)

        revised = discord.Embed(color=random.choice(random_color), timestamp=datetime.datetime.utcnow())
        revised.add_field(name=f"The rules for verifying was updated by:",
                          value=f"{_guild.name}'s {staff_role} on:\n\n{datetime.date.today()}")

        await self.bot.get_guild(guild).get_channel(channel).purge(limit=10)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=image)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=imp)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=revised)
        await ctx.send("Sent the Verified Art Rules.")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
