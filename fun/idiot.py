import random
from discord.ext import commands
from config import idiot_responses

'''await ctx.send("Yes, I am an idiot... Just wish I could accept it. However, my programmer isn't! Please show "
                       "her some love")
        await ctx.send(':heart: :heart:')'''


aliases = ['Idiot', 'Bot is an idiot']


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''@commands.Cog.listener()
    async def on_ready(self):
        print('Idiot is ready')'''

    @commands.command(aliases=aliases,
                      description="This command was originally made to call the bot an idiot. I made the command output that because the 8ball command kept cussing me out. I had fun with that in development but now I'm moving on from that pettiness. However, I have now made it to where it outputs a random comeback as well as the original message. What one will you get?")
    async def idiot(self, ctx):

        await ctx.send(f'{random.choice(idiot_responses)}')


def setup(client):
    client.add_cog(Fun(client))
