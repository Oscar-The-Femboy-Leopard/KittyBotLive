import random
import discord
from discord.ext import commands
from config import random_color, _blnk_value

aliases = ['Insult']
description = "Runs the insult command! Use this to give a funny insult to someone!"
# description = 'Give someone a petty insult!'


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases,
                      description=description)
    async def insult(self, ctx, *, kill: discord.Member = None):
        color = random.choice(random_color)
        guild = ctx.guild
        msg = ctx
        Kill = kill.display_name
        auth = msg.author.display_name
        killmessage = [f"I would explain it to you, {Kill}, but I don’t have any crayons with me.",
                       f"{Kill} is a person of rare intelligence. It’s rare when they show any.",
                       f"Brains aren’t everything. In fact in your case, {Kill}, they’re nothing.",
                       f"{Kill}, you are proof that evolution **CAN** go in reverse.",
                       f"Don’t you need a license to be that ugly, {Kill}?",
                       f"You’re so dumb, {Kill}, your dog teaches you tricks.",
                       f"Your house is so dirty, {Kill}, you have to wipe your feet before you go outside.",
                       f"I don’t know what makes you so stupid, {Kill}, but it really works.",
                       ]
        msg = random.choice(killmessage)

        _8 = discord.Embed(color=color, timestamp=discord.Message.created_at)
        _8.add_field(name=msg, value=_blnk_value, inline=True)
        _8.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)

        await ctx.send(embed=_8)


def setup(bot):
    bot.add_cog(Fun(bot))
