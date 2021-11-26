import discord
import random
from discord.ext import commands
from config import bad_list, blist_responses, unfair_message


class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            msg = message
            guild = message.guild
            gold = discord.Color.dark_gold()

            for bad_word in bad_list:
                if bad_word in message.content:
                    response = random.choice(blist_responses)
                    r2 = unfair_message
                    c_r = str(f"""```css\n{response}```""")
                    embed = discord.Embed(color=gold, timestamp=msg.created_at)
                    embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                    embed.add_field(name="⚠", value=c_r, inline=False)
                    embed.add_field(name="Unfair?", value=r2, inline=False)
                    embed.set_thumbnail(url=self.client.user.avatar_url)
                    embed.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
                    await message.channel.purge(message.author)
                    await message.channel.send(embed=embed)
                    return


def setup(client):
    client.add_cog(Automod(client))
