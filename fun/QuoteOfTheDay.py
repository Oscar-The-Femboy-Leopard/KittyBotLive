import asyncio
from datetime import datetime
from discord.ext import commands

alarm_time = '12:55'  # 24hrs
channel_id = 775770598844137482


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def time_check(self, client):
        await client.wait_until_ready()
        while not client.is_closed:
            now = datetime.strftime(datetime.now(), '%H:%M')
            channel = client.get_channel(channel_id)
            messages = ('Test')
            if now == alarm_time:
                await client.send_message(channel, messages)
                time = 90
            else:
                time = 1
                await asyncio.sleep(time)

        client.loop.create_task(self.time_check())


def setup(client):
    client.add_cog(Fun(client))
