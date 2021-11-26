import requests
import json
import discord
import datetime
import random
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username, bad_list

aliases = ['distractedbf', 'distracted_bf', 'jealousgirlfriend', "jealous_girlfriend"]
description = "Make a meme about having to brace for something!"


class ImgFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def bf(self, ctx, *, message):
        content = ctx
        # ctx = content
        id = '112126428'
        vari = message.split('.')
        # ctx1, ctx2, ctx3, ctx4 = ctx.split('.')
        url = f"https://api.imgflip.com/caption_image?text0={vari[0]}&text1={vari[1]}&text2={vari[2]}&username={imgflip_username}&password={imgflip_password}&template_id={id} "
        print(vari)

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

        if message.content in bad_list:
            await ctx.send("A blacklisted word/praise is used. Please check what word(s) you can't use in Rules.")

        else:

            rm_url = discord.Embed(color=color, title="Distracted BF", timestamp=datetime.datetime.utcnow())
            rm_url.set_image(url=url)
            rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

            await ctx.channel.send(embed=rm_url)

        '''for bad_word in bad_list:
            if bad_word in message.content:
                await ctx.send("Sorry... I cannot do this request. Please don't restricted words. Thank you.")

        else:
            await ctx.channel.send(embed=rm_url)'''


def setup(client):
    client.add_cog(ImgFlip(client))
