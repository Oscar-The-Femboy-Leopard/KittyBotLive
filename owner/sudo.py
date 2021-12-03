from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def speak(self, ctx, *, message):
        message = message

        g = 913007198488133632

        msg = message.split('.', 1)

        stitchlaugh = 'https://media.tenor.co/videos/89a51bb4c0f8992a1e8d5c15e023152d/mp4'

        general = "gen"
        spam = "spam"

        if msg[0] == general:
            if msg[1] == "stitchlaugh":
                await self.bot.get_guild(g).get_channel(913007198488133635).send(f'{stitchlaugh}')
            else:
                await self.bot.get_guild(g).get_channel(913007198488133635).send(f'{msg[1]}')

        if msg[0] == spam:
            if msg[1] == "stitchlaugh":
                await self.bot.get_guild(g).get_channel(913566178033664060).send(f"{stitchlaugh}")
            else:
                await self.bot.get_guild(g).get_channel(913566178033664060).send(f"{msg[1]}")

        await ctx.reply('Done, Mistress!')


def setup(bot):
    bot.add_cog(Owner(bot))
