import discord
import random

from discord.ext import commands
from config import random_color


class Fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['Dice Roll', 'Roll the dice'],
                      description="This command will simulate rolling a dice/dye.")
    async def roll(self, ctx, number_of_dice, number_of_sides, roll=int):
        colors = random.choice(random_color)
        embed = discord.Embed(color=colors)

        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]

        rdice = dice

        if len(roll.int) == 0:
            print("No valid Users With This Role.")
            embed.add_field(name="You cannot roll 0 dice!", value="_ _", inline=False)
        var = ""
        if len(roll.int) > 0:
            for roll in roll:
                var = var + f"\n {dice}"
                # var = f"\n {dice}"
            embed.add_field(name="Current Verified Artists are:", value=var, inline=False)

        embed.add_field(name="Number of dice rolled:", value=number_of_dice, inline=True)
        embed.add_field(name="Number of sides per dice:", value=number_of_sides, inline=True)
        embed.add_field(name="Result:", value=var, inline=False)

        await ctx.reply(f"The result is:", embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
