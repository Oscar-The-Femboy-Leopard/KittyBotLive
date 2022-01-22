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

        reason = reason + f'\nBanned by {ctx.author.display_name} | {ctx.author.id} on {datetime.date.today()}'

        guild = ctx.guild

        if (self.bot.get_user(uID)) in guild.members:
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

        if (self.bot.get_user(uID)) not in guild.members:
            await ctx.guild.ban(discord.Object(id=uID), reason=reason)

            m = self.bot.get_user(uID)
            # m = self.bot.get_user(discord.Object(id=uID))

            embed = discord.Embed(title="Member Banned!", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
            # embed.add_field(name="Member Banned!", value=m.mention, inline=False)
            embed.add_field(name="Member Affected:", value=m.display_name + '#' + m.discriminator, inline=False)
            embed.add_field(name="Member ID:", value=m.id, inline=False)
            embed.add_field(name="Reason Given:", value=reason, inline=False)
            embed.add_field(name="Staff Member Responsible:",
                            value=f"Display name: {ctx.author.display_name}\n\nMention:{ctx.author.mention}\n\nStaff "
                                  f"Member ID: {ctx.author.id}", inline=False)
            embed.add_field(name="Date Of Ban (Year, Month, Day):", value=f"{datetime.date.today()}", inline=False)
            embed.set_thumbnail(url=m.avatar_url)
            await ctx.reply(f"Ban penalty submitted. Posted in {channel.mention}")
            # await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command(name="massban")
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, uID: Greedy[int], *, reason=None):
        if reason is None:
            reason = f"mass banned by {ctx.author.display_name} | {ctx.author.id}"

        banlog = self.bot.get_channel()

        limit = 50
        m = ""
        ID = ""

        e = discord.Embed(color=discord.Color.red(), title="Massban", description=f"The following users have been mass banned by {ctx.author.display_name}")

        if uID is None:
            return await ctx.reply("This command is used to ban multiple people!")
        if ctx.author.id in uID:
            return await ctx.reply("One of the IDs is your own therefore I cannot process this command. Please check IDs before trying again.")
        if self.bot.user.id in uID:
            return await ctx.reply("One of the IDs is mine and therefore I cannot process this command. Please check IDs before trying again.")

        if len(uID) == 0:
            return await ctx.reply("I need a list of IDs to ban.")
        if len(uID) > limit:
            return await ctx.reply(f"I cannot ban that amount of people due to limitations. My limit is {limit}")
        if len(uID) <= limit:
            msg = await ctx.reply(f"Starting banning Process! Banning {uID} members.")
            for uID in uID:
                await ctx.guild.ban(discord.Object(uID), reason=reason)
                m = m + f"{self.bot.get_user(uID).display_name}\n"
                ID = ID + f"ID: {self.bot.get_user(uID)}"
            e.add_field(name="Member's Name:", value=m, inline=True)
            e.add_field(name="Member's ID:", value=ID, inline=True)
            await banlog.send(embed=e)
            return await msg.edit(content=f"Banned them all.")


def setup(bot):
    bot.add_cog(Moderation(bot))
