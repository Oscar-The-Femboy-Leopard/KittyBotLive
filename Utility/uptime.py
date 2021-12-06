import discord
import datetime
import time

from discord.ext import commands
from config import start_time


aliases = ["runtime", "Bot_runtime", "awaketime"]
description = "This will give the uptime of the client since the initial run of the code. The number format is in Hours, Minutes and Seconds."


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        msg = ctx
        guild = msg.guild

        embed = discord.Embed(colour=ctx.message.author.top_role.colour, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)


def setup(client):
    client.add_cog(Utility(client))
