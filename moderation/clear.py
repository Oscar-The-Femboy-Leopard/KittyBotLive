import asyncio
import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''@commands.Cog.listener()
    async def on_ready(self):
            print('Moderation is ready')'''

    # @commands.has_guild_permissions(discord.Member.ban(self,**kwargs))
    @commands.command(aliases=['purge', 'nom'],
                      hidden=True,
                      description="This will purge a channel of the messages! The default amount of messages are 10 but you can manually add that by adding a number after the command.\nUsage:")
    @commands.has_permissions()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Nomed {amount} of messages :stuck_out_tongue:')
        await asyncio.sleep(5)  # Change the number for the amount of time for the message above to stay there
        await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(Moderation(bot))
