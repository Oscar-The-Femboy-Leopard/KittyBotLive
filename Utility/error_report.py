import discord

from discord.ext import commands


aliases = ['Error_Report',
           'AlertDev']
description = "This command sends reports to my dev's server, just in case you find an error with me that should be " \
              "addressed! Just make sure to send the error message as well in the message to help her investigate! "


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases, description=description)
    async def alert(self, ctx, *, report):
        _channel = self.bot.get_guild(488623700539736064).get_channel(844351284568260608)
        channel = self.bot.get_guild(904365272184524811).get_channel(905611246563377172)
        role = self.bot.get_guild(488623700539736064).get_role(488642021184241664).mention

        alert = discord.Embed(color=discord.Color.blurple())
        alert.add_field(name="Report!",
                        value=f"I have a report from **{ctx.guild.name}** by {ctx.author.display_name}#{ctx.author.discriminator} which requres your immediate attention! The error report submitted follows below:\n\n```{report}```",
                        inline=False)
        alert.set_thumbnail(url=ctx.author.avatar_url)
        alert.set_footer(text=f"Author ID: {ctx.author.id}")

        await _channel.send(role, embed=alert)
        await channel.send(embed=alert)
        await ctx.reply(f"Thank you, {ctx.author.display_name}. I have alerted my dev server and they will look into "
                        f"it as soon as they can.")


def setup(bot):
    bot.add_cog(Utility(bot))
