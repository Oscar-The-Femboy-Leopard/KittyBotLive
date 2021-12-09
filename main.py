import asyncio
import datetime
import random
import sys
import traceback
import discord

from discord.ext import commands
from config import PREFIX, cog_extentions, TOKEN, _blnk_value, _PREFIX, _prefix

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=[PREFIX, _PREFIX, _prefix], intents=intents)
client.remove_command('help')


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('_______')

    channel = client.get_channel(844603898203078707)
    await channel.send(f"Bot started at: {datetime.datetime.utcnow()}")

    while True:
        status = [  # playing statuses
            discord.Activity(name=f'my fav games|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'Chinese Whispers with my dev|{PREFIX}help',
                             type=discord.ActivityType.playing),
            discord.Activity(name=f'crane games for cool stuff|{PREFIX}help',
                             type=discord.ActivityType.playing),
            discord.Activity(name=f'with my friends|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with leopards!|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with foxes!|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with bunnies!|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with wolves|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with lynxes|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with paws|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with my RAM|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'on my BIOS trying to Overclock my CPU|{PREFIX}help',
                             type=discord.ActivityType.playing),
            discord.Activity(name=f'on my dedicated server!|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with you cool furs|{PREFIX}help',
                             type=discord.ActivityType.playing),
            discord.Activity(name=f"on my Dev's nerves|{PREFIX}help",
                             type=discord.ActivityType.playing),
            discord.Activity(name=f'with my Dev|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f'with my Prefix|{PREFIX}help', type=discord.ActivityType.playing),
            discord.Activity(name=f"with my dev's hair|{PREFIX}help", type=discord.ActivityType.playing),

            # watching Statuses
            discord.Activity(name=f'the sever for my Dev|{PREFIX}help',
                             type=discord.ActivityType.watching),
            discord.Activity(name=f'some cool things with my Dev|{PREFIX}help',
                             type=discord.ActivityType.watching),
            discord.Activity(name=f'something lame... Why is my dev boring?|{PREFIX}help',
                             type=discord.ActivityType.watching),
            discord.Activity(name=f'butterflies fly!❤|{PREFIX}help',
                             type=discord.ActivityType.watching),

            # listening statuses
            discord.Activity(name=f'birds chirping|{PREFIX}help',
                             type=discord.ActivityType.listening),
            discord.Activity(name=f'my Dev yelling at me 💢 |{PREFIX}help',
                             type=discord.ActivityType.listening),
            discord.Activity(name=f'my cookies crunching |{PREFIX}help',
                             type=discord.ActivityType.listening),
            discord.Activity(name=f'heavy metal with my dev|{PREFIX}help',
                             type=discord.ActivityType.listening)]

        activity = random.choice(status)
        channel1 = client.get_channel(835656871376453673)
        channel = client.get_channel(861989383590248459)

        await client.change_presence(activity=activity)
        await channel1.send(f"Changed my status to {activity.type} {activity.name}. Changing again in 5 minutes!")
        await channel.send(f'Bot Time Check In. Time is now\n**{datetime.datetime.utcnow()}**\n_ _')
        await asyncio.sleep(300)


if __name__ == '__main__':
    for extention in cog_extentions:
        try:
            client.load_extension(extention)
        except Exception as e:
            print(f"Failed load extension {extention}", file=sys.stderr)
            traceback.print_exc()


# TODO Impliment Quote Of The Day
# TODO Impliment Question Of The Day
# TODO Impliment actual Insult command
# TODO Use bad_list to deny phrases and words from getting into memes
# TODO Investigate issues with memes holding more than just 2 options. They're not posting anymore than 2 in a meme.


@client.group(invoke_without_command=True)
async def help(ctx):
    mhelp = discord.Embed(title="Help", description=f"Use {PREFIX}help <module> to load the module help pages")

    mhelp.add_field(name="Fun", value="Have some fun commands in here for you to enjoy!", inline=False)
    mhelp.add_field(name="Memes", value="Make use of Imgflip's API to generate your own memes!", inline=False)
    # mhelp.add_field(name="Moderation", value="Commands for Staff", inline=False)
    mhelp.add_field(name='Utility', value="Some utility commands to play with", inline=False)

    footer = "Remember! Commands and modules ARE case sensitive."

    mhelp.set_footer(text=footer)

    await ctx.send(embed=mhelp)


@help.command()
async def Fun(ctx):
    fhelp = discord.Embed(title="Fun Help Page",
                          description=f"Use {PREFIX}help <command> to load the command help page.")

    fun = '8ball\nfact\ninsult\nkill\nquote\nrps\nship'
    footer = "Remember! Commands and modules ARE case sensitive."

    fhelp.add_field(name=_blnk_value, value=fun, inline=False)
    fhelp.set_footer(text=footer)

    await ctx.send(embed=fhelp)


@help.command()
async def Memes(ctx):
    mhelp = discord.Embed(title="Memes Help Page",
                          description=f"Use {PREFIX}help <command> to load the command help page.")

    meme = "brace\nchangemymind\nfirst_world_problem\nbutton\noption\nskeleton\nspongemock\nimagination\nim_out" \
           "\nthink\nthisisfine\ntoo_high\ntrump\nuno"

    mhelp.add_field(name=_blnk_value, value=meme, inline=False)
    mhelp.add_field(name="What if I want to see a meme added? What can I do to suggest?",
                    value=f"Well... You can suggest with many ways, including the `{PREFIX}alert` command or messaging the "
                          "dev directly!", inline=False)
    footer = "Remember! Commands and modules ARE case sensitive."

    mhelp.set_footer(text=footer)

    await ctx.send(embed=mhelp)


@help.command()
async def Utility(ctx):
    uhelp = discord.Embed(title="Utility Help Page",
                          description=f"Use {PREFIX}help <command> to load the command help page.")

    utility = 'personinfo\npfp\nping\ntimer\nuptime\n'
    footer = "Remember! Commands and modules ARE case sensitive."

    uhelp.add_field(name=_blnk_value, value=utility, inline=False)
    uhelp.set_footer(text=footer)

    await ctx.send(embed=uhelp)


@help.command()
async def Wholesome(ctx):
    whelp = discord.Embed(title="Memes Help Page",
                          description=f"Use {PREFIX}help <command> to load the command help page.")

    wholesome = 'boop\ndoggo\nhug\nlick\n'
    footer = "Remember! Commands and modules ARE case sensitive."

    whelp.add_field(name=_blnk_value, value=wholesome, inline=False)
    whelp.set_footer(text=footer)

    await ctx.send(embed=whelp)


@help.command(name="8ball")
async def _8ball(ctx):
    from fun._8ball import aliases, description
    __8ball = discord.Embed(title='8Ball', description=description)
    __8ball.add_field(name="**Command Syntax**", value=f"{PREFIX}8ball <question>")
    __8ball.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=__8ball)


