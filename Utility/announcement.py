from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role(864655957816508446, 864655959884300298, 864655947736678420, 904108509463990294)
    async def announce(self, ctx, *, message):

        message = message

        ment_ping = "ping"
        no_ping = 'n'
        msg = message.split('.', 1)
        '''if ctx.message.guild.id == 904365272184524811:
          announce_ping = self.client.get_role(904405829007065148).mention

          if msg[0] == ment_ping:
            await self.client.get_channel(904405797168103495).send(f'{announce_ping}\n\n{msg[1]}')

          if msg[0] != ment_ping:
            await self.client.get_guild(904365272184524811).get_channel(904405797168103495).send(f"General Announcement!\n\n{msg[1]}")'''


        # if ctx.guild == 864654684085682207:

        role = self.client.get_guild(864654684085682207).get_role(900500138684989460).mention

        # announce_ping = '<@900500138684989460>'

        if msg[0] == ment_ping:
            await self.client.get_guild(864654684085682207).get_channel(864655320801607700).send(f'{role}\n\n{msg[1]}')
            await ctx.send('Successful!')

        if msg[0] == no_ping:
            await self.client.get_guild(864654684085682207).get_channel(864655320801607700).send({msg[1]})
            await ctx.send('Successful')

        else:
            return await ctx.send('Uncessful')

        # await ctx.send('Successful!')


def setup(client):
    client.add_cog(Utility(client))
