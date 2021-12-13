import discord
import random
import datetime
import asyncio

from discord.ext import commands
from config import random_color


class Staff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="OffenceDatabase")
    @commands.has_role(913019115856359424)
    # async def offencelog(self, ctx, uID: int, *, message):
    async def offencelog(self, ctx):
        g = 913007198488133632
        c = 913736166782681118

        a = ctx.author

        def check(m):
            return m.author.id == a.id

        '''staff_role = 913019115856359424

        if staff_role not in ctx.author.roles:
            return await ctx.reply("You cannot operate this command.")'''

        # m = self.bot.get_user(uID)
        _g = self.bot.get_guild(g)
        _c = self.bot.get_channel(c)

        # reason, action = message.split("|")

        await ctx.reply("Thank you for starting the procedure. This will take place in the DMs, away from the server.")

        await a.send(f"Hello there, {ctx.author.display_name}. May I get the ID of the person?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)

        try:
            uID = int(msg.content)
        except:
            await ctx.message.author.send(
                "That is an invalid ID. \n\nPlease try again or the command will be aborted.")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            try:
                uID = int(msg.content)
            except:
                return await ctx.message.author.send("That is an invalid ID.\n\nThis command has been aborted")

        await a.send(f"Thank you for the ID, {ctx.author.display_name}. Can I have the reason?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check=check)
        _reason = msg.content.lower()

        if _reason == ['no' or 'none']:
            await a.send("There needs to be a reason for this punishment.")

        else:
            await a.send(f"Okay, the reason is `{_reason}`. Is this correct?\n\n**NOTE**:\nThis will always be "
                         f"lowercase due to formatting and checking requirements.")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            confirm = msg.content.lower()

            if confirm == "yes":
                await a.send("Thank you for confirming the reason.")
                reason = _reason
            if confirm == "no":
                await a.send("Okay, I must have it wrong. What reason is it you're giving?")
                await asyncio.sleep(1)
                msg = self.bot.wait_for('message', check=check)
                _reason = msg.content.lower()

                await a.send(f"Okay, the reason that is being submitted is: `{_reason}`")

            await a.send(f"Finally, please can I have what action has been taken against the user?")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check=check)
            action = msg.content

            m = self.bot.get_user(uID)

            embed = discord.Embed(color=random.choice(random_color),
                                  description=f"Log reported on {datetime.date.today()} at {datetime.datetime.utcnow()}{datetime.timezone.utc}")
            embed.add_field(name="Name Of Offender:", value=f"{m.display_name}#{m.discriminator} | {m.mention}",
                            inline=False)
            embed.add_field(name="ID Of Offender:", value=f"{m.id}", inline=False)
            embed.add_field(name="Reason:", value=f"{reason}", inline=False)
            embed.add_field(name="Staff Member Responsible for log:",
                            value=f"Display Name: {ctx.author.display_name} {ctx.author.mention}\nID: {ctx.author.id}")
            embed.add_field(name="Action Taken:", value=action, inline=False)

            embed.set_author(name=_g, icon_url=_g.icon_url)

            await _c.send(embed=embed)


def setup(bot):
    bot.add_cog(Staff(bot))