'''@help.command()
async def coinflip(ctx):
    from fun.coinflip import aliases, description
    Coinflip = discord.Embed(title='coinflip', description=description)
    Coinflip.add_field(name="**Command Syntax**", value=f"{PREFIX}coinflip")
    Coinflip.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=Coinflip)'''


@help.command()
async def fact(ctx):
    from fun.fact import aliases, description
    Fact = discord.Embed(title='fact', description=description)
    Fact.add_field(name="**Command Syntax**", value=f"{PREFIX}fact")
    Fact.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=Fact)


@help.command()
async def insult(ctx):
    from fun.insult import aliases, description
    Insult = discord.Embed(title='insult', description=description)
    Insult.add_field(name="**Command Syntax**", value=f"{PREFIX}insult <member>")
    Insult.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=Insult)


@help.command()
async def kill(ctx):
    from fun.kill import aliases, description
    Kill = discord.Embed(title='kill', description=description)
    Kill.add_field(name="**Command Syntax**", value=f"{PREFIX}kill <member>")
    Kill.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=Kill)


@help.command()
async def quote(ctx):
    from fun.quote import aliases, description
    Quote = discord.Embed(title='quote', description=description)
    Quote.add_field(name="**Command Syntax**", value=f"{PREFIX}quote")
    Quote.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=Quote)


@help.command()
async def rps(ctx):
    from fun.rps import aliases, description
    rps = discord.Embed(title='Rock, Paper, Scissors!', description=description)
    rps.add_field(name="**Command Syntax**", value=f"{PREFIX}rps <Rock/Paper/Scissors>")
    rps.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=rps)


@help.command()
async def ship(ctx):
    from fun.ship import aliases, description
    ship = discord.Embed(title='Ship', description=description)
    ship.add_field(name="**Command Syntax**", value=f"{PREFIX}ship <member>")
    ship.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=ship)


