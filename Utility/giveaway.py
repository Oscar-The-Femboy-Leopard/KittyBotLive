'''import discord
import asyncio
import datetime

from random import choice
from discord.ext import commands
from config import random_color


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, time):
        pos = ["s", "m", "h", "d"]

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    # @commands.has_permissions(kick_members=True)
    async def giveaway(self, ctx):
        await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

        questions = ["Which channel should it be hosted in?", "What should be the duration of the giveaway? (s|m|h|d)",
                     "What is the prize of the giveaway?"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.bot.wait_for('messsage', timeout=15.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send('You didn\'t answer in time, please be quicker next time!')
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
            return

        channel = self.bot.get_channel(c_id)

        # time = convert(answers[1])
        time = int(answers[1])
        if time == -1:
            return await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")

        elif time == -2:
            return await ctx.send(f"The time just be an integer. Please enter an integer next time.")

        prize = answers[2]

        await ctx.send(f"The giveaway will be in {channel.mention} and will last {answers[1]} seconds!")

        embed = discord.Embed(title="Giveaway!", description=f"{prize}", color=choice(random_color))

        embed.add_field(name="Hosted by:", value=ctx.author.mention)

        embed.set_footer(text=f"Ends {answers[1]} from now!")

        my_msg = await channel.send(embed=embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = choice(users)

        await channel.send(f"Congratulations! {winner.mention} won the prize: {prize}!")

    @commands.command()
    # @commands.has_permissions(kick_members=True)
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            return await ctx.send(
                "The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = choice(users)

        await channel.send(f"Congratulations the new winner is: {winner.mention} for the giveaway rerolled!")


def setup(bot):
    bot.add_cog(Giveaway(bot))
'''


'''import discord
from discord.ext import commands
import asyncio
import random
import datetime


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # @commands.has_role("Giveaway Host")
    async def giveaway(self, ctx):
        # Giveaway command requires the user to have a "Giveaway Host" role to function properly

        # Stores the questions that the bot will ask the user to answer in the channel that the command was made
        # Stores the answers for those questions in a different list
        giveaway_questions = ['Which channel will I host the giveaway in?', 'What is the prize?',
                              'How long should the giveaway run for (in seconds)?', ]
        giveaway_answers = []

        # Checking to be sure the author is the one who answered and in which channel
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        # Askes the questions from the giveaway_questions list 1 by 1
        # Times out if the host doesn't answer within 30 seconds
        for question in giveaway_questions:
            await ctx.send(question)
            try:
                message = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send(
                    'You didn\'t answer in time.  Please try again and be sure to send your answer within 30 seconds of the question.')
                return
            else:
                giveaway_answers.append(message.content)

        # Grabbing the channel id from the giveaway_questions list and formatting is properly
        # Displays an exception message if the host fails to mention the channel correctly
        try:
            c_id = int(giveaway_answers[0][2:-1])
        except:
            await ctx.send(f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')
            return

        # Storing the variables needed to run the rest of the commands
        channel = self.bot.get_channel(c_id)
        prize = str(giveaway_answers[1])
        time = int(giveaway_answers[2])

        # Sends a message to let the host know that the giveaway was started properly
        await ctx.send(
            f'The giveaway for {prize} will begin shortly.\nPlease direct your attention to {channel.mention}, this giveaway will end in {time} seconds.')

        # Giveaway embed message
        give = discord.Embed(color=0x2ecc71)
        give.set_author(name=f'GIVEAWAY TIME!', icon_url='https://i.imgur.com/VaX0pfM.png')
        give.add_field(name=f'{ctx.author.name} is giving away: {prize}!',
                       value=f'React with 🎉 to enter!\n Ends in {round(time / 60, 2)} minutes!', inline=False)
        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        give.set_footer(text=f'Giveaway ends at {end} UTC!')
        my_message = await channel.send(embed=give)

        # Reacts to the message
        await my_message.add_reaction("🎉")
        await asyncio.sleep(time)

        new_message = await channel.fetch_message(my_message.id)

        # Picks a winner
        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)

        # Announces the winner
        winning_announcement = discord.Embed(color=0xff2424)
        winning_announcement.set_author(name=f'THE GIVEAWAY HAS ENDED!', icon_url='https://i.imgur.com/DDric14.png')
        winning_announcement.add_field(name=f'🎉 Prize: {prize}',
                                       value=f'🥳 **Winner**: {winner.mention}\n 🎫 **Number of Entrants**: {len(users)}',
                                       inline=False)
        winning_announcement.set_footer(text='Thank you everyone for entering!')
        # await channel.send(embed=winning_announcement)
        await my_message.edit(content="GIVEAWAY ENDED", embed=winning_announcement)
        await channel.send(f"{winner.mention} Please message a staff about your reward!")

    @commands.command()
    # @commands.has_role("Giveaway Host")
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        # Reroll command requires the user to have a "Giveaway Host" role to function properly
        try:
            new_message = await channel.fetch_message(id_)
        except:
            await ctx.send("Incorrect id.")
            return

        # Picks a new winner
        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)

        # Announces the new winner to the server
        reroll_announcement = discord.Embed(color=0xff2424)
        reroll_announcement.set_author(name=f'The giveaway was re-rolled by the host!',
                                       icon_url='https://i.imgur.com/DDric14.png')
        reroll_announcement.add_field(name=f'🥳 New Winner:', value=f'{winner.mention}', inline=False)
        await channel.send(embed=reroll_announcement)


def setup(bot):
    bot.add_cog(Giveaway(bot))
'''


