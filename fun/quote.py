import random
import discord
import requests
import json
import datetime

from discord.ext import commands

# imglink = "[here](https://www.goodhousekeeping.com/health/wellness/g2401/inspirational-quotes/)"

aliases = ['Quote', 'Random Quote', 'RQ']
description = f"Selects a random quote from goodhousekeeping or zenquotes. Please message the developer if there's " \
              f"any that you wish to be added which hasn't been added from that site as there's still plenty more " \
              f"that can be used. "


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return quote

    @commands.command(aliases=aliases, description=description)
    async def quote(self, ctx):
        # n = random.randint(1, 2)
        # Good House Keeping
        '''if n == 1:
            responses = [
                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-william-james'
                '-1562000241.png?crop=1xw:1xh;center,top&resize=980:*',
                # Act as if what you do makes a difference. It does.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-winston'
                '-churchill-1562000243.png?crop=1xw:1xh;center,top&resize=980:*',
                # Success is not final, failure is not fatal: it is the courage to continue that counts.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-helen-keller'
                '-2-1562000224.png?crop=1xw:1xh;center,top&resize=980:*',
                # Never bend your head. Always hold it high. Look the world straight in the eye.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-zig-ziglar'
                '-1562000244.png?crop=1xw:1xh;center,top&resize=980:*',
                # What you get by achieving your goals is not as important as what you become by achieving your
                # goals.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-theodore'
                '-roosevelt-1562000239.png?crop=1xw:1xh;center,top&resize=980:*',
                # Believe you can and you're halfway there.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-carol-burnett'
                '-1562000220.png?crop=1xw:1xh;center,top&resize=980:*',
                # When you have a dream, you've got to grab it and never let go.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-jimmy-dean'
                '-1562000225.png?crop=1xw:1xh;center,top&resize=980:*',
                # I can't change the direction of the wind, but I can adjust my sails to always reach my
                # destination.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-demi-lovato'
                '-1562000222.png?crop=1xw:1xh;center,top&resize=980:*',
                # No matter what you're going through, there's a light at the end of the tunnel.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-williiam'
                '-james-2-1562000243.png?crop=1xw:1xh;center,top&resize=980:*',
                # It is our attitude at the beginning of a difficult task which, more than anything else,
                # will affect its successful outcome.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-albert'
                '-einstein-1562000222.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Life is like riding a bicycle. To keep your balance, you must keep moving.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-ella'
                '-fitzgerald-1562000224.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Just don't give up trying to do what you really want to do. Where there is love and
                # inspiration, I don't think you can go wrong.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-amy-poehler'
                '-1562000220.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Limit your "always" and your "nevers."

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-audrey'
                '-hepburn-1562000220.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Nothing is impossible. The word itself says "I'm possible!"

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-c-s-lewis'
                '-1562000220.png?crop=1xw:1xh;center,top&resize=980:* ',
                # You are never too old to set another goal or to dream a new dream.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-maya-angelou'
                '-2-1562000229.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Try to be a rainbow in someone else's cloud.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-camilla'
                '-eyring-kimball-1562000222.png?crop=1xw:1xh;center,top&resize=980:* ',
                # You do not find the happy life. You make it.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-deep-roy'
                '-1562000220.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Inspiration comes from within yourself. One has to be positive. When you're positive,
                # good things happen.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-dr-seuss'
                '-1562000222.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Sometimes you will never know the value of a moment, until it becomes a memory.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-e-e-cummings'
                '-1562000220.png?crop=1xw:1xh;center,top&resize=980:* ',
                # The most wasted of days is one without laughter.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-eleanor'
                '-roosevelt-1562000222.png?crop=1xw:1xh;center,top&resize=980:* ',
                # You must do the things you think you cannot do.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-ella'
                '-fitzgerald-2-1562000222.png?crop=1xw:1xh;center,top&resize=980:* ',
                # It isn't where you came from. It's where you're going that counts.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-geroge-eliot'
                '-1562000224.png?crop=1xw:1xh;center,top&resize=980:* ',
                # It is never too late to be what you might have been.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-hafez'
                '-1562000224.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Stay close to anything that makes you glad you are alive.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-jennifer'
                '-lopez-1562000226.png?crop=1xw:1xh;center,top&resize=980:* ',
                # You get what you give.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-hazrat-inayat'
                '-khan-1562000224.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Some people look for a beautiful place. Others make a place beautiful.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-john'
                '-barrymore-1562000226.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Happiness often sneaks in through a door you didn't know you left open.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-joseph'
                '-campbell-1562000226.png?crop=1xw:1xh;center,top&resize=980:* ',
                # We must be willing to let go of the life we planned so as to have the life that is waiting for
                # us.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-jim-rohn'
                '-1562000226.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Happiness is not by chance, but by choice.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-lindsey-vonn'
                '-1562000226.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Life changes very quickly, in a very positive way, if you let it.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-helen-keller'
                '-1562000224.png?crop=1xw:1xh;center,top&resize=980:* ',
                # Keep your face to the sunshine and you cannot see a shadow.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-mae-jemison'
                '-1562000227.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Never limit yourself because of others’ limited imagination; never limit others because of
                # your own limited imagination.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-mahatma'
                '-gandhi-1562000227.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Be the change that you wish to see in the world.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-malala'
                '-yusafzai-1562000228.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Let us make our future now, and let us make our dreams tomorrow's reality.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-mandy-hale'
                '-1562000228.png?crop=1xw:1xh;center,top&resize=768:* ',
                # You don't always need a plan. Sometimes you just need to breathe, trust, let go, and see what
                # happens.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-martin-luther'
                '-king-jr-1562000228.png?crop=1xw:1xh;center,top&resize=768:* ',
                # If I cannot do great things, I can do small things in a great way.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-maya-angelou'
                '-1562000230.png?crop=1xw:1xh;center,top&resize=768:* ',
                # My mission in life is not merely to survive, but to thrive.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-meghan-markle'
                '-1562000229.png?crop=1xw:1xh;center,top&resize=768:* ',
                # You are enough just as you are.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-michael'
                '-altshuler-1562000230.png?crop=1xw:1xh;center,top&resize=768:* ',
                # The bad news is time flies. The good news is you're the pilot.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-mother'
                '-theresa-1562000231.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Spread love everywhere you go.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-napoleon-hill'
                '-1562000232.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Don't wait. The time will never be just right.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-nicole-kidman'
                '-1562000232.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Life has got all those twists and turns. You've got to hold on tight and off you go.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-oprah-winfrey'
                '-1562000233.png?crop=1xw:1xh;center,top&resize=768:* ',
                # If you look at what you have in life, you'll always have more.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-quentin-blake'
                '-1562000233.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Inspiration is some mysterious blessing which happens when the wheels are turning smoothly.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-reese'
                '-witherspoon-1562000233.png?crop=1xw:1xh;center,top&resize=768:* ',
                # With the right kind of coaching and determination you can accomplish anything.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-roald-dahl'
                '-1562000235.png?crop=1xw:1xh;center,top&resize=768:* ',
                # If you have good thoughts they will shine out of your face like sunbeams and you will always
                # look lovely.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-robin'
                '-williams-1562000237.png?crop=1xw:1xh;center,top&resize=768:* ',
                # No matter what people tell you, words and ideas can change the world.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-rosa-parks'
                '-1562000235.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Each person must live their life as a model for others.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-serena'
                '-williams-1562000237.png?crop=1xw:1xh;center,top&resize=768:* ',
                # A champion is defined not by their wins but by how they can recover when they fall.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-sheryl'
                '-sandberg-1562000239.png?crop=1xw:1xh;center,top&resize=768:* ',
                # Motivation comes from working on things we care about.

                'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/inspirational-quotes-walt-whitman'
                '-1562000241.png?crop=1xw:1xh;center,top&resize=768:* '
                # Keep your face always toward the sunshine, and shadows will fall behind you.
            ]'''

        # zen quotes
        # if n == 2:

        quote = self.get_quote()

        responses = quote

        response = random.choice(responses)
        color = discord.Color.dark_red()
        msg = ctx
        guild = msg.guild

        quote = discord.Embed(color=color, name="Quote", timestamp=datetime.datetime.utcnow())
        quote.add_field(name="Quote", value=f"[Link to image]({response})")
        quote.set_image(url=response)

        await ctx.send(embed=quote)


def setup(bot):
    bot.add_cog(Fun(bot))
