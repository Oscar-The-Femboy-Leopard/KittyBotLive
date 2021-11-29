import random
import time
import discord
import asyncio
import datetime

from discord.ext import commands
from owner.rules import _password
from config import PREFIX, random_color

aliases = ["Verify", "verification", "Verification", "verify"]
description = "This command will allow people to send an application to verify to gain access to the server"


class Utility(commands.Cog):
    def __init__(self, client, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client

    @commands.command(name='register', pass_context=True, aliases=aliases, description=description)
    async def verify(self, ctx):

        password = ""
        correctPassword = _password

        channel = self.client.get_guild(913007198488133632).get_channel(913540153753092117)
        guild = self.client.get_guild(913007198488133632)
        r = self.client.get_guild(913007198488133632).get_role(913015562894979082)

        if not ctx.message.guild.id == 913007198488133632:
            return

        if ctx.message.channel.id != 913021716169646160:
            return await ctx.reply("This is the incorrect channel.")

        if r in ctx.author.roles:
            return await ctx.reply("You cannot run this command as you already have been verified.")

        if ctx.message.channel.id == 913021716169646160:

            guidmg = discord.Embed(color=random.choice(random_color))
            guidmg.add_field(name="Thank you for starting the verification process!",
                             value=f"For this verification to work, {ctx.author.mention}, I need the following requirements:",
                             inline=False)
            guidmg.add_field(name="REQUIREMENTS", value="> DMs to be open to me\n\n> Password found in Rules.",
                             inline=False)
            guidmg.set_footer(text="I will need the password as this is a way to prevent people joining who don't read "
                                   "the rules. This step is vital for us all. to be safe")

            '''await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs! Please make sure I can DM you for this "
                       f"to work. If it times out, don't worry, you can run this command again. There is also a "
                       f"password you need to find in the Rules. Sadly, this is a required step since the staff "
                       f"don't want trouble makers in the server.")'''

            await ctx.reply(embed=guidmg)

            a = ctx.author

            def check(m):
                return m.author.id == a.id

            await a.send(
                f"Hi there, welcome to the {guild} registration. \n\nDuring this process, please be respectful and answer "
                f"honestly. Any information, like age, shared with me won't leave this DM, it is just for my end of "
                f"verification to the server.\n\nBefore we can start, can I please have the password found in the rules?")

            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            password = msg.content.lower()
            if password != correctPassword:
                await channel.send(f"{a.display_name} entered the wrong password.")
                return await a.send(
                    f"{a.display_name}, you have the wrong password. Please reread the rules before running the command "
                    f"again.")
            if password == correctPassword:
                await a.send(
                    f"{a.display_name}, you have entered the correct password. Let's start the registration!")

            await a.send(
                "Firstly, can I get your fursona name or a name you prefer? I will be calling you this through "
                "the verification.")

            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            name = msg.content
            await a.send(f"Hello, {name}! May I now get your age? It will only be kept between us in this DM so don't "
                         f"worry about other people knowing :slight_smile:")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            age = 0
            agebracket = ""
            try:
                age = int(msg.content)
            except:
                await ctx.message.author.send(
                    "That is an invalid age. \n\nPlease try again or your registration will be aborted.")
                await asyncio.sleep(1)
                msg = await self.client.wait_for('message', check=check)
                try:
                    age = int(msg.content)
                except:
                    return await ctx.message.author.send(
                        "That is an invalid age.\n\nYour registration has been aborted")
            if age >= 18:
                agebracket = "Adult"
            if age < 18:
                agebracket = "Minor"
            if age > 80:
                await a.send("Please don't be so stupid...")
                await channel.send(f'{a.display_name} just said they where {msg.content}')
            await a.send(
                f"Thanks, to protect your age, you will be shown as a {agebracket} in the server.")

            await a.send("Next, may I know if you're a furry? (`Yes` or `No`)")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            furry = msg.content.lower()

            y = "yes"

            if furry == y:
                await a.send(
                    f"Got it! You are a furry. May I ask what your fursona species is?")
                await asyncio.sleep(1)
                msg = await self.client.wait_for('message', check=check)
                fursona = msg.content
                await a.send(
                    f"Got it, your fursona is a {fursona}.")

                await a.send(
                    "Next, tell me about your fursona.\n\nWhat's their favourite activities? What "
                    "gender are they? Do they like sleeping all day? Anything!\n\n**Note:** if you don't wish to share "
                    "your fursona, tell us some basic info of what you imagine your fursona to be or info about you!")
                await asyncio.sleep(1)
                msg = await self.client.wait_for('message', check=check)
                fursonainfo = msg.content

            if furry != y:
                await a.send(
                    f"Okay, {name}, you aren't a furry. That's fine! I will skip all of the fursona questions for "
                    f"you. ^^")
                fursona = "This person doesn't have a fursona."
                fursonainfo = 'N/A'

            await a.send("Next, may I know what your favourite quote is? If you don't have one, you can just put N/A")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            quote = msg.content
            await a.send(
                f"Got it, your favourite quote/s is/are: {quote}.")
            await a.send("Next, may I know what gender you identify as?")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            gender = msg.content
            await a.send(
                f"Got it, you refer to yourself as {gender}.")
            await a.send("Next, may I know what pronouns you use?")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            pronouns = msg.content
            await a.send(
                f"Got it, you refer to yourself as {gender} using {pronouns} pronouns.")

            await a.send(
                "Next, can you please say how you came to find the server today?")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            foundus = msg.content

            embed = discord.Embed(title="New Member Registration!",
                                  description=f"A registration to become a member has been submitted at {datetime.datetime.utcnow()} by {a.mention} ({a.id}).",
                                  color=discord.Color.blue())
            embed.set_thumbnail(url=a.avatar_url)
            embed.add_field(name='Preferred Name', value=f"{name}", inline=False)
            embed.add_field(name='Age Bracket:', value=f"{agebracket}", inline=False)
            embed.add_field(name='Quote', value=f"{quote}", inline=False)
            embed.add_field(name='Gender', value=f"{gender}", inline=False)
            embed.add_field(name='Pronouns', value=f"{pronouns}", inline=False)
            embed.add_field(name='Fursona:', value=f"{fursona}", inline=False)
            embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
            embed.add_field(name='How this user found the server', value=f"{foundus}", inline=False)
            embed.set_footer(
                text=f'Author {a.id}\n\n`{PREFIX}accept <mention>` to accept or `{PREFIX}deny <mention>` to deny.')

            created = a.created_at

            if time.time() - a.created_at.timestamp() > 2592000:
                embed.add_field(name="Account created check", value=f"{created}", inline=False)
            if time.time() - a.created_at.timestamp() < 2592000:
                embed.add_field(name="Account created check", value=f"{created}", inline=False)

            gatekeeper = self.client.get_guild(913007198488133635).get_role(913552884115853363).mention

            await channel.send(f"New registration, {gatekeeper}!", embed=embed)
            await a.send(
                "Thank you! Your registration has been sent to the staff for review.\n\nThey'll accept you as soon "
                "as possible!")

    @commands.command(name="accept", pass_context=True)
    @commands.has_role("Gatekeeper")
    async def accept(self, ctx, *, m: discord.Member = None):

        guild = ctx.guild
        _channel = guild.get_channel(913007198488133635)
        channel = guild.get_channel(913540153753092117)
        priv = self.client.get_guild(488623700539736064).get_channel(913590152583077888)
        a = ctx.message.author
        roles = guild.get_channel(913534684678471732).mention
        faq = guild.get_channel(913595991951835166).mention
        discover = guild.get_channel(913015273538355201).mention
        member = discord.utils.get(a.guild.roles, id=913015562894979082)
        # deny = discord.utils.get(a.guild.roles, id=841500124383281172)
        emoji = self.client.get_emoji(id=880532960145719307)
        emoji2 = self.client.get_emoji(id=880532998313885817)
        welcome = self.client.get_guild(913007198488133635).get_role(913595000363814932).mention

        await ctx.reply(f'{ctx.author.display_name} has just verified them')
        await priv.send(f"{ctx.author.display_name} verified {ctx.message.content}")

        try:
            await m.add_roles(member)
            # await m.remove_roles(deny)
        except discord.Forbidden:
            await self.client.channel.send("I don't have perms to add roles.")

        await _channel.send(welcome)
        await _channel.send(f'{emoji}{emoji2}')
        await _channel.send(f"Please welcome {m.mention}!\n\n> Please visit {roles} to get yourself some roles!\n\n> "
                            f"If you have any questions about the server, that's not covered by {discover} please go "
                            f"to {faq}")

    '''@commands.command(name="deny", pass_context=True)
    @commands.has_role("Staff")
    async def deny(self, ctx, *, m: discord.Member = None):

        guild = ctx.guild
        channel = guild.get_channel(880218549367492659)
        a = ctx.message.author
        member = discord.utils.get(a.guild.roles, id=841501813755609108)
        deny = discord.utils.get(a.guild.roles, id=841500124383281172)

        await channel.send(f'{ctx.author.display_name} has just denied them. Please speak to that member about the failed verification.')

        try:
            await m.add_roles(deny)
            await m.remove_roles(member)

        except discord.Forbidden:
            await self.client.channel.send("I don't have perms to add roles.")'''


def setup(client):
    client.add_cog(Utility(client))
