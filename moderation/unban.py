import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''@commands.Cog.listener()
    async def on_ready(self):
            print('Moderation is ready')'''

    # @commands.has_guild_permissions(discord.Member.ban(self,**kwargs))
    @commands.command(aliases=['unban user'], description="This will unban a user from the server!\nUsage:")
    async def unban(self, ctx):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = discord.Member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')


def setup(bot):
    bot.add_cog(Moderation(bot))
