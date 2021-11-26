import datetime
import discord
import random
import pip
from discord.ext import commands
from config import Owner_ID, random_color


class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['binfo', 'AboutB', 'About this Bot'],
                      description='This will give a short description about the bot.')
    async def botinfo(self, ctx):
        message = ctx
        darkmane_id = '512608629992456192'
        wynter_id = '548269826020343809'

        if not message.author.bot:
            guild = message.guild
            _color = random.choice(random_color)
            """
            response = f"Hello there! I am a bot programmed by <@{Owner_ID}> for her server, {guild.name}. I am currently in development so keep that in mind and let her know if you desire any sort of change to be done to my code."
            response_2 = f"She has worked hard to make me work as reliable as possible. <@{darkmane_id}> has been nice enough to help my developer setup API from <@{wynter_id}> for some commands so a big thank you to him is in order. My developer, <@{Owner_ID}>, will appreciate any sort of feedback you give her so please give her any sort of suggestion you may have as it might have an improvement to how I work!"
            response_3 = "I hope you enjoy my presence and my dev and server owner, wishes you that you enjoy your stay here!"
            response_4 = f'{self.client.get_guild()}'"""

            beta_response = f"Hello there! I am a bot designed and programmed by <@{Owner_ID}>. I am currently allowed into Mech factory, autherised by Jacob, for some beta testing. I am currently self hosted on my dev's bad laptop so take that into consideration if I am running a bit slow. My developer will be happy for any feedback you can give her.\n\n Thank you in advance, my dev"
            version = pip.__version__
            build = "v0.9"
            # number_of_guilds = f"{discord.client.Guild.get_guilds}"
            info = discord.Embed(color=_color, timestamp=datetime.datetime.utcnow())
            info.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            # info.add_field(name="Info about me!", value=f"{response} {response_2}\n\n {response_3}", inline=False)
            info.add_field(name="Info about me!", value=f"{beta_response}", inline=False)
            info.add_field(name="Pip Version:", value=version, inline=False)
            info.add_field(name="Bot Build:", value=build, inline=False)
            # info.add_field(name="Number Of Guilds Bot Is In:", value=number_of_guilds, inline=True)
            info.set_thumbnail(url=self.client.user.avatar_url)
            # info.set_footer(text=f"{guild.name}", icon_url=guild.icon_url)
            await message.channel.send(embed=info)
            return


def setup(client):
    client.add_cog(Utility(client))
