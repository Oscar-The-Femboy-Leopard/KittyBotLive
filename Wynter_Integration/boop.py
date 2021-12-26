import http.client
import mimetypes
import json
import discord
import random
import datetime

from discord.ext import commands
from config import random_color


aliases = ['Boop', 'BOOP']
description = "This command uses Wynter's API, made by Darkmane Arweinydd#0069, to boop people!"


class Wholesome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def boop(self, ctx, b: commands.Greedy[discord.Member]):

        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
            'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/boop/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        url = data["result"]["imgUrl"]
        color = random.choice(random_color)
        guild = ctx.guild
        msg = ctx

        limit = 3
        boop = ""

        if len(b) > 1 <= limit:
            for u in b:
                boop = boop + f" and {u.display_name}"  # + u.display_name
            boop = boop[4:]

        if len(b) == 1:
            for u in b:
                _hug = u.display_name

        if len(b) > limit:
            return await ctx.reply(f"I can only go to my limit of {limit}")

        auth = msg.author.display_name
        choice = [f"***{auth}** booped **{boop}***",
                  f"***{auth}** unloaded an automatic barrage of boops upon **{boop}***",
                  f"***{boop}** couldn't avoid the boop barrage from **{auth}***",
                  f"***{auth}** sneaks up upon **{boop}** and then boops them before darting off*",
                  f"***{auth}** has just booped **{boop}** outta nowhere!*"]
        boopmessage = random.choice(choice)

        e_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        e_url.add_field(name=boopmessage, value=f":frame_photo: [Link to image]({url})", inline=False)
        e_url.set_image(url=url)
        e_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await msg.channel.send(embed=e_url)


def setup(bot):
    bot.add_cog(Wholesome(bot))
