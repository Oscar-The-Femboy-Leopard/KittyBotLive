import asyncio
from datetime import datetime
from discord.ext import commands

alarm_time = '12:55'  # 24hrs
channel_id = 775770598844137482


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def time_check(self, bot):
        await bot.wait_until_ready()
        while not bot.is_closed:
            now = datetime.strftime(datetime.now(), '%H:%M')
            channel = bot.get_channel(channel_id)
            messages = ('Test')
            if now == alarm_time:
                await bot.send_message(channel, messages)
                time = 90
            else:
                time = 1
                await asyncio.sleep(time)

        bot.loop.create_task(self.time_check())


def setup(bot):
    bot.add_cog(Fun(bot))
