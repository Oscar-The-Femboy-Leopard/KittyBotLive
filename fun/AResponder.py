"""@commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.client:
            msg = message
            guild = message.guild
            gold = discord.Color.dark_gold()
            bad_list = ["SWEAR",
                        "SWEAR",
                        "SWEAR"]
            responses = ["RESPONSE",
                         "RESPONSE",
                         "RESPONSE"]
            for bad_word in bad_list:
                if bad_word in message.content:
                    response = random.choice(responses)
                    c_r = str(f"""
import random
import discord
from discord.ext import commands
from mainconfig import Fuzzball_ID


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.client:
            ID = Fuzzball_ID
            msg = message
            guild = message.guild
            gold = discord.Color.dark_gold()
            # author = ID
            fuzzball_list = ["Goodnight Mistress",
                             "goodnight mistress",
                             "Goodnight misress",
                             "goodnight",
                             "Goodnight"]
            responses = ["Goodnight my little fuzzball",
                         "Night my big fuzzball, sweet dreams",
                         "Night my little fuzzball, sweet dreams"]
            if msg.author == ID:
                for fuzz in fuzzball_list:
                    if fuzz in message.content:
                        response = random.choice(responses)
                        c_r = str(f"""```css\n{response}```""")
                        embed = discord.Embed(color=gold, timestamp=msg.created_at)
                        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                        embed.add_field(name="⚠", value=c_r, inline=False)
                        embed.set_thumbnail(url=self.client.user.avatar_url)
                        embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                        await message.channel.send(embed=embed)
                    return

            else:
                return

    '''@commands.command(hidden=True)
    async def idiot(self, ctx):
        await ctx.send("Yes, I am an idiot... Just wish I could accept it. However, my programmer isn't! Please show "
                       "her some love")
        await ctx.send(':heart: :heart:')'''


def setup(client):
    client.add_cog(Fun(client))
