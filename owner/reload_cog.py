from discord.ext import commands


class OwnerCog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='reload', aliases=['update', 'cog update'], hidden=True)
    @commands.has_any_role(904365555627229254, 488642021184241664)
    async def reload(self, ctx, *, cog: str):
        if ctx.author.id not in [670932463077556224, 176371068448145408]:
            return

        try:
            self.client.unload_extension(cog)
            self.client.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            print("reloaded")

            
def setup(bot):
    bot.add_cog(OwnerCog(bot))
