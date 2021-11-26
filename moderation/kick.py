import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.Cog.listener()
    async def on_ready(self):
            print('Moderation is ready')'''

    # @commands.has_guild_permissions(discord.Member.ban(self,**kwargs))
    @commands.command(aliases=['kick user'],
                      description="This will kick a user from the server!\nUsage:")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')


def setup(client):
    client.add_cog(Moderation(client))
