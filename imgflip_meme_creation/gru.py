import datetime

import requests
import json
import discord
import random
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username


class ImgFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Gru'],
                      description="Write 4 things on Gru's board")
    async def gru(self, ctx, *, message):
        content = ctx
        id = '131940431'

        vari = message.split('.')
        # ctx1, ctx2, ctx3, ctx4 = ctx.split('.')
        url = f"https://api.imgflip.com/caption_image?text0={vari[0]}&text1={vari[1]}&text2={vari[2]}&text3={vari[3]}&username={imgflip_username}&password={imgflip_password}&template_id={id} "
        print(vari)
# TODO Make this command work
        payload = {}
        headers = {
            'Cookie': '__cfduid=de5b6cba36f7140e0ab1a42da298d3e4b1605580276'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        url = data["data"]["url"]
        color = random.choice(random_color)
        # guild = message.guild
        msg = ctx
        guild = msg.guild

        rm_url = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.channel.send(embed=rm_url)


def setup(client):
    client.add_cog(ImgFlip(client))
