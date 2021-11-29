import ast
import asyncio
import datetime
import random
import discord
import os

from discord.ext import commands
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

    @commands.command(name='directory', alias="Directory", hidden=True)
    @commands.is_owner()
    async def directory(self, ctx):
        g = 913007198488133632

        staff_role = self.bot.get_guild(g).get_role(913019115856359424).mention
        verified_artist_role = self.bot.get_guild(g).get_role(913032815954755584).mention

        # UNCATEGORIZED
        rules = self.bot.get_guild(g).get_channel(913038295255093249).mention
        faq = self.bot.get_guild(g).get_channel(913595991951835166).mention

        # INTRODUCTIONS/INFORMATION
        announcements = self.bot.get_guild(g).get_channel(913040579926044713).mention
        staff_intro = self.bot.get_guild(g).get_channel(913015228508291122).mention
        roles = self.bot.get_guild(g).get_channel(913534684678471732).mention
        changelog = self.bot.get_guild(g).get_channel(913597776183578634).mention
        suggestions = self.bot.get_guild(g).get_channel(913553966401474650).mention

        # PARTNERS
        partner_requirements = self.bot.get_guild(g).get_channel(913038686969548810).mention
        current_partners = self.bot.get_guild(g).get_channel(913038759606509568).mention

        # MAIN ROOMS
        general_chat = self.bot.get_guild(g).get_channel(913007198488133635).mention
        general_rp = self.bot.get_guild(g).get_channel(914618169052774410).mention
        irl_pics = self.bot.get_guild(g).get_channel(913030009537585172).mention
        animals_and_pets = self.bot.get_guild(g).get_channel(913030038453116940).mention
        memes = self.bot.get_guild(g).get_channel(913032300470632448).mention
        spam = self.bot.get_guild(g).get_channel(913566178033664060).mention

        # ART ROOMS
        art_tips = self.bot.get_guild(g).get_channel(913604304005378179).mention
        traditional = self.bot.get_guild(g).get_channel(913032994527264808).mention
        digital = self.bot.get_guild(g).get_channel(913033016144691220).mention
        original_music = self.bot.get_guild(g).get_channel(913598391794167819).mention

        # VOICE ROOMS
        hydra_song_requests = self.bot.get_guild(g).get_channel(913034632335855617).mention
        music_text_channel = self.bot.get_guild(g).get_channel(913605992997081168).mention
        no_mic_chat = self.bot.get_guild(g).get_channel(913034247261003799).mention

        # GAME ROOMS
        self_promotion = self.bot.get_guild(g).get_channel(913030255776768060).mention
        gaming_clips = self.bot.get_guild(g).get_channel(913029918772834324).mention
        gaming_chat = self.bot.get_guild(g).get_channel(913030294079156254).mention
        no_mic_chat_ = self.bot.get_guild(g).get_channel(913030404439670836).mention

        # Thinking Corner
        question_of_the_day = self.bot.get_guild(g).get_channel(913031444098592818).mention
        answers = self.bot.get_guild(g).get_channel(913031493515898920).mention
        dailypoll = self.bot.get_guild(g).get_channel(913623473409122324).mention
        polldis = self.bot.get_guild(g).get_channel(913623496632987689).mention

        # BOT AREA
        general_commands = self.bot.get_guild(g).get_channel(913032430930239548).mention
        bump = self.bot.get_guild(g).get_channel(913554518808096798).mention
        currency_log = self.bot.get_guild(g).get_channel(913032459946430514).mention
        tickets = self.bot.get_guild(g).get_channel(913571656855847012).mention

        resources = self.bot.get_guild(g).get_channel(913564182346092635).mention
        vent = self.bot.get_guild(g).get_channel(913564201639874571).mention

        color = random.choice(random_color)
        _color = random.choice(random_color)
        __color = random.choice(random_color)
        ___color = random.choice(random_color)
        ____color = random.choice(random_color)
        _____color = random.choice(random_color)
        ______color = random.choice(random_color)
        _______color = random.choice(random_color)
        ________color = random.choice(random_color)

        guild = self.bot.get_guild(g)

        img = "https://media.discordapp.net/attachments/880852778124206180/913601573689651260/Directory.gif"

        uncat = f"{rules} - This is self explanatory. This channel is for the server rules.\n\n{faq} - This is for " \
                f"the frequently asked questions about the server. If you believe we have missed some, please contact " \
                f"a staff member immediately. Thank you."

        intro = f"{announcements} - This channel is for any announcements this server will have. Important ones will " \
                f"be pinged by the mention role.\n\n{staff_intro} - Look here to get to know the staff! There will be " \
                f"some basic information here for you to get to know them better.\n\n{roles} - Go here to get " \
                f"yourself some reaction roles! They allow some cool customisation, and if you have some suggestions, " \
                f"don't gorget to leave them in {suggestions}.\n\n{changelog} - This channel is designed for members " \
                f"to see what has changed at a glance.\n\n{suggestions} - This channel is self explanatory. If " \
                f"there's anything out there that could improve this server, please suggest them here!"

        partner = f"{partner_requirements} - This is the information about how you go about becoming a partner of the " \
                  f"server.\n\n{current_partners} - This is the channel you visit to get the list of active " \
                  f"partnerships! "

        text_channels = f"{general_chat} - This chat is for the usual talking with other members. However, " \
                        f"it is still a SFW channel.\n\n{general_rp} - This chat is designed for Tupperbox and all of " \
                        f"your small RP needs!\n\n{irl_pics} - This channel is for posting any IRL media, just " \
                        f"make sure it is SFW content.\n\n{animals_and_pets} - This channel is designed for you to " \
                        f"share any cute pictures of pets or animals alike!\n\n{memes} - This is just dedicated for " \
                        f"memes. Every server needs a meme channel.\n\n{spam} - This channel is for all of your " \
                        f"spamming needs. Spam how much here you desire without any limitation of how much you send. "

        art = f"{art_tips} - This channel is all about artists giving tips along with aspiring artists asking for " \
              f"tips. Just remember to be fair with each other.\n\n{traditional} - Like digital, but only for " \
              f"traditional art instead of digital.\n\n{digital} - This is the channel where people can show any " \
              f"digital art they made/commissioned.\n\n{original_music} - This is for whatever music you compose " \
              f"yourself! Please don't be shy or don't hate. "

        vc = f"{hydra_song_requests} - This channel is for requesting songs for the music bot to play.\n\n" \
             f"{music_text_channel} - This channel is designed to allow people who are listening to music to also " \
             f"talk, because the music VC is muted by default.\n\n{no_mic_chat} - This chat is designed for people " \
             f"who are in the normal VC to chat without having to use a mic. This channel is also role locked, " \
             f"which the role is temporarily given by joining the general vc."

        gaming = f"{self_promotion} - This channel is designed for you to promote your Youtube channel along with " \
                 f"your twitch!.\n\n{gaming_clips} - This channel is designed for people who just want to share short" \
                 f" clips of gameplay or screenshot(s).\n\n{no_mic_chat_} - This text channel is also role locked. " \
                 f"Like the music and VC roles, you need to join the appropriate vc to be able to access."

        qotd = f"{question_of_the_day} - This channel is where you will find the Question Of The Day!\n\n{answers} - " \
               f"If you wish to partake in the QOTD, please put your answer(s) in here.\n\n{dailypoll} - In here, I " \
               f"will do a poll daily, for you guys to vote.\n\n{polldis} - This is for the discussion of the daily " \
               f"poll! "

        botarea = f"{general_commands} - This is where you can find where you would use the normal day to day " \
                  f"commands.\n\n{bump} - This is the channel to bump the server using disboard!\n\n{currency_log} - " \
                  f"This is the channel for the currency to be logged, just in case people where curious. It might " \
                  f"get rather spammed so it wouldn't cause too much damage if you muted it.\n\n{tickets} - This is " \
                  f"the channel you use if you want to open a ticket for any problems you may have with a server " \
                  f"member or want to ask staff something in private without actively DMing the staff member. "

        infirmary = f"{resources} - This is the numbers for suicide helplines in several countries. If we missed " \
                    f"any, go to {suggestions} or message a staff member.\n\n{vent} - This is currently the only " \
                    f"general venting channel. Please keep within the rules to safeguard everyone's safety."

        image = discord.Embed(timestamp=datetime.datetime.utcnow(), color=color)
        image.set_image(url=img)

        imp = discord.Embed(color=_color)
        imp.add_field(name="Directory: Very Important Info", value=uncat, inline=False)
        imp.set_footer(text=ctx.author.display_name, icon_url=guild.icon_url)

        info = discord.Embed(color=random.choice(random_color))
        info.add_field(name="Directory: Important Formation, not too important", value=intro, inline=False)
        info.set_footer(text=ctx.author.display_name, icon_url=guild.icon_url)

        _partner = discord.Embed(color=__color)
        _partner.add_field(name="Directory: Partners", value=partner, inline=False)
        # _partner.set_footer(text="This can change if the server ever implement NSFW channels.", icon_url=guild.icon_url)

        text = discord.Embed(color=___color)
        text.add_field(name="Directory: Main Rooms", value=text_channels, inline=False)
        # warning.set_footer(text=f"These are given at the Staff's digression", icon_url=guild.icon_url)

        Art = discord.Embed(color=_______color)
        Art.add_field(name="Discovery: Art Rooms", value=art, inline=False)

        VC = discord.Embed(color=______color)
        VC.add_field(name="Discovery: Voice Channels", value=vc, inline=False)

        vents = discord.Embed(color=____color)
        vents.add_field(name="Discovery: Gaming Room", value=gaming, inline=False)
        # vents.set_footer(text="These are very strict rules about this to safeguard us all.", icon_url=guild.icon_url)

        Ticket = discord.Embed(color=_____color)
        Ticket.add_field(name="Discovery: Thinking Corner", value=qotd, inline=False)
        Ticket.set_footer(text="Please remember that these are for fun, and shouldn't cause arguments.")

        _botarea = discord.Embed(color=random.choice(random_color))
        _botarea.add_field(name="Discovery: Bot Area", value=botarea, inline=False)

        infirm = discord.Embed(color=_______color)
        infirm.add_field(name="Directory: Infirmary", value=infirmary, inline=False)

        revised = discord.Embed(color=________color, timestamp=datetime.datetime.utcnow())
        revised.add_field(name=f"The discovery was updated on:", value=f"{datetime.date.today()}")

        await guild.get_channel(913015273538355201).purge(limit=15)
        await guild.get_channel(913015273538355201).send(embed=image)
        await guild.get_channel(913015273538355201).send(embed=imp)
        await guild.get_channel(913015273538355201).send(embed=info)
        await guild.get_channel(913015273538355201).send(embed=_partner)
        await guild.get_channel(913015273538355201).send(embed=text)
        await guild.get_channel(913015273538355201).send(embed=Art)
        await guild.get_channel(913015273538355201).send(embed=VC)
        await guild.get_channel(913015273538355201).send(embed=vents)
        await guild.get_channel(913015273538355201).send(embed=Ticket)
        await guild.get_channel(913015273538355201).send(embed=_botarea)
        await guild.get_channel(913015273538355201).send(embed=infirm)
        await guild.get_channel(913015273538355201).send(embed=revised)
        await ctx.send("Sent the directory.")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
