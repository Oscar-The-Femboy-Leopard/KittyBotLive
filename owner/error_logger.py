import ast
import discord
from discord.ext import commands
from config import Owner_ID


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
        self.author = Owner_ID
        self.bot = bot

    @commands.Cog.listener()
    async def errornotification(self, ctx, *, bot):

        channel = bot.guild.get_channel(844351284568260608)
        error = bot.on_error(self)

        # await bot.guild.get_channel(channel).send(f'{type(e).__name__} - {e}')

        '''try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            print("loaded")'''


def setup(bot):
    bot.add_cog(OwnerCog(bot))
