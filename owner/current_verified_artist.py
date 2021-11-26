import ast
import asyncio
import datetime
import random
import discord

from discord.ext import commands, tasks
from config import Owner_ID, random_color


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.guild = None
        self.author = Owner_ID
        self.bot = bot

    '''async def loop(self, member):
        guild = 841496169556475975
        verified = 855406836463173653
        _verified = self.bot.get_guild(guild).get_role(verified)
        _role = _verified
        # Role = role
        mem = discord.Role.members
        print(mem)
        member = _role.members
        while True:
            member
            
            await asyncio.sleep(1)'''

    @commands.command(name='current_verify_artist', alias="CVA", hidden=True, pass_context=True)
    @commands.is_owner()
    async def currentverifiedartist(self, ctx):
        guild = 841496169556475975
        channel = 880919156025860117
        verified = 855406836463173653

        # save = discord.Guild.

        staff_role = self.bot.get_guild(guild).get_role(841497322138632222).mention
        verified_artist_role = self.bot.get_guild(guild).get_role(verified).mention

        color = random.choice(random_color)

        _guild = self.bot.get_guild(guild)

        img = "https://media.discordapp.net/attachments/880852778124206180/880959182822588456/Verified_Artist.png"

        # impInfo = f"{_guild.get_role(855406836463173653).fetch_members}"
        impInfo = f"*There is currently no verified artists here.*"

        _verified = self.bot.get_guild(guild).get_role(verified)
        _role = _verified
        r = _role.members
        print(r)

        image = discord.Embed(timestamp=datetime.datetime.utcnow(), color=color)
        image.set_image(url=img)

        imp = discord.Embed(color=random.choice(random_color))
        if len(_role.members) == 0:
            print("No valid Users With This Role.")
            _var = impInfo
            imp.add_field(name="No current Verified Artists", value="_ _", inline=False)
        var = ""
        if len(_role.members) > 0:
            for member in _role.members:
                # var = var + f"\n {member.mention}"
                var = f"\n {member.mention}"
        imp.add_field(name="Current Verified Artists are:", value=var, inline=False)
        # imp.add_field(name="Current Verified Artists are:", value=var)
        imp.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)

        revised = discord.Embed(color=random.choice(random_color), timestamp=datetime.datetime.utcnow())
        revised.add_field(name=f"The verified artists was  by:",
                          value=f"{_guild.name}'s {staff_role} on:\n\n{datetime.date.today()}")

        await self.bot.get_channel(channel).purge(limit=10)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=image)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=imp)
        # await self.bot.get_guild(guild).get_channel(channel).send(embed=revised)
        await ctx.send("Sent the Verified Art Rules.")

    @commands.command(name="updateCVA", pass_context=True)
    @commands.has_role("OWNER")
    async def updateCVA(self, ctx):
        verified = 855406836463173653
        _guild = self.bot.get_guild(841496169556475975)
        _chan = _guild.get_channel(880919156025860117)

        _role = _guild.get_role(855406836463173653)
        # _guild = self.bot.get_guild(guild)

        _verified = _guild.get_role(verified)
        _role = _verified
        r = _role.members
        impInfo = f"*There is currently no verified artists here.*"

        imp = discord.Embed(color=random.choice(random_color))
        if len(_role.members) == 0:
            print("No valid Users With This Role.")
            _var = impInfo
            imp.add_field(name="No current Verified Artists", value="_ _", inline=False)
        var = ""
        for member in _role.members:
            var = var + f"\n {member.mention}"
        imp.add_field(name="Current Verified Artists are:", value=var, inline=False)

        update = discord.Embed(color=random.choice(random_color))
        update.add_field(name="Current Verified Artists are:", value=var)
        update.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)
        await _chan.message.edit(imp, embed=update)

    '''@commands.command(name="updateCVA")
    @commands.has_role("Staff")
    async def updateCVA(self, ctx):
        guild = self.bot.get_guild(841496169556475975)
        channel = self.bot.get_channel(880919156025860117)
        _role = guild.get_role(855406836463173653)

        r = _role.members
        impInfo = f"*There is currently no verified artists here.*"

        imp = discord.Embed(color=random.choice(random_color))
        if len(_role.members) == 0:
            print("No valid Users With This Role.")
            var = impInfo
            imp.add_field(name="Current Verified Artists are:", value=var, inline=False)
        var = ""
        for member in _role.members:
            var = var + f"\n {member.mention}"
        imp.add_field(name="Current Verified Artists are:", value=var, inline=False)
        # imp.add_field(name="Current Verified Artists are:", value=var)
        imp.set_footer(text=ctx.author.display_name, icon_url=guild.icon_url)

        await self.bot.get_guild(841496169556475975).get_channel(880919156025860117).purge(limit=1)
        await self.bot.get_guild(841496169556475975).get_channel(880919156025860117).send(embed=imp)'''




    '''await self.bot.get_guild(guild).get_channel(channel).purge(limit=10)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=image)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=imp)
        await self.bot.get_guild(guild).get_channel(channel).send(embed=revised)
        await ctx.send("Sent the Verified Art Rules.")'''

    '''while True:
            m = discord.guild.Role.members
            imp.add_field(name="Current Verified Artists are:", value=f"{m}")
            await self.bot.get_guild(guild).get_channel(channel).edit(embed=imp)'''

    '''@commands.Cog.listener()
    async def update(self, ctx):
        _guild = self.bot.get_guild(841496169556475975)
        verified = _guild.get_role(855406836463173653)
        guild = 841496169556475975
        _role = verified
        # Role = role
        mem = discord.Role.members
        print(mem)
        r = _role.members
        print(r)

        if discord.member in r:
            val = "{}".format(_guild.member.mention)

            new_imp = discord.Embed(color=random.choice(random_color))
            new_imp.add_field(name="Current verified artists are:", value=val, inline=False)
            new_imp.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)

            imp = discord.Embed(color=random.choice(random_color))
            imp.add_field(name="Current verified artists are:", value=val, inline=False)
            imp.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)

            counter = 0
            channel = self.bot.get_channel(835656871376453673)  # channel ID goes here
            _channel = self.bot.get_channel(775770598844137482)
            while not self.bot.is_closed():

                # await self.bot.get_guild(guild).get_channel(channel).purge(limit=10)
                # await self.bot.get_guild(guild).get_channel(channel).send(embed=image)
                msg = await self.bot.get_guild(guild).get_channel(channel).send(embed=imp)
                # await self.bot.get_guild(guild).get_channel(channel).send(embed=revised)
                # await ctx.send("Sent the Verified Art Rules.")

                counter += 1
                await channel.send(counter)
                await asyncio.sleep(60)  # task runs every 60 seconds
                await _channel.send("Updated.")

                # edit the embed of the message
                await msg.edit(embed=new_imp)
                # await self.bot.get_guild(guild).get_channel(channel).send(embed=revised)'''



    '''@commands.command()
    async def cva_update(self, ctx, member: discord.Member = None):
        verified = 855406836463173653
        guild = 841496169556475975

        first_embed = Embed(title='embed 1')
        new_embed = Embed(title='embed 2')

        # send a first message with an embed
        msg = await ctx.send(embed=first_embed)

        # edit the embed of the message
        await msg.edit(embed=new_embed)'''



    '''@commands.command()
    async def cva_update(self, ctx, member: discord.Member = None):

        # roles = [role for role in member.roles]

        guild = 841496169556475975
        channel = 880919156025860117
        verified = 855406836463173653

        role = self.bot.get_guild(guild).get_role(verified)
        _guild = self.bot.get_guild(guild)
        r_member = None

        impInfo = ""

        imp = discord.Embed(color=random.choice(random_color))
        imp.add_field(name="Current verified artists are:", value=impInfo, inline=False)
        imp.set_footer(text=ctx.author.display_name, icon_url=_guild.icon_url)

        if _guild.get_member.roles.has(verified):

            embed_to_dict = imp.todict()

            for field in embed_to_dict:
                if field["name"] == "Current verified artists are:":
                    field["value"] += member.mention

            imp = discord.Embed.from_dict(embed_to_dict)
            await ctx.edit(embed=imp)'''
    '''@commands.Cog.listener()
    async def on_verified_artist_role_add(self, payload):
        guild = 841496169556475975
        channel = 880919156025860117
        verified = 855406836463173653
        _message = 880965617279201331

        if payload == self.bot:
            return
        channel = self.bot.get_channel(payload.channel)
        message = await channel.fetch_message(payload.message)
        imp, roles = message.embeds[0], [verified]
        index = roles.index(payload.role.name)

        imp.set_field_at(index, name=imp.fields[index].name, value=payload.member.mention, inline=False)
        await message.edit(embed=imp)'''


def setup(bot):
    bot.add_cog(OwnerCog(bot))
