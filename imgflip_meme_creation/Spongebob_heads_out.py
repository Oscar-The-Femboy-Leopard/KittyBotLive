import requests
import json
import discord
import datetime
import random
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username


aliases = ["alrightI'mout", "alright_I'm_out"]
description = "Make Spongebob say he's heading out because of something!"


class ImgFlip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases,
                      description=description)
    async def im_out(self, ctx, *, message):
        content = ctx
        # ctx = content
        id = '196652226'
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

        rm_url = discord.Embed(color=color, title="SpoungeBob Heads Out", timestamp=datetime.datetime.utcnow())
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.channel.send(embed=rm_url)


def setup(bot):
    bot.add_cog(ImgFlip(bot))
