import requests
import json
import discord
import random
import datetime
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username


aliases = ['Nut', "Blank_Nut_Button", 'blank_nut_button', 'blanknutbutton', "button", "Button"]
description = "Blank nut button meme!"


class ImgFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def nut(self, ctx, *, message):
        content = ctx
        message, message2 = message.split('.')
        id = '119139145'
        # url = f"https://api.imgflip.com/caption_image?text0=Not adding commands to Club Bot&text1=Adding commands to Club Bot&username={imgflip_username}&password={imgflip_password}&template_id={id}"
        url = f"https://api.imgflip.com/caption_image?text0={message}&text1={message2}&username={imgflip_username}&password={imgflip_password}&template_id={id}"
        payload = {}
        headers = {
            'Cookie': '__cfduid=d8877b9d3f7f03d74d494201c69a043e81605576645; claim_key=eVrjsNJKFzqzCYRCMTSxdpSh5BnGPLdV'
        }
        # content1 = f"{message}"
        # content2 = f'{}'
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        url = data["data"]["url"]
        color = random.choice(random_color)
        guild = ctx.guild
        # msg = message

        rm_url = discord.Embed(color=color, title="Blank Button", timestamp=datetime.datetime.utcnow())
        # rm_url.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        # await msg.channel.send(f"***{msg.author}*** hugged ***{msg.mentions}***")
        await ctx.channel.send(embed=rm_url)


def setup(client):
    client.add_cog(ImgFlip(client))
