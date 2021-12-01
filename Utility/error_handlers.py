import discord
from discord.ext import commands
from config import PREFIX


class error_handling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        priv = self.client.get_guild(488623700539736064).get_channel(915405860266704906)

        msg = discord.Embed(title="ERROR!", color=discord.Color.red())
        msg.add_field(name="Member:", value=f"Name: `{ctx.author.display_name}`\nID: `{ctx.author.id}`)", inline=False)
        msg.add_field(name="Guild:", value=f"Name: `{ctx.guild}`\nID: `{ctx.guild.id}`", inline=False)
        msg.add_field(name="Channel:", value=f"Name: `{ctx.channel}`\nID: `{ctx.channel.id}`", inline=False)

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply('You are missing the required argument of: `{}`'.format(error))
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You do not have all the permissions required!")
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.MissingRole):
            await ctx.reply("You are missing a role to complete this.")
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.BotMissingPermissions):
            await ctx.reply('I cannot complete this as I am missing the {} permission.'.format(error))
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.BadArgument):
            await ctx.reply("Bad argument! {}".format(error))
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"Command not found! Please refer to `{PREFIX}help` to avoid this error in the future.")
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.TooManyArguments):
            await ctx.reply(f"Too many arguments! Please refer to `{PREFIX}help <command>` for more information ")
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.reply("Command is on cooldown! Please retry after: `{}`").format(error)
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.ChannelNotReadable):
            await ctx.reply("I cannot read this channel. Please check my permissions.")
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, commands.EmojiNotFound):
            await ctx.reply("Cannot find the required emoji.\n\n{}").format(error)
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        if isinstance(error, discord.Forbidden):
            await ctx.reply("I am forbidden: {}").format(error)
            msg.add_field(name="Error Type:", value=f"{error}", inline=False)
            msg.add_field(name="Content of message:", value=ctx.message.content, inline=False)
            print(error)

        await priv.send(embed=msg)


def setup(client):
    client.add_cog(error_handling(client))
