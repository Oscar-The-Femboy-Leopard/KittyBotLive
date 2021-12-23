import asyncio
import discord

from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx, *, message):
        sent_users = []
        # CHANNEL_ID = 913514927384301568
        CHANNEL_ID = 775770598844137482

        if message.guild:  # ensure the channel is a DM
            return

        if message.author == self.bot.user:
            return

        if message.author.id in sent_users:  # Ensure the initial message hasn't been sent before
            return

        # gg_fluff = self.bot.get_guild(864654684085682207)
        gg_fluff = self.bot.get_guild(488623700539736064)

        modmail_channel = self.bot.get_channel(CHANNEL_ID)

        embed = discord.Embed(color=0x00FFFF)
        embed.set_author(name=f"{gg_fluff} Modmail System",
                         icon_url="https://cdn.discordapp.com/icons/690937143522099220/34fbd058360c3d4696848592ff1c5191.webp?size=1024")
        embed.add_field(name='Report a member:', value=f"React with 1️⃣ if you want to report a member.")
        embed.add_field(name='Report a Staff Member:', value=f"React with 2️⃣ if you want to report a Staff Member.")
        embed.add_field(name='Warn Appeal:', value=f"React with 3️⃣ if you would like to appeal a warning.")
        embed.add_field(name='Question:',
                        value=f"React with 4️⃣ if you have a question about our moderation system or the server rules.")
        embed.set_footer(text="Olympia Gaming | Modmail")
        msg = await message.author.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")

        sent_users.append(message.author.id)  # add this user to the list of sent users

        try:
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]

            reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "1️⃣":
                embed = discord.Embed(color=0x00FFFF)
                embed.set_author(name=f"Olympia Gaming Modmail System",
                                 icon_url="https://cdn.discordapp.com/icons/690937143522099220/34fbd058360c3d4696848592ff1c5191.webp?size=1024")
                embed.add_field(name='How to Report:',
                                value="Send the ID of the person you are reporting and attach add a screen shot of them breaking a rule (can be ToS or a server rule).")
                embed.set_footer(text="Olympia Gaming | Report a member ")
                await message.author.send(embed=embed)

                message = await self.bot.wait_for("message", timeout=60, check=lambda
                    m: m.channel == message.channel and m.author == message.author)
                embed = discord.Embed(title=f"{message.content}", color=0x00FFFF)
                await modmail_channel.send(embed=embed)

        except asyncio.TimeoutError:
            await message.delete()


def setup(bot):
    bot.add_cog(Utility(bot))
