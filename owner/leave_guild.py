import discord
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def gleave(self, ctx, guild_id):
        guild = discord.utils.get(self.client.guilds, name=guild_id)
        if guild is None:
            await ctx.send("I don't recognize that guild.")
            return
        await self.client.leave_guild(guild)
        await ctx.send(f":ok_hand: Left guild: {guild.name} ({guild.id})")
        print(guild_id)


def setup(client):
    client.add_cog(Owner(client))
