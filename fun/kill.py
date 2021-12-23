import random
import discord
from discord.ext import commands
from config import random_color, _blnk_value

aliases = ['Kill']
description = "Runs the kill command. Use this command to make a funny death!"


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases,
                      description=description)
    async def kill(self, ctx, *, kill: discord.Member = None):
        color = random.choice(random_color)
        guild = ctx.guild
        msg = ctx
        Kill = kill.display_name
        auth = msg.author.display_name
        if auth == Kill:
            killmessage = [
                f"{auth} has spotted something they don't like so they tried to keep their KD by ewo looping!",
                f"Who would know that {auth} would wanna do that? We should hug them!",
                f"{auth} received a mysterious package of cute puppies from an unknown sender. {auth} opens the package and they die due to cuteness overload.",
                f"{auth} made it look like a suicide but they faked their death!"]
        else:
            killmessage = [f"{auth} forgot to give zombie repellent to {Kill}! I guess zombies enjoyed their feast.",
                           f"{auth} gave too much truth serum to {Kill} so {Kill} told the truth for hours until collapsing and dying.",
                           f"{auth} yeeted {Kill} out of existence!",
                           f"{auth} thew a glitter bomb at {Kill}. {Kill} enjoyed it so much, the immediately died.",
                           f"{auth} fired {Kill} from a confetti cannon! They went pop and out of the top of the tent to never be seen again.",
                           f"{Kill} said something to {auth} that was so funny, {Kill} just died laughing.",
                           f"{Kill} received a mysterious package of cute puppies from {auth}. {Kill} opens the package and they die due to cuteness overload.",
                           f"{auth} called their dog up onto {Kill}'s lap. The dog showed so much affection, it killed {Kill}.",
                           f"{auth} got a group of turtles to give {Kill} an underwater tour. Sadly, {Kill}'s oxygen tank ran out.",
                           ]
        msg = random.choice(killmessage)

        _8 = discord.Embed(color=color, timestamp=discord.Message.created_at)
        _8.add_field(name=msg, value=_blnk_value, inline=True)
        _8.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.send(embed=_8)


def setup(bot):
    bot.add_cog(Fun(bot))
