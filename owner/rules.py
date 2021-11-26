import ast
import datetime
import random
import discord
import os

from discord.ext import commands
from config import Owner_ID, random_color

_password = 'licking leopards'


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.guild = None
        self.author = Owner_ID
        self.bot = bot

    @commands.command(name='Rules', alias="rules", hidden=True)
    @commands.is_owner()
    async def rules(self, ctx):

        guild = 913007198488133632
        vent = self.bot.get_guild(guild).get_channel(913564201639874571).mention
        ticket = self.bot.get_guild(guild).get_channel(913571656855847012).mention
        spam = self.bot.get_guild(guild).get_channel(913566178033664060).mention
        staff_role = self.bot.get_guild(guild).get_role(913019115856359424).mention
        owner_role = self.bot.get_guild(guild).get_role(913015340122914816).mention
        co_owner_role = self.bot.get_guild(guild).get_role(913023600716578826).mention
        w1 = self.bot.get_guild(guild).get_role(913571050590203924).mention  # '<@752631938505769070>'
        w2 = self.bot.get_guild(guild).get_role(913571220606316625).mention  # '<@752631938505769069>'
        tos = 'https://discord.com/terms'
        guidelines = 'https://discord.com/guidelines'
        colors = random.choice(random_color)

        img = 'https://media.discordapp.net/attachments/880852778124206180/913572435515834398/Rules.gif'
        img = img

        genRule = f"**NO** disrespecful behaviour towards anyone in any way. This isn't the best " \
                  f"of ideas as we all want a community where we feel safe and secure. This also means no drama of " \
                  f"any kind. This will lead to punishments, below.\nPlease no political or religious discussions as " \
                  f"it can tear the community apart, ruining everything we want.\nWe do also follow Discord's TOS " \
                  f"found [here]({tos}) and guidelines found [here]({guidelines}). "

        NSFW = f"**STRICTLY NO** NSFW content. Use of this kind of content **WILL** result in you having warnings or " \
               f"possibly a kick/ban, depending on how severe the content is. Password is: {_password}"

        warnings = f"There is a warning system in this server. This is how the warnings go: \n\n > 1st Warning: You " \
                   f"will receive a mute and the {w1} Role. \n\n > 2nd warning: Staff will keep a strict eye on you. " \
                   f"Same goes for warning 1; you're getting muted and given {w2} role as well. \n\n > There is no " \
                   f"3rd warning. If you continue to break the rules, you **WILL** be banned without warning. \n\n " \
                   f"*Please note, {w1} can be removed through good behaviour by any staff member, Mod and up, " \
                   f"and only {w2} can be removed by {owner_role} and {co_owner_role}. If you are found to be sucking " \
                   f"up to either staff, this can lead you to be banned.* "

        venting = f"There is **NO TOLERANCE** for promoting suicide or self harm of any kind. If you need to just " \
                  f"vent, visit {vent} as it is the appropriate channel for it. If you believe that someone is going " \
                  f"to commit suicide, call your country's suicide hotline. "

        spam = f"Under any circumstances, do not spam in any channels except {spam}. We all want channels that aren't " \
               f"clogged with random messages as this is very disrupting to conversations and also can be seen as " \
               f"disrespectful to other members and staff."

        guild = self.bot.get_guild(913007198488133632)

        image = discord.Embed(timestamp=datetime.datetime.utcnow(), color=colors)
        image.set_image(url=img)

        rules = discord.Embed(description=f"{guild.name}'s Rules!", color=colors)
        rules.add_field(name="General Rules:", value=genRule, inline=False)
        rules.set_footer(text=ctx.author.display_name, icon_url=guild.icon_url)

        nsfw = discord.Embed(color=colors)
        nsfw.add_field(name="NSFW Rules", value=NSFW, inline=False)
        nsfw.set_footer(text="This can change if the server ever implement NSFW channels.", icon_url=guild.icon_url)

        warning = discord.Embed(color=colors)
        warning.add_field(name="Server Warnings", value=warnings, inline=False)
        warning.set_footer(text=f"These are given at the Staff's digression", icon_url=guild.icon_url)

        vents = discord.Embed(color=colors)
        vents.add_field(name="Venting in this server", value=venting, inline=False)
        vents.set_footer(text="These are very strict rules about this to safeguard us all.", icon_url=guild.icon_url)

        spamm = discord.Embed(color=colors)
        spamm.add_field(name="Spam Rules", value=spam, inline=False)
        spamm.add_field(name="_ _",
                        value=f"**IF YOU HAVE ANY TROUBLES/QUESTIONS, PLEASE DM ONE OF THE {staff_role} OR CREATE A "
                              f"TICKET HERE {ticket}! If it's serious, reach out to {owner_role} or {co_owner_role} "
                              f"directly!**")
        spamm.set_footer(text="These rules are guidelines for the server, and the staff can alter them to their "
                              "digression.", icon_url=guild.icon_url)

        revised = discord.Embed(color=colors, timestamp=datetime.datetime.utcnow())
        revised.add_field(name=f"These rules where revised by:",
                          value=f"{guild.name}'s {staff_role} on:\n\n{datetime.date.today()}")

        await guild.get_channel(913038295255093249).purge(limit=10)
        await guild.get_channel(913038295255093249).send(embed=image)
        await guild.get_channel(913038295255093249).send(embed=rules)
        await guild.get_channel(913038295255093249).send(embed=nsfw)
        await guild.get_channel(913038295255093249).send(embed=warning)
        await guild.get_channel(913038295255093249).send(embed=vents)
        await guild.get_channel(913038295255093249).send(embed=spamm)
        await guild.get_channel(913038295255093249).send(embed=revised)
        await ctx.send("Sent the normal rules.")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
