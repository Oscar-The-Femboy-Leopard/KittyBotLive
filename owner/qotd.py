import ast
import discord
import threading
import datetime
import tracemalloc
from discord.ext import commands, tasks
from config import Owner_ID


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.author = Owner_ID
        self.bot = bot

    '''@commands.command(name='qotd', alias="QOTD", hidden=True)
    @commands.is_owner()'''
    @tasks.loop(minutes=1)
    async def checkTime(self, ctx):
        # threading.Timer(1, self.checkTime).start()

        now = datetime.datetime.now()
        # _channel = self.client.get_channel(775770598844137482)
        _guild = self.bot.get_guild(488623700539736064)
        _channel = _guild.get_channel(775770598844137482)

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)

        if current_time == '12:42:00':
            print('sending message')
            await _channel.send("Test")
            await self.bot.get_channel(self, 775770598844137482).send("Hello")

    # checkTime()


def setup(bot):
    bot.add_cog(OwnerCog(bot))
