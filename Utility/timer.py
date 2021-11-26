import asyncio
from discord.ext import commands
from config import PREFIX

aliases = ["Timer", "countdown", "Countdown"]
description = f"This command will let you set a timer for anything! The timer will edit the message for you to see a live countdown of the time left until it has ended. It will then ping you to let you know that it has ended! This command does have a cooldown."


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def timer(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 300:
                await ctx.send("I don't think im allowed to do go above 300 seconds. Can you choose a number that's 300 seconds or less, please?")
                raise BaseException
            if secondint <= 0:
                await ctx.send("I don't think im allowed to do negatives. Can you choose a number that's positive, please?")
                raise BaseException
            message = await ctx.send("Timer: {seconds}")
            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="Ended!")
                    break
                await message.edit(content=f"Timer: {secondint}s")
                await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention} Your countdown Has ended!")
        except ValueError:
            await ctx.send("Must be a number!")


def setup(client):
    client.add_cog(Utility(client))
