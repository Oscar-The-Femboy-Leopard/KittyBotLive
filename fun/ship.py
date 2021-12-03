import datetime
import random
import discord
from discord.ext import commands
from config import _blnk_value

aliases = ['Ship', 'SHIP']
description = "Run this command to see the ship score between you and someone else!"


class Fun(commands.Cog):
    def __init__(self, client):  # init the class so it's ready to be used

        self.client = client  # defines the command as part of the bot and makes it callable at the bottom to load the command

    @commands.command(aliases=aliases, description=description)
    async def ship(self, ctx, *, member: discord.Member = None):  # passes through context, and defines Member to be called below

        '''author = message.author  # makes author callable
        await ctx.send(f'{author} ships {member} and {member}') # Basically saying that the Author ships the 2 peeps they mention
        await ctx.send(f'The score is:', random.randint(0, 100)) # calls a random number from RanInts that's 0-100'''
        auth = ctx.author.display_name
        '''shipped, shipped1 = ctx.author.message.split(',')
        shipped = member.display_name
        shipped1 = member.display_name'''

        shipped = member.display_name
        shipped1 = member.display_name

        '''_shipped, __shipped = ctx.author.message.split(',')
        _shipped = shipped
        __shipped = shipped1'''

        '''_shipped = member.display_name
        _shipped1 = member.display_name'''
        score = random.randint(0, 100)
        val = f"This command runs off random integers. It is not made to be serious."

        if score <= 10:
            reply = f"There's no hope here at all. Better off moving on."
            color = discord.Color.from_rgb(101, 28, 50)
        elif score <= 25:
            reply = f"The score is too low. Maybe you could be something in the future?"
            color = discord.Color.red()
        elif score <= 50:
            reply = f"Looks like you're good friends"
            color = discord.Color.magenta()
        elif score <= 75:
            reply = f"Pretty high score. Great friends maybe?"
            color = discord.Color.green()
        elif score <= 90:
            reply = f"Great friends!"
            color = discord.Color.dark_green()
        elif score > 90:
            reply = "Give it a shot. They're meant to be your lover!"
            color = discord.Color.gold()

        if auth == shipped:
            return await ctx.send(f"You cannot ship yourself, {auth}. It just doesn't make sense to do it.")

        else:
            shipname = f"{auth} ships {shipped}"
            # shipname = f"{auth} ships {shipped} and {shipped1}"
            shipvalue = f"The score is: {score}"
            ship = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
            ship.add_field(name=shipname, value=shipvalue, inline=False)
            ship.add_field(name=reply, value=_blnk_value, inline=False)
            ship.set_footer(text=val)
            return await ctx.send(embed=ship)


def setup(client):
    client.add_cog(Fun(client))
