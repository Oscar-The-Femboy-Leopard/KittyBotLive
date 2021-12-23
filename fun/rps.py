import random
from discord.ext import commands

aliases = ['RockPaperScissors']
description = "Play Rock Paper Scissors with the bot!"


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alias=aliases,
                      description=description)
    async def rps(self, ctx, choice: str):
        author = ctx.message.author
        rpsbot = {"rock": ":rock:",
                  "paper": ":page_facing_up:",
                  "scissors": ":scissors:"}
        choice = choice.lower()
        if choice in rpsbot.keys():
            botchoice = random.choice(list(rpsbot.keys()))
            msgs = {
                "win": " You win {}!".format(author.mention),
                "square": " Draw! {}!".format(author.mention),
                "lose": " You lose {}!".format(author.mention)
            }
            if choice == botchoice:
                await ctx.channel.send(rpsbot[botchoice] + msgs["square"])
            elif choice == "rock" and botchoice == "paper":
                await ctx.channel.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "rock" and botchoice == "scissors":
                await ctx.channel.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "rock":
                await ctx.channel.send(rpsbot[botchoice] + msgs["win"])
            elif choice == "paper" and botchoice == "scissors":
                await ctx.channel.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "rock":
                await ctx.channel.send(rpsbot[botchoice] + msgs["lose"])
            elif choice == "scissors" and botchoice == "paper":
                await ctx.channel.send(rpsbot[botchoice] + msgs["win"])
        else:
            await ctx.channel.send("Choose rock, paper or scissors.")


def setup(bot):
    bot.add_cog(Fun(bot))
