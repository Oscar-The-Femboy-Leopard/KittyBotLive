import discord
import random
import asyncio

from discord.ext import commands
from config import random_color


class StaffIntro(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role(913019115856359424)
    async def staffintro(self, ctx):

        channel = self.client.get_guild(913007198488133632).get_channel(913015228508291122)
        guild = self.client.get_guild(913007198488133632)

        if not ctx.message.guild.id == 913007198488133632:
            return

        guidmg = discord.Embed(color=random.choice(random_color))
        guidmg.add_field(name="Thank you for starting the staff intro process!",
                         value=f"_ _", inline=False)

        '''await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs! Please make sure I can DM you for this "
                       f"to work. If it times out, don't worry, you can run this command again. There is also a "
                       f"password you need to find in the Rules. Sadly, this is a required step since the staff "
                       f"don't want trouble makers in the server.")'''

        await ctx.reply(embed=guidmg)

        a = ctx.author

        def check(m):
            return m.author.id == a.id

        await a.send("Firstly, can I get your fursona name or a name you prefer? I will be calling you this through "
                     "the intro.")

        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        name = msg.content
        await a.send(f"Hello, {name}! May I now get your age?")
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
                return await ctx.message.author.send("That is an invalid age.\n\nYour registration has been aborted")
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
                "gender are they? Do they like sleeping all day? Anything!\n\n**Note:**\nIf you don't wish to share "
                "your fursona, tell us some basic info of what you imagine your fursona to be or info about you!")
            await asyncio.sleep(1)
            msg = await self.client.wait_for('message', check=check)
            fursonainfo = msg.content

        if furry != y:
            await a.send(
                f"Okay, {name}, you aren't a furry. That's fine! I will skip all of the fursona questions for you. ^^")
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

        await a.send("Can I have any extra info?")
        await asyncio.sleep(1)
        msg = await self.client.wait_for('message', check=check)
        foundus = msg.content

        embed = discord.Embed(title="New Staff Intro!", color=discord.Color.blue())
        embed.set_thumbnail(url=a.avatar_url)
        embed.add_field(name='Preferred Name', value=f"{name}", inline=False)
        embed.add_field(name='Age Bracket:', value=f"{agebracket}", inline=False)
        embed.add_field(name='Quote', value=f"{quote}", inline=False)
        embed.add_field(name='Gender', value=f"{gender}", inline=False)
        embed.add_field(name='Pronouns', value=f"{pronouns}", inline=False)
        embed.add_field(name='Fursona:', value=f"{fursona}", inline=False)
        embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        embed.add_field(name='Extra Info', value=f"{foundus}", inline=False)
        embed.set_footer(text=f'Author {a.id}')

        await channel.send(f"New Staff Intro!", embed=embed)
        await a.send("Thank you! It has been sent to the server.!")

def setup(client):
    client.add_cog(StaffIntro(client))
