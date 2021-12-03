import random
import discord
from discord.ext import commands
from config import _8ball_responses

aliases = ['8ball', 'eightball', 'eight ball', "8"]
description = "Runs the 8ball command. Ask the 8ball any question and it'd answer, just like if it was a real 8ball!"


class Fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=aliases,
                      description=description)
    async def _8ball(self, ctx, *, question):
        question = question
        response = random.choice(_8ball_responses)
        color = discord.Color.dark_red()
        msg = ctx
        guild = msg.guild
        thumb = f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.ebayimg.com%2Fimages%2Fg%2FATUAAOSw8hpdwj5V%2Fs-l300.jpg&f=1&nofb=1"

        _8 = discord.Embed(color=color, timestamp=discord.Message.created_at)
        _8.add_field(name="The question asked:", value=question, inline=False)
        _8.add_field(name="My Response:", value=response, inline=False)
        _8.set_thumbnail(url=thumb)
        _8.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.send(embed=_8)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Missing argument. Can you please provide a question for the 8ball?')


def setup(client):
    client.add_cog(Fun(client))
