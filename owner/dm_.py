import discord

from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def _dm(self, ctx, uID: int, *, message=None):
        m = (self.bot.get_user(uID))
        if ctx.author.id not in [670932463077556224, 176371068448145408]:
            return

        if message is None:
            await ctx.reply("Please give me the message you want me to send.")

        try:
            await m.send(message)
            await ctx.reply(f"I have sent the DM! The reply is followed:\n\n```{message}```")
        except discord.Forbidden:
            await ctx.reply(f"I cannot DM this user. ({uID} | {m.display_name}#{m.discriminator} | {m.mention})")


def setup(bot):
    bot.add_cog(Owner(bot))
