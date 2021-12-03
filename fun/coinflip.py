import os
import random
import discord
import datetime

from discord.ext import commands


aliases = ['cflip', 'coinf']
description = "Flip a coin and it will land on either Heads or Tails!"


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def coinflip(self, ctx):

        coinsides = ['Heads', 'Tails']
        result = random.choice(coinsides)
        if result == 'Heads':
            coin = os.listdir('./heads')
            sendingcoin = random.choice(coin)
            sentcoin = file=discord.File('./heads' + sendingcoin)

            await ctx.send(f"{ctx.author.display_name} flipped a coin! It landed on Heads!",
                           file=discord.File('./heads/' + sendingcoin))

        if result == 'Tails':
            coin = os.listdir('./tails')
            sendingcoin = random.choice(coin)

            await ctx.send(f"{ctx.author.display_name} flipped a coin! It landed on Heads!",
                           file=discord.File('./tails/' + sendingcoin))

        color = discord.Color.blue()
        msg = ctx
        guild = msg.guild

        _flip = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        _flip.add_field(name=f"{ctx.author.display_name} flipped a coin!", value="Result:", inline=False)
        _flip.set_image(url=f"{coin} + {sendingcoin}")
        _flip.set_footer(text=f"{msg.author}")

        # await msg.send(embed=_flip)

    @coinflip.error()
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the side of the coin you would like to use.')


def setup(client):
    client.add_cog(Fun(client))
