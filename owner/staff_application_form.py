import discord
import random
import asyncio
import datetime

from discord.ext import commands
from config import random_color, PREFIX
from datetime import time


class Staff_Applications(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def apply_staff(self, ctx):
        channel = self.bot.get_guild(913007198488133632).get_channel(913540153753092117)
        _guild = self.bot.get_guild(913007198488133632)
        r = self.bot.get_guild(913007198488133632).get_role(913019115856359424)

        c = random.choice(random_color)

        guidmg = discord.Embed(color=c)
        guidmg.add_field(name="Thank you for starting the Staff Application process!",
                         value=f"For this application to work, {ctx.author.mention}, I need the following requirements:",
                         inline=False)
        guidmg.add_field(name="REQUIREMENTS",
                         value="> DMs to be open to me\n\n> No infractions within the last month\n\n> Trustworthy.",
                         inline=False)
        guidmg.set_footer(text="I will need the password as this is a way to prevent people joining who don't read "
                               "the rules. This step is vital for us all. to be safe")

        await ctx.reply(embed=guidmg)

        a = ctx.author

        def check(m):
            return m.author.id == a.id

        if r in a.roles:
            return await ctx.reply("You already are staff!")

        if time.time() - a.joined_at.timestamp() < 2592000:
            return await ctx.reply(f"You haven't been here long enough to become staff, {ctx.author.mention}. Please "
                                   f"try again at a different opportunity.")

        await a.send(
            "Firstly, can I get your fursona name or a name you prefer? I will be calling you this through "
            "the application.")

        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        name = msg.content

        await a.send("Next, may I know if you're a furry? (`Yes` or `No`)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        furry = msg.content.lower()

        y = "yes"

        if furry == y:
            await a.send(
                f"Got it! You are a furry. May I ask what your fursona species is?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            fursona = msg.content
            await a.send(
                f"Got it, your fursona is a {fursona}.")

            await a.send(
                "Next, tell me about your fursona.\n\nWhat's their favourite activities? What "
                "gender are they? Do they like sleeping all day? Anything!\n\n**Note:** if you don't wish to share "
                "your fursona, tell us some basic info of what you imagine your fursona to be or info about you!")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            fursonainfo = msg.content

        if furry != y:
            await a.send(
                f"Okay, {name}, you aren't a furry. That's fine! I will skip all of the fursona questions for "
                f"you. ^^")
            fursona = "This person doesn't have a fursona."

            await a.send("Because you don't have a fursona, can I know what hobbies you enjoy?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            hobby = msg.content

        await a.send("Next, may I know what your favourite quote is? If you don't have one, you can just put N/A")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        quote = msg.content
        await a.send(
            f"Got it, your favourite quote/s is/are: {quote}.")
        await a.send("Next, may I know what gender you identify as?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        gender = msg.content
        await a.send(
            f"Got it, you refer to yourself as {gender}.")
        await a.send("Next, may I know what pronouns you use?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        pronouns = msg.content
        await a.send(
            f"Got it, you refer to yourself as {gender} using {pronouns} pronouns.")

        await a.send(
            "Next, What makes you think that you would be a useful part of the staff team?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        viable = msg.content

        embed = discord.Embed(title="New Member Registration!",
                              description=f"A registration to become a member has been submitted at {datetime.datetime.utcnow()} by {a.mention} ({a.id}).",
                              color=c)
        embed.set_thumbnail(url=a.avatar_url)
        embed.add_field(name='Preferred Name', value=f"{name}", inline=False)
        embed.add_field(name='Quote', value=f"{quote}", inline=False)
        embed.add_field(name='Gender', value=f"{gender}", inline=False)
        embed.add_field(name='Pronouns', value=f"{pronouns}", inline=False)
        embed.add_field(name='Fursona:', value=f"{fursona}", inline=False)
        if furry == y:
            embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        if furry != y:
            embed.add_field(name="Hobbies", value=f"{hobby}", inline=False)
        embed.add_field(name='How this user will be useful to staff team', value=f"{viable}", inline=False)

        await channel.send(f"New Staff Application!", embed=embed)
        await a.send(
            "Thank you! Your registration has been sent to the staff for review.\n\nThey'll accept you as soon "
            "as possible!")


def setup(bot):
    bot.add_cog(Staff_Applications(bot))
