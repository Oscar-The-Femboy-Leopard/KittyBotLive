import http.client
import mimetypes
import json
import discord
import random
import datetime

from discord.ext import commands
from config import random_color

aliases = ['huggles', 'Hugs', 'Huggles']
description = "This command uses Wynter's API, made by Darkmane Arweinydd#0069, to hug people!"


class Wholesome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    # async def hug(self, ctx, m: commands.Greedy[discord.Member]):
    async def hug(self, ctx, *, m: discord.Member):

        conn = http.bot.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
            'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/hug/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        url = data["result"]["imgUrl"]
        color = random.choice(random_color)
        guild = ctx.guild
        msg = ctx
        # hugged = discord.Member
        _ment_hug = m.display_name
        # _ment_hug = ", ".join(m)
        auth = msg.author.display_name

        '''if hugged and huggled:
            hug = [
                f"**{auth}** hugged **{_ment_hug}** and **{ment_hug}**",
                f"When **{_ment_hug}** and **{ment_hug}** wasn't looking, **{auth}** sneak hugs them"
            ]'''

        # else:
        hug = [
            f"***{auth}** hugged **{_ment_hug}***",
            f"***{auth}** sneaks up on **{_ment_hug}** before giving them bear hugs*",
            f"*When **{_ment_hug}** isn't looking, **{auth}** just hugs them tightly*",
            f"***{auth}** hugs **{_ment_hug}** from behind*"
        ]
        hugmessage = random.choice(hug)

        e_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        e_url.add_field(name=hugmessage, value=f":frame_photo: [Link to image]({url})", inline=False)
        e_url.set_image(url=url)
        e_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        if auth == _ment_hug:
            return await msg.channel.send(f"You cannot hug yourself, {auth}, so I'll hug you! *hugs tightly*")
        else:
            return await msg.channel.send(embed=e_url)


def setup(bot):
    bot.add_cog(Wholesome(bot))
