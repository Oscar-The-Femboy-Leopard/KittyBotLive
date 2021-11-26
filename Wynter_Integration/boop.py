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

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def boop(self, message, *, booped: discord.Member = None):

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
        guild = message.guild
        msg = message
        _ment_boop = booped.display_name
        auth = msg.author.display_name
        choice = [f"***{auth}** booped **{_ment_boop}***",
                  f"***{auth}** unloaded an automatic barrage of boops upon **{_ment_boop}***",
                  f"***{_ment_boop}** couldn't avoid the boop barrage from **{auth}***",
                  f"***{auth}** sneaks up upon **{_ment_boop}** and then boops them before darting off*",
                  f"***{auth}** has just booped **{_ment_boop}** outta nowhere!*"]
        boopmessage = random.choice(choice)

        e_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        e_url.add_field(name=boopmessage, value=f":frame_photo: [Link to image]({url})", inline=False)
        e_url.set_image(url=url)
        e_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await msg.channel.send(embed=e_url)


def setup(client):
    client.add_cog(Wholesome(client))