'''@help.command()
async def bf(ctx):
    from imgflip_meme_creation.bf import aliases, description
    bf = discord.Embed(title='distracted boyfriend', description=description)
    bf.add_field(name="**Command Syntax**", value=f"{PREFIX}bf <message>")
    bf.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=bf)'''


@help.command()
async def brace(ctx):
    from imgflip_meme_creation.brace import aliases, description
    brace = discord.Embed(title='brace', description=description)
    brace.add_field(name="**Command Syntax**", value=f"{PREFIX}brace <message>")
    brace.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=brace)


@help.command()
async def cardboard_sign(ctx):
    from imgflip_meme_creation.cardboard_sign import aliases, description
    option = discord.Embed(title='cardboard_sign', description=description)
    option.add_field(name="**Command Syntax**", value=f"{PREFIX}cardboard_sign <message>.<message2>", inline=False)
    option.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                     value=_blnk_value, inline=False)
    option.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=option)


@help.command()
async def changemymind(ctx):
    from imgflip_meme_creation.change_my_mind import aliases, description
    CMM = discord.Embed(title='Change My Mind', description=description)
    CMM.add_field(name="**Command Syntax**", value=f"{PREFIX}changemymind <message>")
    CMM.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=CMM)


@help.command()
async def first_world_problem(ctx):
    from imgflip_meme_creation.first_world_problem import aliases, description
    fwp = discord.Embed(title='first world problem', description=description)
    fwp.add_field(name="**Command Syntax**", value=f"{PREFIX}fwp <message>")
    fwp.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=fwp)


@help.command()
async def lie_detector(ctx):
    from imgflip_meme_creation.lie_detector import aliases, description
    option = discord.Embed(title='Maury Lie Detector', description=description)
    option.add_field(name="**Command Syntax**", value=f"{PREFIX}lie_detector <message>.<message2>", inline=False)
    option.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                     value=_blnk_value, inline=False)
    option.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=option)


@help.command()
async def button(ctx):
    from imgflip_meme_creation.nut_button import aliases, description
    imagination = discord.Embed(title='Blank Nut Button', description=description)
    imagination.add_field(name="**Command Syntax**", value=f"{PREFIX}nut <message>.<message2>")
    imagination.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                          value=_blnk_value, inline=True)
    imagination.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=imagination)


@help.command()
async def option(ctx):
    from imgflip_meme_creation.option import aliases, description
    option = discord.Embed(title='options', description=description)
    option.add_field(name="**Command Syntax**", value=f"{PREFIX}options <message>.<message2>", inline=False)
    option.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                     value=_blnk_value, inline=False)
    option.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=option)


@help.command()
async def putitsomwhereelse(ctx):
    from imgflip_meme_creation.put_it_somewhere_else import aliases, description
    option = discord.Embed(title='put it somewhere else', description=description)
    option.add_field(name="**Command Syntax**", value=f"{PREFIX}putitsomwhereelse <message>.<message2>", inline=False)
    option.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                     value=_blnk_value, inline=False)
    option.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=option)


@help.command()
async def say_that_again(ctx):
    from imgflip_meme_creation.say_that_again import aliases, description
    option = discord.Embed(title='Say That Again I Dare You', description=description)
    option.add_field(name="**Command Syntax**", value=f"{PREFIX}say_that_again <message>.<message2>", inline=False)
    option.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                     value=_blnk_value, inline=False)
    option.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=option)


@help.command()
async def skeleton(ctx):
    from imgflip_meme_creation.skeleton import aliases, description
    imagination = discord.Embed(title='Waiting Skeleton', description=description)
    imagination.add_field(name="**Command Syntax**", value=f"{PREFIX}skeleton <message>", inline=False)
    imagination.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=imagination)


@help.command()
async def spongemock(ctx):
    from imgflip_meme_creation.spongebob_mock import aliases, description
    mock = discord.Embed(title="Mocking Spongebob meme!", description=description)
    mock.add_field(name="**Command Syntax**", value=f"{PREFIX}spongemock <message>.<message2>", inline=False)
    mock.add_field(name="This command **REQUIRES** a `.` to split the thexts for the sides of the memes!",
                   value=_blnk_value, inline=False)
    mock.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=mock)


