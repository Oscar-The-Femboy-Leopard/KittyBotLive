from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    @commands.is_owner()
    async def speak(self, ctx, *, message):
        message = message

        msg = message.split('.', 1)

        jastico_test = "jt"
        bot_alrert = "ba"
        # lovers_zone = 'lz'
        intro_channel = 'ic'

        if msg[0] == jastico_test:
            await self.client.get_guild(904365272184524811).get_channel(904365272184524814).send(f'{msg[1]}')
            await ctx.reply(':thumbs_up:')

        if msg[0] == bot_alrert:
            await self.client.get_guild(864654684085682207).get_channel(905520433766486067).send(f'{msg[1]}')
            await ctx.reply('Done, Mistress!')

        '''if msg[0] == lovers_zone:
            await self.client.get_guild(864654684085682207).get_channel(904021983807807499).send(f'{msg[1]}')
            await ctx.reply('Done, Mistress!')'''

        if msg[0] == intro_channel:
            await self.client.get_guild(864654684085682207).get_channel(864655467224367164).send(f'{msg[1]}')
            await ctx.reply('Done!')


def setup(client):
    client.add_cog(Owner(client))
