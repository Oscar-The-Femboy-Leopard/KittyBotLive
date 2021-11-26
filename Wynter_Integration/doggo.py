import http.client
import mimetypes
import json
import discord
import random
import datetime
from discord.ext import commands
from config import random_color, _blnk_value

aliases = ['dog', 'doggie', 'Dog', 'Doggie', 'puppy', 'Puppy']
description = "This command uses Wynter's API, made by Darkmane Arweinydd#0069, to show doggos!"


class Wholesome(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def doggo(self, message, *, ctx):
        """Just use for a cute doggo!"""

        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
            'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/dog/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        url = data["result"]["imgUrl"]
        color = random.choice(random_color)
        guild = message.guild
        msg = message
        auth = msg.author.display_name
        _val = f"A doggo for: {auth}"
        val = f":frame_photo: [Link to image]({url})"

        e_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow(), description=f"{_val}")
        e_url.add_field(name=f"{val}", value=_blnk_value, inline=True)
        e_url.set_image(url=url)
        e_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await msg.channel.send(embed=e_url)


def setup(client):
    client.add_cog(Wholesome(client))
