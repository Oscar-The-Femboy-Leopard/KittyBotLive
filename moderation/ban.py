import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.Cog.listener()
    async def on_ready(self):
            print('Moderation is ready')'''

    # @commands.has_guild_permissions(discord.Member.ban(self,**kwargs))
    @commands.command(aliases=['ban user'],
                      description="This bans a user!\n Usage:")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


def setup(client):
    client.add_cog(Moderation(client))
