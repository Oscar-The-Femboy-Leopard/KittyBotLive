import datetime
import discord

from discord.ext import commands


aliases = ["whois", "userinfo"]
description = "Find out a member's information within the server."


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def personinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        uID = member.id

        # online = "🟢"
        # dnd = "🔴"
        # offline = "⚫"
        # idol = "🟡"

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=ctx.message.author.top_role.colour, timestamp=datetime.datetime.utcnow(),
                              title=f"User Info -\n {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author} | uID:{ctx.author.id}")

        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=False)
        embed.add_field(name="Server Name:", value=member.mention, inline=False)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name="Roles:", value="_ _".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        # embed.add_field(name="Permissions", value=f"_ _".join([role.permissions for role in roles]), inline=False)
        # embed.add_field(name="Permissions", value=f"{[role.permissions for role in roles]}", inline=False)
        # embed.add_field(name="Key Permissions", value=member.guild_permissions, inline=False)

        if member.status.name == "offline":
            # emoji = offline
            emoji = "⚫"
        elif member.status.name == "online":
            # emoji = online
            emoji = "🟢"
        elif member.status.name == "dnd":
            # emoji = dnd
            emoji = "🔴"
        elif member.status.name == 'idol':
            # emoji = idol
            emoji = "🟡"

        embed.add_field(name="Status:", value=f"{emoji}" + member.status.name, inline=False)
        # embed.add_field(name="User Status:", value=member._state, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
