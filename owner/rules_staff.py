import ast
import datetime
import random
import discord

from discord.ext import commands
from config import Owner_ID, random_color, _blnk_value


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

    @commands.command(name='StaffRules', alias="staffrules", hidden=True)
    @commands.is_owner()
    async def staffrules(self, ctx):
        msg = ctx
        guild = 913007198488133632
        color = random.choice(random_color)
        vent = self.bot.get_guild(guild).get_channel(841663659133894667).mention
        spam = self.bot.get_guild(guild).get_channel(913566178033664060).mention
        incidents = self.bot.get_guild(guild).get_channel(913736166782681118).mention

        owner_role = self.bot.get_guild(guild).get_role(913015340122914816).mention
        co_owner_role = self.bot.get_guild(guild).get_role(913023600716578826).mention
        w1 = self.bot.get_guild(guild).get_role(913571050590203924).mention
        w2 = self.bot.get_guild(guild).get_role(913571220606316625).mention
        muted = self.bot.get_guild(guild).get_role(913016747664220190).mention

        tos = 'https://discord.com/terms'
        guidelines = 'https://discord.com/guidelines'

        ban_and_kick = f"**DO NOT** ban or kick people just because you don't like the individual. That is considered " \
                       f"very unfair and gives the staff and server a very bad name. **ONLY** ban without " \
                       f"warning if a {co_owner_role} or the {owner_role} tells you that it's appropriate. The only " \
                       f"time that doesn't apply is when someone goes through the warning roles and/or are trolls.\n "

        spam = f"**DO NOT** spam in chat. This rule is applied to staff as well. We got to lead by example and if " \
               f"someone is spamming outside of {spam}, please redirect them there. "

        venting = f"If someone is venting outside of {vent}, please redirect them there. If they don't listen and " \
                  f"continue to vent outside of {vent}, follow the warning precedures with the roles. "

        warnings = f"These roles should be given if people consistently and/or purposely break the rules. The " \
                   f"individual should receive {muted} and receive the {w1} role. If they don't stop, assign {w2} and " \
                   f"{muted}. The {w1} and {w2} should be there for a month when they've been good but won't be " \
                   f"removed after 1 month if they've not behaved with the {muted} being given for an hour for {w1} " \
                   f"and 6 hours for {w2}. The 3rd strike should not be hinted and before going through with it, " \
                   f"try to get the member to behave as banning should be **A LAST RESORT!**"
        warnings2 = f"{w1} can be removed through good behaviour by any staff member, Mod and higher. " \
                    f"Only {w2} can be removed by {owner_role} and {co_owner_role}. If someone is found to be sucking " \
                    f"up to any staff, go through the warnings with them. Also, log any warnings/incidents in " \
                    f"{incidents}. for ease of access and possibly for cases to do with more serious matters down the " \
                    f"line, if it ever comes to that."

        nsfw = f"If someone is posting NSFW, please warn them. It isn't tolerated as there is members here that don't " \
               f"want to see it. "

        cred = f"Please keep an eye on these rules as you are in the chat. If staff is seen breaking the rules " \
               f"themselves, they could face demotion or even banned. "

        guild = self.bot.get_guild(841496169556475975)

        rules = discord.Embed(color=color)
        rules.add_field(name="Staff Guidelines in This server:", value=f"These rules are here as a basis to let the "
                                                                       f"staff "
                                                                       f"know what is expected of them by {owner_role}. If you catch any "
                                                                       f"staff breaking the rules, please contact {owner_role} or {co_owner_role} "
                                                                       f"immediately and privately!", inline=False)
        rules.set_footer(text="\n\nThey are as follows:", icon_url=guild.icon_url)

        ban = discord.Embed(color=color)
        ban.add_field(name="Banning And Kicking Policies", value=f"{ban_and_kick}", inline=False)
        ban.set_footer(text="These guidelines regarding kicking and banning is monitored strictly by the owner. "
                            "Strictly no banning unless there's evidence of the rule breaking.",
                       icon_url=guild.icon_url)

        spamm = discord.Embed(color=color)
        spamm.add_field(name="Spam Policies", value=f"{spam}", inline=False)
        spamm.set_footer(text="This is here to keep spam out of main channels. Please use these guidelines with "
                              "dealing with spam", icon_url=guild.icon_url)

        venti = discord.Embed(color=color)
        venti.add_field(name="Venting Policies", value=f"{venting}", inline=False)
        venti.set_footer(text="Please use logic when dealing with the venting chat. We don't want people to feel "
                              "unsafe in our server. Every staff member in this server is responsible for the well "
                              "being of the members", icon_url=guild.icon_url)

        warning = discord.Embed(color=color)
        warning.add_field(name="Warning Policy", value=warnings, inline=False)
        warning.add_field(name="PLEASE NOTE", value=warnings2, inline=False)
        warning.set_footer(text="Please follow the guidelines for this. It is a must that it is treated properly.", icon_url=guild.icon_url)

        _nsfw = discord.Embed(color=color)
        _nsfw.add_field(name="NSFW Policy", value=f"{nsfw}", inline=False)
        _nsfw.set_footer(text="This is a very strict policy... This is because we want everyone to feel safe and "
                              "secure. Plus, there's a good chance that minors would get into this server.")

        revised = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        revised.add_field(name="Staff Rule Breakers", value=f"{cred}\n\n", inline=False)
        revised.add_field(name=f"{_blnk_value}", value=f"Please remember that we follow Discord's [TOS]({tos}) and [Guidelines]({guidelines})", inline=False)
        revised.add_field(name=f"These rules where revised by:",
                          value=f"{owner_role} on:\n\n{datetime.date.today()}", inline=False)

        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).purge(limit=10)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=rules)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=ban)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=spamm)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=warning)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=_nsfw)
        await self.bot.get_guild(913007198488133632).get_channel(913019586876694528).send(embed=revised)
        await ctx.send("Sent the staff rules.")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