import discord
import asyncio

from discord.ext import commands
from random import choice


class Giveaway(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def convert(self, time):
        pos = ["s", "m", "h", "d"]

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    @commands.guild_only()
    async def gstart(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        giveaway_questions = ['Which channel will I host the giveaway in?', 'What is the prize?',
                              'How long should the giveaway run for?', ]
        giveaway_answers = []

        for question in giveaway_questions:
            await ctx.send(question)
            try:
                message = await self.bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.send(
                    'You haven\'t answered in time.  Please try again and be sure to send your answer within 30 seconds of the question.')
            else:
                giveaway_answers.append(message.content)

            # Grabbing the channel id from the giveaway_questions list and formatting is properly
            # Displays an exception message if the host fails to mention the channel correctly
        try:
            c_id = int(giveaway_answers[0][2:-1])
        except:
            return await ctx.send(
                f'You failed to mention the channel correctly.  Please do it like this: {ctx.channel.mention}')

        '''await ctx.send("This command times out after 15 seconds on each point.\nWhat is the duration of this giveaway?")
        await asyncio.sleep(1)
        try:
            duration = await self.bot.wait_for('message', timeout=15.0, check=check())
        except asyncio.TimeoutError:
            return await ctx.send("Command has timed out.")
        
        await ctx.send("Okay, what is the prize going to be?")
        await asyncio.sleep(1)
        try:
            prize = await self.bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Command has timed out.")
        
        await ctx.send("What channel is it going to be hosted/displayed in?")
        await asyncio.sleep(1)
        try:
            channel = await self.bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.send("Command has timed out.")'''

        duration = giveaway_answers[2]
        prize = giveaway_answers[1]
        c = self.bot.get_channel(c_id)

        time = self.convert(duration)
        if time == -1:
            return await ctx.send(f'Answer Time With A Proper Unit (s, m, h, d)')
        elif time == -2:
            return await ctx.send(f'Time Must Be A Integer!')

        giveaway = discord.Embed(
            title="🎉 New Giveaway! 🎉",
            description=f"**Prize:** {prize}\n"
                        f"**Hosted By:** {ctx.author.mention}\n",
                        # f"**Ends In:** {time} Seconds",
            colour=discord.Color.green()
        )
        giveaway.insert_field_at(index=1, name="**Ends In:**", value=f"{time}")

        my_msg = await c.send(embed=giveaway)

        reactions = await my_msg.add_reaction("🎉")

        while time >= 0:

            if time <= 60:
                giveaway.remove_field(index=1)
                giveaway.insert_field_at(index=1, name='Ends:', value=f'{time} second(s) from now')
                await my_msg.edit(embed=giveaway)
                time -= 10
                await asyncio.sleep(10)
            elif 60 <= time < 3600:
                giveaway.remove_field(index=1)
                giveaway.insert_field_at(index=1, name='Ends:', value=f'{time / 60} minute(s) from now')
                await my_msg.edit(embed=giveaway)
                time -= 6
                await asyncio.sleep(6)
            elif 3600 <= time < 86400:
                giveaway.remove_field(index=1)
                giveaway.insert_field_at(index=1, name='Ends:', value=f'{time / 3600} hour(s) from now')
                await my_msg.edit(embed=giveaway)
                time -= 360
                await asyncio.sleep(360)
            elif time >= 86400:
                giveaway.remove_field(index=1)
                giveaway.insert_field_at(index=1, name='Ends:', value=f'{time / 86400} day(s) from now')
                await my_msg.edit(embed=giveaway)
                time -= 8640
                await asyncio.sleep(8640)
        if time <= 0:
            giveaway.remove_field(index=1)
            giveaway.insert_field_at(index=1, name='Ends:',
                                     value=f'Ended at {datetime.datetime.now().strftime("%B %d, %I:%M %p")}')  # noqa
            giveaway.set_footer(text="Thank you for entering. I wish you the best of luck for the next one.")
            await my_msg.edit(embed=giveaway)

        await asyncio.sleep(time)

        new_msg = await ctx.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = choice(users)

        endembed = discord.Embed(
            title="Giveaway ended!",
            description=f"Prize: {prize}\nWinner: {winner.mention}")

        await my_msg.edit(embed=endembed)
        await c.send(f"🎉 Giveaway Winner: {winner.mention} | Prize: {prize}\nPlease message the giveaway host, {ctx.author.mention} to claim the prize")

    @commands.command()
    async def reroll(self, ctx, channel: discord.TextChannel, id_: int):
        try:
            new_message = await channel.fetch_message(id_)
        except:
            return await ctx.send("Incorrect id.")

        users = await new_message.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))
        winner = choice(users)

        reroll_announcement = discord.Embed(color=0xff2424)
        reroll_announcement.set_author(name=f'The giveaway was re-rolled by the host!',
                                       icon_url='https://i.imgur.com/DDric14.png')
        reroll_announcement.add_field(name=f'🥳 New Winner:', value=f'{winner.mention}', inline=False)
        await channel.send(embed=reroll_announcement)


def setup(bot):
    bot.add_cog(Giveaway(bot))
