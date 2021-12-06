import asyncio
import random
from discord.ext import commands
from mainconfig import Bot_ID

'''class Fun(commands.Cog):
    def __init__(self, client):
        self.message = None
        self.client = client

    @commands.command(aliases=['Guess the Number', 'Guess 1-50', 'numguess'],
                      description="Take a guess of a number between 1 and 50")
    # This basically just says that it's a command and that the aliases are them and it sets the description for the command
    async def NumGuess(self, value):
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            pass


class Guess(commands.Bot):
    async def get_context(self, message, *, cls=Fun):
        return await super().get_context(message, cls=cls)


@commands.command()
async def guess(ctx, number: int):
    """Guess a number 1 to 50"""
    value = random.randint(1, 50)
    await ctx.tick(number == value)'''


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Guess', 'GuessNumber'],
                      description="Guess the client's random number!")
    async def guess(self, message):
        # we do not want the client to reply to itself
        if message.author.id == Bot_ID:
            return

        else:
            await message.channel.send('Guess a number between 1 and 10.')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 15)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

            if int(guess.content) == answer:
                await message.channel.send('You are right!')
            else:
                await message.channel.send('Oops. It is actually {}.'.format(answer))


def setup(client):  # Sets up the client for the client
    client.add_cog(Fun(client))  # Adds the command to the client for it to be able to run
