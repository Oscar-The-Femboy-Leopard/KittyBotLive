import random
import discord
import asyncio
import datetime
# import urllib.parse

from discord.ext import commands
from owner.rules import _password
from config import PREFIX, random_color
from moderation.ban import ban_appeal


aliases = ["Verify", "verification", "Verification", "verify"]
description = "This command will allow people to send an application to verify to gain access to the server"


class Utility(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot

    @commands.command(name='register', pass_context=True, aliases=aliases, description=description)
    async def verify(self, ctx):
        password = ""
        msg = ""
        correctPassword = _password

        channel = self.bot.get_guild(913007198488133632).get_channel(913540153753092117)
        _guild = self.bot.get_guild(913007198488133632)
        r = self.bot.get_guild(913007198488133632).get_role(913015562894979082)

        imgsearch = 'https://images.google.com/searchbyimage?image_url='
        # pfp = urllib.parse.quote(ctx.author.avatar_url, safe='')

        c = random.choice(random_color)

        guidmg = discord.Embed(color=c)
        guidmg.add_field(name="Thank you for starting the verification process!",
                         value=f"For this verification to work, {ctx.author.mention}, I need the following requirements:",
                         inline=False)
        guidmg.add_field(name="REQUIREMENTS", value="> DMs to be open to me\n\n> Password found in Rules.",
                         inline=False)
        guidmg.set_footer(text="I will need the two parts of the password from the rules as this is a way to prevent "
                               "people joining who don't read the rules. This step is vital for us all. to be "
                               "safe\n**NOTE:** The password contains 2 words found different places of the rules ("
                               "Please enter them in the way they come from the rules ~~top to bottom~~).")

        await ctx.reply(embed=guidmg)

        a = ctx.author

        def check(m):
            return m.author.id == a.id

        '''if ctx.message.guild:
            return'''

        if r in a.roles:
            return await ctx.reply("You already have been verified!")

        try:
            await a.send(
                f"Hi there, welcome to the {_guild} registration.\n\nDuring this process, please be respectful and answer "
                f"honestly. Any information, like age, shared with me won't leave this DM, it is just for my end of "
                f"verification to the server.\nYou can type `cancel` on any question and it will cancel verification "
                f"until you run the command again.\n\nBefore we can start, can I please have the password found in the "
                f"rules?")
        except discord.Forbidden:
            return await ctx.reply(
                "I am sorry, but I cannot DM you. Can you open the DMs to the server to verify and try again?\nThank you.")

        if msg in ctx.message.guild:
            return

        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        password = msg.content.lower()
        if password == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        if password != correctPassword:
            await channel.send(f"{a.display_name} entered the wrong password. They entered: {password}")
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
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        name = msg.content
        if name == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        await a.send(f"Hello, {name}! May I now get your age? It will only be kept between us in this DM so don't "
                     f"worry about other people knowing :slight_smile:")
        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        if msg.content.lower() == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        age = 0
        agebracket = ""
        try:
            age = int(msg.content)
        except:
            await ctx.message.author.send(
                "That is an invalid age. \n\nPlease try again or your registration will be aborted.")
            await asyncio.sleep(1)
            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await a.send('Verification has timed out. Please rerun the command.')
            try:
                age = int(msg.content)
            except:
                return await ctx.message.author.send(
                    "That is an invalid age.\n\nYour registration has been aborted")
        if age >= 18:
            agebracket = "Adult"
        if age < 18:
            agebracket = "Minor"
        if age < 13:
            await a.send(f"I am sorry, {name}, but due to what you have stated is your age - `{age}` - it is below "
                         f"the member age the TOS states therefore you're going to be banned. You can appeal here "
                         f"when you're over TOS age of 13.\n\n{ban_appeal}")
            await ctx.guild.ban(discord.Object(a.id), reason=f"Banned at Verification. Stated they where {age} which is Discord TOS violating. | {ctx.guild}")
            return await channel.send(f"User said they where {age} and therefore have been banned automatically.")
        if age > 80:
            await a.send("Please don't be so stupid...")
            await channel.send(f'{a.display_name} just said they where {age}')
        await a.send(f"Thank you. As promised, I will protect your age and show you as {agebracket}")

        await a.send("Next, may I know if you're a furry? (`Yes` or `No`)")
        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        furry = msg.content.lower()

        if furry == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        y = "yes"

        if furry == y:
            await a.send(
                f"Got it! You are a furry. May I ask what your fursona species is?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            fursona = msg.content.lower()
            if fursona == 'cancel':
                await channel.send(f"{a.display_name} has cancelled their verification.")
                return await a.send(f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
            await a.send(
                f"Got it, your fursona is a {fursona}.")

            await a.send(
                "Next, tell me about your fursona.\n\nWhat's their favourite activities? What "
                "gender are they? Do they like sleeping all day? Anything!\n\n**Note:** if you don't wish to share "
                "your fursona, tell us some basic info of what you imagine your fursona to be or info about you!")
            await asyncio.sleep(1)
            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await a.send('Verification has timed out. Please rerun the command.')
            fursonainfo = msg.content.lower()

            if fursonainfo == 'cancel':
                await channel.send(f"{a.display_name} has cancelled their verification.")
                return await a.send(f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        if furry != y:
            await a.send(
                f"Okay, {name}, you aren't a furry. That's fine! I will skip all of the fursona questions for "
                f"you. ^^")
            fursona = "This person doesn't have a fursona."

            await a.send("Because you don't have a fursona, can I know what hobbies you enjoy?")
            await asyncio.sleep(1)
            try:
                msg = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await a.send('Verification has timed out. Please rerun the command.')
            hobby = msg.content.lower()

            if hobby == 'cancel':
                await channel.send(f"{a.display_name} has cancelled their verification.")
                return await a.send(f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        await a.send("Next, may I know what your favourite quote is? If you don't have one, you can just put N/A")
        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        quote = msg.content.lower()
        if quote == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        await a.send(
            f"Got it, your favourite quote/s is/are: {quote}.")

        await a.send(
            "Next, can you please say how you came to find the server today?")
        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        foundus = msg.content.lower()
        if foundus == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        await a.send(
            "Finally, can I have why you're wanting to get from joining us today?"
        )
        await asyncio.sleep(1)
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            return await a.send('Verification has timed out. Please rerun the command.')
        want = msg.content.lower()
        if want == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        embed = discord.Embed(title="New Member Registration!",
                              description=f"A registration to become a member has been submitted at {datetime.datetime.utcnow()}{datetime.timezone.utc} by {a.mention} | {a.display_name} ({a.id}).",
                              color=c)
        embed.set_thumbnail(url=a.avatar_url)
        embed.add_field(name='Preferred Name', value=f"{name}", inline=False)

        embed.add_field(name='Age Bracket:', value=f"{agebracket}", inline=False)
        embed.add_field(name='Quote', value=f"{quote}", inline=False)

        embed.add_field(name='Fursona:', value=f"{fursona}", inline=False)
        if furry == y:
            embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        if furry != y:
            embed.add_field(name="Hobbies", value=f"{hobby}", inline=False)

        embed.add_field(name='How this user found the server', value=f"{foundus}", inline=True)
        embed.add_field(name="What is want from joining", value=f"{want}", inline=True)

        embed.add_field(name="Created Account on:", value=a.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined On:", value=a.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.set_footer(
            text=f'Author {a.id}\n\n`{PREFIX}accept <mention>` to accept or `{PREFIX}deny <mention> <reason>` to deny.'
        )

        gatekeeper = self.bot.get_guild(913007198488133632).get_role(913552884115853363).mention

        await channel.send(f"New Verification! {gatekeeper}", embed=embed)
        await a.send(
            "Thank you! Your registration has been sent to the staff for review.\n\nThey'll accept you as soon "
            "as possible!"
        )

    @commands.command(name="accept", aliases=["A", "a"], pass_context=True)
    @commands.has_role(913552884115853363)
    async def accept(self, ctx, uID: int):
        a = ctx.message.author
        guild = ctx.guild

        _channel = guild.get_channel(913007198488133635)
        channel = guild.get_channel(913540153753092117)
        priv = self.bot.get_guild(488623700539736064).get_channel(913590152583077888)
        roles = guild.get_channel(913534684678471732).mention
        suggestions = guild.get_channel(913553966401474650).mention
        faq = guild.get_channel(913595991951835166).mention
        discover = guild.get_channel(913015273538355201).mention

        welcome = discord.utils.get(a.guild.roles, id=913595000363814932).mention
        member = discord.utils.get(a.guild.roles, id=913015562894979082)

        emoji = self.bot.get_emoji(id=880532960145719307)
        emoji2 = self.bot.get_emoji(id=880532998313885817)
        m = ctx.guild.get_member(user_id=uID)

        if m is not None:
            try:
                await m.add_roles(member)
                await ctx.reply(f'{ctx.author.display_name} has just verified {m.display_name}')
                await priv.send(f"{ctx.author.display_name} verified {m.display_name}#{m.discriminator} | UID: {m.id}")

                e = discord.Embed(color=random.choice(random_color))
                e.add_field(name=f"New Join!",
                            value=f"Welcome {m.mention}\n\n> Please visit {roles} to get yourself some roles!\n\n> If you "
                                  f"have any question about where a channel is or for, please visit {discover} and it will "
                                  f"direct you.\n\n> If any questions, please visit {faq} before asking staff since what you "
                                  f"may want to ask could be here.\n\n> If you ever have any suggestions for the server, "
                                  f"please visit {suggestions}!")
                e.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)

                await _channel.send(f'{emoji}{emoji2}')
                await _channel.send(welcome, embed=e)

                msg = f"You have been verified in {ctx.guild.name}. Please message staff if you have any problems within the " \
                      f"server. - \n\n**Owner: {ctx.guild.owner.display_name}**\n**Bot: {self.bot.user.display_name}** "

                _e = discord.Embed(name="Accepted!", color=discord.Color.green())
                _e.add_field(name="Congratulations!", value=msg, inline=False)
                _e.add_field(name="Time of acceptance:", value=f"{datetime.datetime.now()}", inline=False)

                try:
                    await m.send(embed=_e)
                except discord.Forbidden:
                    await ctx.reply(f"I was unable to alert {m.display_name} that they was accepted.")

            except discord.Forbidden:
                await self.bot.channel.send("I don't have perms to add roles.")
            return

        if m is None:
            return await ctx.reply(f"Member {self.bot.get_user(uID).display_name} is not present in this server.")

    @commands.command(name="deny", pass_context=True)
    @commands.has_role(913552884115853363)
    async def deny(self, ctx, uID: int, *, reason=None):
        priv = self.bot.get_guild(488623700539736064).get_channel(913590152583077888)

        m = (self.bot.get_user(uID))

        if reason is None:
            await ctx.reply("Please give me the message you want me to send.")

        else:
            _reason = f"Your verification has been denied from {ctx.guild} for the following reason:\n\n{reason}"
            # print(_reason)

        try:
            await m.send(_reason)
            await ctx.reply(f"I have sent the DM! The reply is followed:\n\n```{_reason}```")
        except discord.Forbidden:
            await ctx.reply(f"I am sadly unable to dm {m.display_name}. The reason cannot be sent.")

        await priv.send(f"{ctx.author.display_name} denied {m.display_name} with following reason:\n\n{reason}")


def setup(bot):
    bot.add_cog(Utility(bot))
