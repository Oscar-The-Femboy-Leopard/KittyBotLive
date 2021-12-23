import requests
import json
import discord
import random
import datetime
from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username


aliases = ['sta', 'saythatagain', 's_t_a']
description = "A meme with Samual L Jackson 'Say That Again I Dare You'."


class ImgFlip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def say_that_again(self, ctx, *, message):
        message, message2 = message.split('.')

        id = '124212'
        url = f"https://api.imgflip.com/caption_image?text0={message}&text1={message2}&username={imgflip_username}&password={imgflip_password}&template_id={id}"
        payload = {}
        headers = {
            'Cookie': '__cfduid=d8877b9d3f7f03d74d494201c69a043e81605576645; claim_key=eVrjsNJKFzqzCYRCMTSxdpSh5BnGPLdV'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        url = data["data"]["url"]

        color = random.choice(random_color)
        guild = ctx.guild

        rm_url = discord.Embed(color=color, title="Say That Again I Dare You", timestamp=datetime.datetime.utcnow())
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.channel.send(embed=rm_url)


def setup(bot):
    bot.add_cog(ImgFlip(bot))
