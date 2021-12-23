import ast
import datetime
import random
import discord
from discord.ext import commands
from config import _blnk_value, Owner_Name

aliases = ['cstatus', 'CStatus', 'Random_Status', 'random_status']
description = "It gives out a random fact!"


def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)


class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=aliases,
                      description=description)
    @commands.is_owner()
    async def songstatus(self, ctx):
        AC = "Alice Cooper"
        ATR = 'All That Remains'
        A7X = 'Avenged Sevenfold'
        BFMV = 'Bullet For My Valentine'
        DL = 'Def Leppard'
        FM = 'Fort Minor'
        IM = 'Iron Maiden'
        KL = 'Kenny Loggins'
        LP = 'Lynkin Park'
        APC = 'A Perfect Circle'
        P = 'Poison'
        Q = 'Queen'
        Slip = 'Slipknot'
        artist = [
            AC,
            ATR,
            A7X,
            BFMV,
            DL,
            FM,
            IM,
            KL,
            LP,
            APC,
            P,
            Q,
            Slip

        ]

        AC = [

        ]

        ATR = [

        ]

        A7X = [

        ]

        BFMV = [
            # Hand of Blood
            'There goes my valentine again\nSoaked in red for what she said',
            "I don't want to feel, my heart is breaking",
            "I don't want to see, my life is burning!",
            "I saw you look away\nIs what you've seen too much to take\nOr are you blind and seeing nothing?",
            "Is what I've done too much to take\nOr are you scared of being nothing?",

            # All The Things I Hate
            "Once more I say goodbye, to you\nThings happen but we don't really know why",
            "If it's supposed to be like this, why do most of us ignore the chance to miss?",
            "Torn apart at the seams and my dreams turn to tears",
            "Run away try to find a safe place you can hide\nIt's the best place to be when you're feeling like",
            "Once more you tell those lies, to me\nWhy can't you just be straight up with honesty?",

            # No Way Out
            "Looking out standing over the edge\nToo numb to feel alive",
            "So why the fuck are these thoughts in my head?\nReach in and pull them out!",
            "Still nothing feels the same\nToo late to hesitate\nWhy can't I run and escape from myself?",
            # "Tell me why I feel like there's no way out\nTrying hard to heal as the pain pours out\nI don't wanna feel this way but it's hard",
            "There's nothing left for me\nJust tainted memories\nThere's no one here for me",

            # Venom
            "You're nowhere even near me\nBut everywhere I go I feel you\nCan you feel me?",
            "How dare you play the victim?\nThese tortured eyes, they see right through you\nRight through you",
            
            # Your Betrayal
            "Am I going insane?\nMy blood is boiling inside of my veins",
            # "My body's shaking, there's no turning back\nDon't take your eyes off the trigger!\nI'm not to blame if your world turns to black",
            "My heart is pounding as I say goodbye\nSo now I dance in the flames\nI love you crying and screaming my name",
            "I love you crying and screaming my name\nYou said that we'd be forever!\nHow could you kill me and lie to my face?",

            # Over It
            "After all this time\nYou still couldn't recognize\nThat your problem lies within\nIn a vicious circle",
            "Can you tell me why?\nWhy you've thrown it all away\n'Cause it makes no sense to me\nWhy you wouldn't listen",
            "I know it hurts\nI tried to help to ease your pain",
            "You've only got yourself to blame\nAnd I can't take this anymore\nI'm over it\nSo over it",
            "Watching you decline\nWhat were you expecting\nI can't save you from yourself\nWhen you don't want saving",

            # Tears Don't Fall
            "There's always something different going wrong\nThe path I walk's in the wrong direction",
            "Your tears don't fall, they crash around me\nHer conscience calls, the guilty to come home",
            "The moments die, I hear no screaming\nThe visions left inside me are slowly fading",

            # The Harder The Heart (The Harder It Breaks)
            "I'm not the reason you're empty!\nI'm not your scapegoat or shoulder to cry on\nI'm just the person you needed!",
            "Why can't you see, can't believe\nThat you are your own worst enemy?",
            # "These are our times, never forget\nNo looking back, no more regrets\nOne thing we've learned from our mistakes\nThe harder the heart, the harder it breaks",
            "You've gone and burnt all your bridges!\nDo I have to sit and watch 'til nothing remains?!",


                ]

        DL = [

        ]

        FM = [

        ]

        IM = [

        ]

        KL = [

        ]

        LP = [

        ]

        APC = [

        ]

        P = [

        ]

        Q = [

        ]

        Slip = [

        ]

        chooseArtist = random.choice(artist)

        if chooseArtist == AC:
            song = random.choice(AC)

        if chooseArtist == ATR:
            song = random.choice(ATR)

        if chooseArtist == A7X:
            song = random.choice(A7X)

        if chooseArtist == BFMV:
            song = random.choice(BFMV)

        if chooseArtist == DL:
            song = random.choice(DL)

        if chooseArtist == FM:
            song = random.choice(FM)

        if chooseArtist == IM:
            song = random.choice(IM)

        if chooseArtist == KL:
            song = random.choice(KL)

        if chooseArtist == LP:
            song = random.choice(LP)

        if chooseArtist == APC:
            song = random.choice(APC)

        if chooseArtist == P:
            song = random.choice(P)

        if chooseArtist == Q:
            song = random.choice(Q)

        if chooseArtist == Slip:
            song = random.choice(Slip)


        color = discord.Color.dark_red()
        msg = ctx
        guild = msg.guild

        q = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        q.add_field(name=_blnk_value, value=song, inline=True)
        q.set_footer(text=f'Bot made by {Owner_Name}')

        await ctx.send(embed=q)


def setup(bot):
    bot.add_cog(OwnerCog(bot))
