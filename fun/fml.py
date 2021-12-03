import random
import discord
import datetime
from discord.ext import commands
from config import _blnk_value

aliases = ['FML', 'Fml']


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=f"Selects a random fml from [here](https://www.fmylife.com/random). Please message the developer if there's any that you wish to be added which hasn't been added from that site as there's still plenty more that can be used")
    async def fml(self, ctx):
        responses = ['https://www.fmylife.com/article/today-my-mum-found-out-she-s-pregnant-i-would-be-happy-for-her-if-she-knew-who-the-father-was-fm_143163.html',
                     # Today, my mum found out she's pregnant. I would be happy for her, if she knew who the father was. FML

                     ]
        response = random.choice(responses)
        color = discord.Color.dark_red()
        msg = ctx
        guild = msg.guild

        quote = discord.Embed(color=color, name="FML", timestamp=datetime.datetime.utcnow())
        quote.add_field(name="FML", value=f"[Link to fml]({response})")
        quote.set_image(url=response)
        # quote.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        # quote.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.send(embed=quote)

        # await ctx.send(f'> Quote:\n')
        # await ctx.send(f'{random.choice(responses)}')


def setup(client):
    client.add_cog(Fun(client))
