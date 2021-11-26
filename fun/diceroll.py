import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Dice Roll', 'Roll the dice'],
                      description="This command will simulate rolling a dice/dye.")
    async def roll(self, ctx, number_of_dice, number_of_sides, roll=int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]


def setup(client):
    client.add_cog(Fun(client))
