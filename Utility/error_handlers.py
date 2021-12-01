import discord
from discord.ext import commands
from config import PREFIX


class error_handling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('You are missing the required argument of: `{}`'.format(error))
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You do not have all the permissions required!")
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.MissingRole):
            await ctx.reply("You are missing a role to complete this.")
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply('I cannot complete this as I am missing the {} permission.'.format(error))
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.BadArgument):
            await ctx.reply("Bad argument! {}".format(error))
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"Command not found! Please refer to `{PREFIX}help` to avoid this error in the future.")
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Too many arguments! Please refer to `{PREFIX}help <command>` for more information ")
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply("Command is on cooldown! Please retry after: `{}`").format(error)
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.ChannelNotReadable):
            await ctx.reply("I cannot read this channel. Please check my permissions.")
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, commands.EmojiNotFound):
            await ctx.reply("Cannot find the required emoji.\n\n{}").format(error)
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)

        if isinstance(error, discord.Forbidden):
            await ctx.reply("I am forbidden: {}").format(error)
            priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)
            await priv.send(f'{ctx.author.display_name} (uID {ctx.author.id} has this error:\n\n{error}')
            print(error)


def setup(client):
    client.add_cog(error_handling(client))
