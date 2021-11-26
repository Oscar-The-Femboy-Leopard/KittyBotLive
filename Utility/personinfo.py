import datetime
import discord

from discord.ext import commands
from config import _blnk_value

aliases = ["whois", "userinfo"]
description = "Find out a member's information within the server."


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases, description=description)
    async def personinfo(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=ctx.message.author.top_role.colour, timestamp=datetime.datetime.utcnow(),
                              title=f"User Info -\n {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}|USD:{ctx.author.id}")

        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=False)
        embed.add_field(name="Server Name:", value=member.mention, inline=False)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name="Roles:", value=_blnk_value.join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        embed.add_field(name="Permissions", value=_blnk_value.join([role.permissions for role in roles]), inline=False)
        # embed.add_field(name="Key Permissions", value=member.guild_permissions, inline=False)

        # embed.add_field(name="Status:", value=member.desktop_status, inline=False)
        # embed.add_field(name="User Status:", value=member._state, inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Utility(client))
