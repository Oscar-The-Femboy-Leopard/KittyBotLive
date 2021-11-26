from discord.ext import commands


class OwnerCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='load', aliases=["Load", "Enable", "enable"], hidden=True)
    async def load(self, ctx, *, cog: str):
        if ctx.author.id not in [670932463077556224, 176371068448145408]:
            return

        try:
            self.client.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            print("loaded")


def setup(client):
    client.add_cog(OwnerCog(client))
