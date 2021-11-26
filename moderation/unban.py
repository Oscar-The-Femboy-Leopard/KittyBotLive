import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.Cog.listener()
    async def on_ready(self):
            print('Moderation is ready')'''

    # @commands.has_guild_permissions(discord.Member.ban(self,**kwargs))
    @commands.command(aliases=['unban user'],
                      description="This will unban a user from the server!\nUsage:")
    async def unban(self, ctx, *, reason=None):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = discord.member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


def setup(client):
    client.add_cog(Moderation(client))
