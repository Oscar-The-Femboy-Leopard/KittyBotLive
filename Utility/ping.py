import datetime
import discord

from discord.ext import commands


aliases = ['Latency', 'latency']
description = "Use this command to check the bot's latency!"


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        # avlatency = round(self.bot.average_latency * 1000)
        msg = ctx
        guild = msg.guild
        latency = int(latency)
        # avlatency = int(avlatency)

        if latency <= 25:
            latency = f"`{latency}ms`"
            color = discord.Color.dark_green()
            emoji = ':green_circle:'
            foot = f"My heartbeat is fast and strong!"

        elif latency <= 75:
            latency = f"`{latency}ms`"
            color = discord.Color.green()
            emoji = ':green_circle:'
            foot = f"My heartbeat is fast and good!"

        elif latency <= 150:
            latency = f"`{latency}ms`"
            color = discord.Color.from_rgb(255, 191, 0)
            emoji = ':yellow_circle:'
            foot = f"My heartbeat is mediocre...."

        else:
            latency = f"`{latency}ms`"
            color = discord.Color.dark_red()
            emoji = ':red_circle:'
            foot = f"My heartbeat is slow and weak...."

        _ping = discord.Embed(color=color, timestamp=datetime.datetime.utcnow(), description=f"My ping is:")
        _ping.add_field(name=f"{latency}", value=emoji, inline=True)
        # _ping.add_field(name="Average Latency:", value=f"{avlatency}ms", inline=True)
        _ping.set_footer(text=f'{foot}')

        await ctx.reply(embed=_ping)


def setup(bot):
    bot.add_cog(Utility(bot))
