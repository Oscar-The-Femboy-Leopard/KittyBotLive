import discord
import random

from discord.ext import commands
from config import random_color


class ChannelMessage(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def cmessage(self, ctx, cID: int, *, message):
        channel = self.client.get_channel(cID)

        msg = message.split('.', 1)

        # await channel.send(msg)

        embed = discord.Embed(color=random.choice(random_color), title="A message")
        embed.add_field(name="What it is about:", value=msg[0], inline=False)
        embed.add_field(name="Message:", value=msg[1], inline=False)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await channel.send(embed=embed)

        await ctx.reply("sent!")


def setup(client):
    client.add_cog(ChannelMessage(client))