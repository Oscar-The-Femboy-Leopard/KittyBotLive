import discord
import random
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="This command will flip things!")
    async def flip(self, ctx, user: discord.Member = None):
        if user != None:
            msg = ""
            if user.id == self.client.user.id:
                user = ctx.message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
                char = "abcdefghijklmnopqrstuvwxyz"
                tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
                table = str.maketrans(char, tran)
                name = user.name.translate(table)
                char = char.upper()
                tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
                table = str.maketrans(char, tran)
                name = name.translate(table)
                return await ctx.send(ctx + "(╯°□°）╯︵ " + name[::-1])
            else:
                ht = random.choice(["**HEADS!**", "**TAILS!**"])
                return await ctx.send(f"*flips a coin and it hands on:*\n\n {ht}")
                # return await ctx.send("*flips a coin and... " + random.choice(["HEADS!*", "TAILS!*"]))


def setup(client):
    client.add_cog(Fun(client))
