import discord
import datetime

from discord.ext import commands
from discord.ext.commands import Greedy


baliases = ['Ban', 'Ban_member', 'Ban_Member']
bdescription = "This command is self explanitory. It bans members from the server."




ban_appeal = "https://forms.gle/rmQEkwXTt43pWDAa8"


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=baliases, description=bdescription)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, uID: int, *, reason=None):
        channel = self.bot.get_channel(922596086848323634)

        if uID is None:
            return await ctx.reply("You need someone to ban.")
        if ctx.author.id == uID:
            return await ctx.reply("You cannot ban yourself!")
        if reason is None:
            return await ctx.reply("We need a reason for this ban.")

        if uID in ctx.guild.members:
            m = (self.bot.get_user(uID))

            message = f"You have been banned from {ctx.guild} for {reason}.\n\nYou can appeal the ban [here]({ban_appeal})"

            banned = discord.Embed(color=discord.Color.green())
            banned.add_field(name="You're Banned!", value=message, inline=False)
            banned.add_field(name="Date Of Ban:", value=f'{datetime.date.today()}', inline=False)

            await m.send(embed=banned)

            await ctx.guild.ban(discord.Object(id=uID), reason=reason)

            ban = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
            ban.add_field(name="Member Banned!", value=m.mention, inline=False)
            ban.add_field(name="Member Affected:", value=m.display_name + "#" + m.discriminator, inline=False)
            ban.add_field(name="Member's ID:", value=m.id, inline=False)
            ban.add_field(name="Reason Given:", value=reason, inline=False)
            ban.add_field(name="Staff Member Responsible:",
                          value=f"**Server name:** {ctx.author.display_name}\n\n**Mention:** {ctx.author.mention}\n\n**Staff "
                                f"Member ID:** {ctx.author.id}", inline=False)
            ban.add_field(name="Date Banned (year, month, day):", value=f'{datetime.date.today()}', inline=False)
            ban.set_thumbnail(url=m.avatar_url)
            await ctx.reply(f"Ban penalty submitted. Posted in: {channel.mention}")
            return await channel.send(embed=ban)
            # await ctx.reply(embed=banned)

        if uID not in ctx.guild.members:
            await ctx.guild.ban(discord.Object(id=uID), reason=reason)

            m = self.bot.get_user(uID)

            embed = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Member Banned!", value=m.mention, inline=False)
            embed.add_field(name="Member Affected:", value=m.display_name + '#' + m.discriminator, inline=False)
            embed.add_field(name="Member ID:", value=m.id, inline=False)
            embed.add_field(name="Reason Given:", value=reason, inline=False)
            embed.add_field(name="Staff Member Responsible:",
                            value=f"Display name: {ctx.author.display_name}\n\nMention:{ctx.author.mention}\n\nStaff "
                                  f"Member ID: {ctx.author.id}", inline=False)
            embed.add_field(name="Date Of Ban (Year, Month, Day):", value=f"{datetime.date.today()}", inline=False)
            embed.set_thumbnail(url=m.avatar_url)
            await ctx.reply(f"Ban penalty submitted. Posted in {channel.mention}")
            await channel.send(embed=embed)

    @commands.command(name="massban")
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, uID: Greedy[int], *, reason=None):
        if reason is None:
            reason = f"mass banned by {ctx.author.display_name} | {ctx.author.id}"

        limit = 50

        if uID is None:
            return await ctx.reply("This command is used to ban multiple people!")
        if ctx.author.id in uID:
            return await ctx.reply("One of the IDs is your own and I cannot process this command. Please check IDs before trying again.")
        if self.bot.user.id in uID:
            return await ctx.reply("One of the IDs is mine and therefore I cannot process this command. Please check IDs before trying again.")

        if len(uID) == 0:
            return await ctx.reply("I need a list of IDs to ban.")
        if len(uID) > limit:
            return await ctx.reply(f"I cannot ban that amount of people. My limit is {limit}")
        if len(uID) <= limit:
            await ctx.reply(f"Starting banning Process! Banning {uID} members.")
            for uID in uID:
                # m = self.bot.get_user(discord.Object(uID))
                await ctx.guild.ban(discord.Object(uID), reason=reason)
                '''e = discord.Embed(color=discord.Color.random())
                e.add_field(name="Banned:", value=m.id + '\n' + m.mention + '\n' + m.display_name + '#' + m.discriminator)
                e.add_field(name="Reason:", value=reason)
                await self.bot.get_channel(922779595705557082).send(embed=e)'''

        await ctx.reply("Banned members.")


print("loaded Ban and mass ban.")


def setup(bot):
    bot.add_cog(Moderation(bot))
    # bot.add_cog(Moderation_Massban(bot))
