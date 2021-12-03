from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def speak(self, ctx, *, message):
        message = message

        g = 913007198488133632

        msg = message.split('.', 1)

        general = "gen"


        if msg[0] == general:
            await self.client.get_guild(g).get_channel(913007198488133635).send(f'{msg[1]}')
            await ctx.reply('Done, Mistress!')


def setup(client):
    client.add_cog(Owner(client))
