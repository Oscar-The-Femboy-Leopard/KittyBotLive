from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(hidden=True)
    async def _dm(self, ctx, uID: int, *, message=None):
        if ctx.author.id not in [670932463077556224, 176371068448145408]:
            return

        if message == None:
            await ctx.reply("Please give me the message you want me to send.")

        await (self.client.get_user(uID)).send(message)
        await ctx.reply(f"I have sent the DM! The reply is followed:\n\n```{message}```")


def setup(client):
    client.add_cog(Owner(client))
