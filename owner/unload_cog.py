from discord.ext import commands


class OwnerCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='unload', aliases=['Unload', 'CloseCog', 'StopCog', 'disable', 'Disable'], hidden=True)
    async def unload(self, ctx, *, cog: str):
        if ctx.author.id not in [670932463077556224, 176371068448145408]:
            return

        try:
            self.client.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESSFUL UNLOAD`**')
            print("Unloaded Cog")


def setup(client):
    client.add_cog(OwnerCog(client))
