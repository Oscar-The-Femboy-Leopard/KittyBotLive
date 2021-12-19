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

    '''@commands.Cog.listener()
    async def on_member_join(self, ctx, m: discord.Member):
        self.client.get_user()
        if m.created_at >='''

    @commands.command(name='register', pass_context=True, aliases=aliases, description=description)
    async def verify(self, ctx):

        password = ""
        correctPassword = _password

        channel = self.client.get_guild(913007198488133632).get_channel(913540153753092117)
        _guild = self.client.get_guild(913007198488133632)
        r = self.client.get_guild(913007198488133632).get_role(913015562894979082)

        c = random.choice(random_color)

        guidmg = discord.Embed(color=c)
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
            await ctx.reply(
                "I am sorry, but I cannot DM you. Can you open the DMs to the server to verify and try again?\nThank you.")

        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        password = msg.content.lower()
        if password == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
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
        if name == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        await a.send(f"Hello, {name}! May I now get your age? It will only be kept between us in this DM so don't "
                     f"worry about other people knowing :slight_smile:")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
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
        if age < 13:
            agebracket = f"Minor | **WARNING: USER DECLARED THEY'RE UNDER 13** (`{age}`)"
        if age > 80:
            await a.send("Please don't be so stupid...")
            await channel.send(f'{a.display_name} just said they where {age}')
        await a.send(
            f"Thanks, to protect your age, you will be shown as a {agebracket} in the server.")

        await a.send("Next, may I know if you're a furry? (`Yes` or `No`)")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
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

            await a.send("Because you don't have a fursona, can I know what hobbies you enjoy?")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            hobby = msg.content

        await a.send("Next, may I know what your favourite quote is? If you don't have one, you can just put N/A")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        quote = msg.content.lower()
        if quote == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        await a.send(
            f"Got it, your favourite quote/s is/are: {quote}.")

        await a.send("Next, may I know what gender you identify as?")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        gender = msg.content.lower()
        if gender == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        await a.send(
            f"Got it, you refer to yourself as {gender}.")

        await a.send("Next, may I know what pronouns you use?")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        pronouns = msg.content.lower()
        if pronouns == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")
        await a.send(
            f"Got it, you refer to yourself as {gender} using {pronouns} pronouns.")

        await a.send(
            "Next, can you please say how you came to find the server today?")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        foundus = msg.content.lower()
        if foundus == 'cancel':
            await channel.send(f"{a.display_name} has cancelled their verification.")
            return await a.send(
                f"{a.display_name}, you have canceled your verification. You can rerun this command when you're ready.")

        await a.send(
            "Finally, can I have why you're wanting to get from joining us today?"
        )
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
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
        embed.add_field(name='Gender', value=f"{gender}", inline=False)
        embed.add_field(name='Pronouns', value=f"{pronouns}", inline=False)
        embed.add_field(name='Fursona:', value=f"{fursona}", inline=False)
        if furry == y:
            embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        if furry != y:
            embed.add_field(name="Hobbies", value=f"{hobby}", inline=False)
        embed.add_field(name='How this user found the server', value=f"{foundus}", inline=False)
        embed.add_field(name="What is want from joining", value=f"{want}", inline=False)
        embed.set_footer(
            text=f'Author {a.id}\n\n`{PREFIX}accept <mention>` to accept or `{PREFIX}deny <mention> <reason>` to deny.'
        )

        created = a.created_at

        if time.time() - a.created_at.timestamp() > 2592000:
            embed.add_field(name="Account created check", value=f"{created}", inline=False)
        if time.time() - a.created_at.timestamp() < 2592000:
            embed.add_field(name="Account created check", value=f"{created} | New Account", inline=False)

        gatekeeper = self.client.get_guild(913007198488133632).get_role(913552884115853363).mention

        await channel.send(f"New Verification! {gatekeeper}", embed=embed)
        await a.send(
            "Thank you! Your registration has been sent to the staff for review.\n\nThey'll accept you as soon "
            "as possible!"
        )

    '''@verify.error()
    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.Forbidden):
            await ctx.reply("Cannot find the required emoji.\n\n{}").format(error)'''

    @commands.command(name="accept", pass_context=True)
    @commands.has_role(913552884115853363)
    async def accept(self, ctx, *, m: discord.Member):
        a = ctx.message.author
        guild = ctx.guild

        _channel = guild.get_channel(913007198488133635)
        channel = guild.get_channel(913540153753092117)
        priv = self.client.get_guild(488623700539736064).get_channel(913590152583077888)
        roles = guild.get_channel(913534684678471732).mention
        suggestions = guild.get_channel(913553966401474650).mention
        faq = guild.get_channel(913595991951835166).mention
        discover = guild.get_channel(913015273538355201).mention

        welcome = discord.utils.get(a.guild.roles, id=913595000363814932).mention
        member = discord.utils.get(a.guild.roles, id=913015562894979082)

        emoji = self.client.get_emoji(id=880532960145719307)
        emoji2 = self.client.get_emoji(id=880532998313885817)

        if m in ctx.guild:
            await ctx.reply(f'{ctx.author.display_name} has just verified {m.display_name}')
            await priv.send(f"{ctx.author.display_name} verified {m.display_name}#{m.discriminator} | UID: {m.id}")

            try:
                await m.add_roles(member)
                print("done")
                # await m.remove_roles(deny)
            except discord.Forbidden:
                await self.client.channel.send("I don't have perms to add roles.")

        if m not in ctx.guild:
            return await ctx.reply(f"Member {m.display_name} is not present in this server.")

        e = discord.Embed(color=random.choice(random_color))
        e.add_field(name=f"New Join!", value=f"Welcome {m.mention}\n\n> Please visit {roles} to get yourself some "
                                             f"roles!\n\n> If you have any question about where a channel is or for, "
                                             f"please visit {discover} and it will direct you.\n\n> If any questions, "
                                             f"please visit {faq} before asking staff since what you may want to ask "
                                             f"could be here.\n\n> If you ever have any suggestions for the server, "
                                             f"please visit {suggestions}!")
        e.set_author(name=ctx.guild, icon_url=ctx.guild.icon_url)

        await _channel.send(f'{emoji}{emoji2}')
        await _channel.send(welcome, embed=e)

        msg = f"You have been verified in {ctx.guild.name}. Please message staff if you have any problems within the " \
              f"server. - \n\n**Owner: {ctx.guild.owner.display_name}**\n**Bot: {self.client.user.display_name}** "

        _e = discord.Embed(name="Accepted!", color=discord.Color.green())
        _e.add_field(name="Congratulations!", value=msg, inline=False)
        _e.add_field(name="Time of acceptance:", value=f"{datetime.datetime.now()}", inline=False)

        try:
            await m.send(embed=_e)
            '''await m.send(f"You have been verified in {ctx.guild.name}. Please message staff if you have any problems "
                         f"within the server. - \n\n**Owner: {ctx.guild.owner.display_name}**\n**Bot: {self.client.user.display_name}**")'''
        except discord.Forbidden:
            await ctx.reply(f"I was unable to alert {m.display_name} that they was accepted.")

    @commands.command(name="deny", pass_context=True)
    @commands.has_role(913552884115853363)
    async def deny(self, ctx, uID: int, *, reason):
        guild = ctx.guild
        channel = guild.get_channel(880218549367492659)
        a = ctx.message.author
        member = discord.utils.get(a.guild.roles, id=864655959753490432)
        deny = discord.utils.get(a.guild.roles, id=904349776659755050)
        priv = self.client.get_guild(488623700539736064).get_channel(913590152583077888)

        m = (self.client.get_user(uID))

        if reason is None:
            await ctx.reply("Please give me the message you want me to send.")

        else:
            _reason = f"Your verification has been denied from {ctx.guild.name} for the following reason:\n\n{reason}"
            print(_reason)

        try:
            await m.send(_reason)
            await ctx.reply(f"I have sent the DM! The reply is followed:\n\n```{_reason}```")
        except discord.Forbidden:
            await ctx.reply(f"I am sadly unable to dm {m.display_name}. The reason cannot be sent.")
            await priv.send(f"{ctx.author.display_name} denied {m.display_name} with following reason:\n\n{reason}")

        '''guild = ctx.guild
        channel = guild.get_channel(880218549367492659)
        a = ctx.message.author
        member = discord.utils.get(a.guild.roles, id=864655959753490432)
        deny = discord.utils.get(a.guild.roles, id=904349776659755050)'''


def setup(client):
    client.add_cog(Utility(client))
