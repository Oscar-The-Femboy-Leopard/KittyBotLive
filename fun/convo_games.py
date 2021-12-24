import discord
import aiohttp
import html

from discord.ext import commands
from discord.ext.commands import BucketType
from random import choice
from datetime import datetime
# from btns_menus.Buttons import *


CLIENT_SESSION = aiohttp.ClientSession()

taliases = [
    'Truth',
    'T',
    't',
]
tdescription = "Get a truth!"

daliases = [
    'Dare',
    'D',
    'd',
]
ddescription = "Get a dare!"

naliases = [
    'neverhaveiever',
    'NeverHaveIEver',
    'nhie',
    'ever',
    'n',
]
ndescription = "Get a Never Have I Ever question."

ttaliases = [
    'tot',
    'tt'
]
ttdescription = "Get a this or that question."

wyraliases = [
    'wyr',
    'WYR',
    'WouldYouRather',
    'rather',
]
wyrdescription = "Get a Would You Rather question."

wyptbaliases = [
    'wyp',
    'wyptbutton'
]
wyptbdescription = "Get a Will You Press The Button question."


def parse_list_file(file_path: str) -> list:
    with open(file_path) as f:
        return [l.strip() for l in f.readlines() if l.strip()]


class ConvoGames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.database = {
            "truths": parse_list_file('./fun/gamedata/truth.txt'),
            "dares": parse_list_file('./fun/gamedata/dares.txt'),
            "nhie": parse_list_file('./fun/gamedata/nhie.txt'),
            "tot": parse_list_file('./fun/gamedata/tot.txt'),
        }

    @commands.command(aliases=taliases, description=tdescription)
    @commands.cooldown(1, 2.5, BucketType.user)
    async def truth(self, ctx):
        response = f"**Truth:** {choice(self.database['truths'])}"
        e = discord.Embed(color=discord.Color.random(), title=response)
        e.set_footer(text="Truth")
        await ctx.reply(embed=e, mention_author=False)

    @commands.command(aliases=daliases, description=ddescription)
    @commands.cooldown(1, 2.5, BucketType.user)
    async def dare(self, ctx):
        response = f"**Dare:** {choice(self.database['dares'])}"
        e = discord.Embed(color=discord.Color.random(), title=response)
        e.set_footer(text="Dare")
        await ctx.reply(embed=e, mention_author=False)

    '''@commands.command(aliases=naliases, description=ndescription)
    @commands.cooldown(1, 2.5, BucketType.user)
    async def never(self, ctx):
        response = f"**Never have I ever:** {choice(self.database['nhie'])}"
        await ctx.reply(response)'''

    '''@commands.command(aliases=ttaliases, description=ttdescription)
    @commands.cooldown(1, 2.5, BucketType.user)
    async def thisorthat(self, ctx):
        response = choice(self.database['tot'])

        message = []

        c = choice(random_color)

        if ':' in response:
            split = response.split(':')
            message.append(f"**{split[0]}**")
            tort = split[1].strip()

        else:
            tort = response

        message.append(f"🔴 {tort.replace(' or ', ' **OR** ')} 🔵")

        e = discord.Embed(
            color=c,
            timestamp=datetime.utcnow(),
            description='\n'.join(message)
        )

        '''"""btn1 = SButton(label="🔴")
        btn2 = SButton(label="🔵")

        view_ = Button(self.bot, btn1, btn2).view()
        await ctx.send(embed=e, view=view_)"""'''

        sent_embed = await ctx.send(embed=e)
        await sent_embed.add_reaction("🔴")
        await sent_embed.add_reaction("🔵")

    @commands.command(aliases=wyraliases, description=wyrdescription)
    @commands.cooldown(1, 2.5, BucketType.user)
    async def wouldyourather(self, ctx):
        r = 0xEF2928
        b = 0x0094E6
        async with CLIENT_SESSION.get('http://either.io/questions/next/1/') as resp:
            result = await resp.json(content_type=None)
            result = result['questions'][0]

        option1, option2 = result['option_1'].capitalize(), result['option_2'].capitalize()
        option1_total, option2_total = int(result['option1_total']), int(result['option2_total'])
        option_total, comments = option1_total + option2_total, result['comment_total']
        title, desc, url = result['title'], result['moreinfo'], result['short_url']

        embed = discord.Embed(
            title=title,
            url=url,
            color=r if (option1_total > option2_total) else b,
            timestamp=datetime.utcnow()
        )
        embed.add_field(
            name='Would You Rather',
            value=f"🔴 `({(option1_total / option_total * 100):.1f}%)` {option1}\n🔵 `({(option2_total / option_total * 100):.1f}%)` {option2}",
            inline=False
        )
        if desc: embed.add_field(name="More Info", value=desc, inline=False)
        embed.set_footer(text=f"either.io • 💬 {comments}")
        sent_embed = await ctx.send(embed=embed)
        await sent_embed.add_reaction("🔴")
        await sent_embed.add_reaction("🔵")'''

    @commands.command(aliases=wyptbaliases, description=wyptbdescription)
    @commands.cooldown(1, 3, BucketType.user)
    async def willyoupressthebutton(self, ctx):
        r = 0xEF2928
        b = 0x0094E6

        async with CLIENT_SESSION.post('https://api2.willyoupressthebutton.com/api/v2/dilemma') as resp:
            result = await resp.json(content_type=None)
            result = result['dilemma']

        txt1, txt2 = html.unescape(result['txt1']), html.unescape(result['txt2'])
        will_press, wont_press = int(result['yes']), int(result['no'])
        press_total, q_id = (will_press + wont_press), result['id']
        url = f"https://willyoupressthebutton.com/{q_id}"

        embed = discord.Embed(
            title="Press the button?",
            url=url,
            color=r if (will_press > wont_press) else b,
            timestamp=datetime.utcnow()
        )
        embed.add_field(
            name='Will you press the button if...',
            value=f"{txt1}\n**but...**\n{txt2}",
            inline=False
        )
        embed.add_field(
            name='Options',
            value=f"🔴 `({(will_press / press_total * 100):.1f}%)` I will press the button.\n🔵 `({(wont_press / press_total * 100):.1f}%)` I won't press the button.",
            inline=False
        )
        embed.set_footer(text="willyoupressthebutton.com")
        sent_embed = await ctx.send(embed=embed)
        await sent_embed.add_reaction("🔴")
        await sent_embed.add_reaction("🔵")


def setup(bot):
    bot.add_cog(ConvoGames(bot))
