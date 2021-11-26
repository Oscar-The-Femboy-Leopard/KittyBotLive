import discord
import datetime

from discord.ext import commands

baliases = ['Ban', 'Ban_member', 'Ban_Member']
bdescription = "This command is self explanitory. It bans members from the server."

haliases = ['hackban']
hdescription = "Use this command to ban someone outside of the server!"

ban_appeal = "https://forms.gle/nspdFFGKvJ54A85g9"


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=baliases, description=bdescription)
    @commands.has_any_role(864655957816508446, 864655959884300298, 864655947736678420, 488642021184241664)
    async def ban(self, ctx, member: int, *, reason=None):

        channel = self.client.get_channel(913736166782681118)

        m = (self.client.get_user(member))

        if m == None:
            return await ctx.reply("You need to name someone to ban.")
        if ctx.author.id == m:
            return await ctx.reply("You cannot ban yourself")
        if reason == None:
            return await ctx.reply("We need a reason for this ban.")

        if m in ctx.guild:
            message = f"You have been banned from {ctx.guild.name} for {reason}."

            # await member.send(message)
            banned = discord.Embed(color=discord.Color.green())
            banned.add_field(name="You're banned!", value=message + f"\n\nYou can appeal the ban [here]({ban_appeal})")
            banned.add_field(name="Date Of Ban:", value=f'{datetime.date.today()}', inline=False)

            await m.send(m.mention, embed=banned)

            await m.ban(reason=reason)

            ban = discord.Embed(color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
            ban.add_field(name="Member Banned!", value=m.mention, inline=False)
            ban.add_field(name="Member Affected:", value=m.display_name + "#" + m.discriminator, inline=False)
            ban.add_field(name="Member's ID:", value=m.id, inline=False)
            ban.add_field(name="Reason Given:", value=reason, inline=False)
            ban.add_field(name="Staff Member Responsible:",
                          value=f"Server name: {ctx.author.display_name}\n\nMention:{ctx.author.mention}\n\nStaff "
                                f"Member ID: {ctx.author.id}", inline=False)
            ban.add_field(name="Date Banned (year, month, day):", value=f'{datetime.date.today()}')
            ban.set_thumbnail(url=m.avatar_url)
            await ctx.reply(f"Ban penalty submitted. Posted in: {channel.mention}")
            await channel.send(embed=ban)

        else:
            await m.ban(reason=reason)

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
            await ctx.reply(f"Ban penelty submitted. Posted in {channel.mention}")
            await channel.send(embed=embed)

    '''@commands.command(aliases=haliases, description=hdescription)
    @commands.has_any_role(864655957816508446, 864655959884300298, 864655947736678420, 488642021184241664,
                           904108509463990294)
    async def hban(self, ctx, userID: int, *, reason=None):

        channel = self.client.get_channel(900520129627037707)

        if reason == None:
            reason = "No reason was given."
        guild = ctx.guild
        if userID in guild.members:
            embed = discord.Embed(color=discord.Color.orange())
            embed.add_field(name="UNCESSFUL", value="Member is currently in this server.")
            await ctx.reply(embed=embed)

        else:
            await ctx.guild.ban(discord.Object(id=userID))
            embed = discord.Embed(color=discord.Color.orange())
            # embed.add_field(name="Member Name", value=discord.Member.id.member_display_name + "#" + discord.Member.id.member_discriminator, inline=False)

            embed.add_field(name="Member id:", value=f'{userID}', inline=False)
            embed.add_field(name="Reason", value=reason, inline=False)
            embed.add_field(name="Staff Member Responsible:",
                            value=f"Server name: {ctx.author.display_name}\n\nMention:{ctx.author.mention}\n\nStaff Member ID: {ctx.author.id}",
                            inline=False)
            # embed.set_thumbnail(url=userID.avatar_url)
            embed.add_field(name="Date Banned (Year, Month, Day):", value=f'{datetime.date.today()}')
            await ctx.reply("banned")
            # await ctx.send("banned {}".format(discord.Member.id.display_name))
            await channel.send(embed=embed)'''


def setup(client):
    client.add_cog(Moderation(client))
