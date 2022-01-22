import discord
import random

from discord.ext import commands
from config import random_color


class ChannelMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmessage(self, ctx, cID: int, *, message):
        owner = [
            895656099376681011,
            670932463077556224,
        ]

        if ctx.author.id not in owner:
            return

        channel = self.bot.get_channel(cID)

        msg = message.split('.', 2)

        # await channel.send(msg)
        color = random.choice(random_color)

        if msg[0] == 'embed':

            embed = discord.Embed(color=color, title="A message")
            embed.add_field(name="What it is about:", value=msg[0], inline=False)
            embed.add_field(name="Message:", value=msg[1], inline=False)
            embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

            await channel.send(embed=embed)

            await ctx.reply("sent!")

            # editmsg = self.bot.get_message(mID)

            n = discord.Embed(color=color, title="A message")
        if msg[0] != 'embed':
            await channel.send(msg[1], "\n", msg[2])

    @commands.command()
    @commands.is_owner()
    async def editmsg(self, ctx, mID: int, *, message):
        msg = await ctx.fetch_message(mID)

        _msg = message.split('.', 1)

        c = random.choice(random_color)

        e = discord.Embed(color=c)
        e.add_field(name="What it is about:", value=_msg[0], inline=False)
        e.add_field(name="Message:", value=_msg[1], inline=False)
        e.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

        await msg.edit(content="", embed=e)
        await msg.reply("Edited message!")


def setup(bot):
    bot.add_cog(ChannelMessage(bot))