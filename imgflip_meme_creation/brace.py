import requests
import json
import discord
import random
import datetime

from discord.ext import commands
from config import random_color, imgflip_password, imgflip_username, bad_list


aliases = ['brace_x_is_coming!']
description = "Make a meme about having to brace for something!"


class ImgFlip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def brace(self, ctx, message):
        id = '61546'
        url = f"https://api.imgflip.com/caption_image?text0=Brace yourselves, {message} is coming&username={imgflip_username}&password={imgflip_password}&template_id={id}"

        payload = {}
        headers = {
            'Cookie': '__cfduid=d8877b9d3f7f03d74d494201c69a043e81605576645; claim_key=eVrjsNJKFzqzCYRCMTSxdpSh5BnGPLdV'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        url = data["data"]["url"]
        color = random.choice(random_color)
        msg = ctx
        guild = msg.guild

        rm_url = discord.Embed(color=color, title="Brace", timestamp=datetime.datetime.utcnow())
        rm_url.set_image(url=url)
        rm_url.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        # await ctx.channel.send(embed=rm_url)

        for bad_word in bad_list:
            if bad_word in message.content:
                return await ctx.reply("Sorry, but I am unable to complete this command due to blacklisted word.")
            else:
                await ctx.send(embed=rm_url)

        '''for bad_word in bad_list:
            if bad_word in message.content:
                await ctx.send("Sorry... I cannot do this request. Please don't restricted words. Thank you.")

        else:
            await ctx.channel.send(embed=rm_url)'''


def setup(bot):
    bot.add_cog(ImgFlip(bot))
