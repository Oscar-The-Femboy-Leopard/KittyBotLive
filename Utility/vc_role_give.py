import discord

from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, m: discord.Member, before, after):
        role = discord.utils.get(after.guild.roles, name="VC")