@help.command()
async def imagination(ctx):
    from imgflip_meme_creation.spongebob_imagination import aliases, description
    imagination = discord.Embed(title='Spongebob Imagination', description=description)
    imagination.add_field(name="**Command Syntax**", value=f"{PREFIX}imagination <message>")
    imagination.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=imagination)


@help.command()
async def im_out(ctx):
    from imgflip_meme_creation.Spongebob_heads_out import aliases, description
    im_out = discord.Embed(title='Spongebob Imagination', description=description)
    im_out.add_field(name="**Command Syntax**", value=f"{PREFIX}im_out <message>")
    im_out.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=im_out)


@help.command()
async def think(ctx):
    from imgflip_meme_creation.think import aliases, description
    think = discord.Embed(title='Think', description=description)
    think.add_field(name="**Command Syntax**", value=f"{PREFIX}think <message1>.<message2>")
    think.add_field(name="This command **REQUIRES** a `.` to split the texts for the sides of the memes!",
                    value=_blnk_value, inline=True)
    think.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=think)


@help.command()
async def this_is_fine(ctx):
    from imgflip_meme_creation.this_is_fine import aliases, description
    tif = discord.Embed(title='This is fine', description=description)
    tif.add_field(name="**Command Syntax**", value=f"{PREFIX}thisisfine <message>")
    tif.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=tif)


@help.command()
async def trump(ctx):
    from imgflip_meme_creation.trump import aliases, description
    trump = discord.Embed(title='This is fine', description=description)
    trump.add_field(name="**Command Syntax**", value=f"{PREFIX}trump <message>")
    trump.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=trump)


@help.command()
async def uno(ctx):
    from imgflip_meme_creation.uno import aliases, description
    uno = discord.Embed(title='Uno', description=description)
    uno.add_field(name="**Command Syntax**", value=f"{PREFIX}uno <message>", inline=False)
    uno.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=uno)


@help.command()
async def userinfo(ctx):
    from Utility.personinfo import aliases, description
    info = discord.Embed(title='Member Info', description=description)
    info.add_field(name="**Command Syntax**", value=f"{PREFIX}userinfo <member>")
    info.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=info)


@help.command()
async def pfp(ctx):
    from Utility.pfp import aliases, description
    info = discord.Embed(title='Pfp', description=description)
    info.add_field(name="**Command Syntax**", value=f"{PREFIX}pfp <member>")
    info.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=info)


@help.command()
async def ping(ctx):
    from Utility.ping import aliases, description
    info = discord.Embed(title='Ping', description=description)
    info.add_field(name="**Command Syntax**", value=f"{PREFIX}ping")
    info.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=info)


@help.command()
async def timer(ctx):
    from Utility.timer import aliases, description
    timer = discord.Embed(title='Timer', description=description)
    timer.add_field(name="**Command Syntax**", value=f"{PREFIX}timer <amount of time in seconds>")
    timer.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=timer)


@help.command()
async def uptime(ctx):
    from Utility.uptime import aliases, description
    uptime = discord.Embed(title='Uptime', description=description)
    uptime.add_field(name="**Command Syntax**", value=f"{PREFIX}uptime")
    uptime.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=uptime)


@help.command()
async def boop(ctx):
    from Wynter_Integration.boop import aliases, description
    boop = discord.Embed(title='Boop', description=description)
    boop.add_field(name="**Command Syntax**", value=f"{PREFIX}boop <member>")
    boop.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=boop)


@help.command()
async def doggo(ctx):
    from Wynter_Integration.doggo import aliases, description
    doggo = discord.Embed(title='Doggo!', description=description)
    doggo.add_field(name="**Command Syntax**", value=f"{PREFIX}doggo")
    doggo.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=doggo)


@help.command()
async def hug(ctx):
    from Wynter_Integration.hug import aliases, description
    hug = discord.Embed(title='Hug', description=description)
    hug.add_field(name="**Command Syntax**", value=f"{PREFIX}hug <member>")
    hug.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=hug)


@help.command()
async def lick(ctx):
    from Wynter_Integration.lick import aliases, description
    lick = discord.Embed(title='Lick', description=description)
    lick.add_field(name="**Command Syntax**", value=f"{PREFIX}lick <member>")
    lick.set_footer(text=f"Aliases for this command are: {aliases}")
    await ctx.send(embed=lick)


client.run(TOKEN, reconnect=True)
