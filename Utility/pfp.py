import discord
from discord.ext import commands


aliases = ["PFP", "Avatar", "avatar"]
description = "This will allow you to see any member's profile picture! You do need to mention the user you wish to " \
              "view the profile picture of "


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases, description=description)
    async def pfp(self, ctx, *, avamember: discord.Member = None):
        channel = self.client.get_channel(904112900485021706)
        # channel = 904112900485021706
        staff = [864655958352986112, 864655957816508446, 864655959884300298, 904108509463990294, 904349776659755050, 864655947736678420]
        if not avamember:
            avamember = ctx.message.author
        if ctx.channel is not channel:
            return await ctx.reply("I don't have permission to use this command outside of the designated channel set "
                                   "by my devs.")
        '''if ctx.author.roles not in staff:
            await ctx.reply("This is a staff command. For help, please message Michelle directly.")'''

        gettt = self.client.get_user(avamember)

        userAvatarUrl = avamember.avatar_url
        userBannerURL = gettt.fetch_user.banner_url
        msg = ctx
        guild = msg.guild

        pfp = discord.Embed(color=ctx.message.author.top_role.color, description="**Profile Picture Requested:**")
        pfp.add_field(name="User:", value=avamember.display_name, inline=True)
        pfp.set_image(url=userAvatarUrl)
        pfp.set_image(url=userBannerURL)
        pfp.set_footer(text=f'Requested by {ctx.author}')

        await ctx.send(embed=pfp)


def setup(client):
    client.add_cog(Utility(client))