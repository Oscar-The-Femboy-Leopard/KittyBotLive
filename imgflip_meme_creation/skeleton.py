import requests
import json
import discord
import datetime
import random
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username


aliases = ["Skeleton", "waiting_skeleton"]
description = "Put some text with a skeleton in the park!"


class ImgFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def skeleton(self, ctx, *, message):
        content = ctx
        # ctx = content
        id = '4087833'
        url = f"https://api.imgflip.com/caption_image?text0={message}&username={imgflip_username}&password={imgflip_password}&template_id={id}"

        payload = {}
        headers = {
            'Cookie': '__cfduid=d8877b9d3f7f03d74d494201c69a043e81605576645; claim_key=eVrjsNJKFzqzCYRCMTSxdpSh5BnGPLdV'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        url = data["data"]["url"]
        color = random.choice(random_color)
        # guild = message.guild
        msg = ctx
        guild = msg.guild

        rm_url = discord.Embed(color=color, title="Waiting Skeleton", timestamp=datetime.datetime.utcnow())
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.channel.send(embed=rm_url)


def setup(client):
    client.add_cog(ImgFlip(client))
