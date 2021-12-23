import datetime
import discord

from discord.ext import commands

aliases = ["whois", "userinfo"]
description = "Find out a member's information within the server."


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''def handle_custom(self, user):
        print(user.activities)
        a = [c for c in user.activities if c.type == ActivityType.custom]
        if not a:
            return None, ActivityType.custom
        a = a[0]
        c_status = None
        if not a.name:
            c_status = self.bot.get_emoji(a.emoji.id)
        if c_status:
            pass
        if a.name and a.emoji:
            c_status = f"{a.emoji} {a.name}"
        elif a.emoji and not c_status:
            c_status = f"{a.emoji}"
        elif a.name:
            c_status = a.name
        else:
            c_status = None
        return c_status, ActivityType.custom

    def handle_playing(self, user):
        p_acts = [c for c in user.activities if c.type == ActivityType.playing]
        p_act = p_acts[0] if p_acts else None
        act = p_act.name if p_act and p_act.name else None
        return act, ActivityType.playing

    def handle_streaming(self, user):
        s_acts = [c for c in user.activities if c.type == ActivityType.streaming]
        s_act = s_acts[0] if s_acts else None
        act = f"{s_act.name}{' | ' if s_act.game else ''}{s_act.game or ''}" if s_act and s_act.name and hasattr(s_act,
                                                                                                                 "game") else s_act.name if s_act and s_act.name else None
        return act, ActivityType.streaming

    def handle_listening(self, user):
        l_acts = [c for c in user.activities if c.type == ActivityType.listening]
        l_act = l_acts[0] if l_acts else None
        act = f"{l_act.title}{' | ' if l_act.artists[0] else ''}{l_act.artists[0] or ''}" if l_act and hasattr(l_act,
                                                                                                               "title") else l_act.name if l_act and l_act.name else None
        return act, ActivityType.listening

    def handle_watching(self, user):
        w_acts = [c for c in user.activities if c.type == ActivityType.watching]
        w_act = w_acts[0] if w_acts else None
        act = w_act.name if w_act else None
        return act, ActivityType.watching

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(embed_links=True)
    async def userinfo(self, ctx, *, user: discord.Member = None):
        author = ctx.author
        guild = ctx.guild

        if not user:
            user = author

        #  A special case for a special someone :^)
        # special_date = datetime(2016, 1, 10, 6, 8, 4, 443000)
        # is_special = user.id == 96130341705637888 and guild.id == 133049272517001216

        roles = user.roles[-1:0:-1]
        names, nicks = await self.bot.get_names_and_nicks(user)

        joined_at = user.joined_at  # if not is_special else special_date
        since_created = (ctx.message.created_at - user.created_at).days
        if joined_at is not None:
            since_joined = (ctx.message.created_at - joined_at).days
            user_joined = joined_at.strftime("%d %b %Y %H:%M")
        else:
            since_joined = "?"
            user_joined = "Unknown"
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        voice_state = user.voice
        member_number = (
                sorted(guild.members, key=lambda m: m.joined_at or ctx.message.created_at).index(user)
                + 1
        )

        created_on = "{}\n({} days ago)".format(user_created, since_created)
        joined_on = "{}\n({} days ago)".format(user_joined, since_joined)

        if user.status.name == "online":
            if user.is_on_mobile() is True:
                statusemoji = "https://cdn.discordapp.com/emojis/554418132953989140.png?v=1"
            else:
                statusemoji = "https://cdn.discordapp.com/emojis/642458713738838017.png?v=1"
        elif user.status.name == "offline":
            statusemoji = "https://cdn.discordapp.com/emojis/642458714074513427.png?v=1"
        elif user.status.name == "dnd":
            statusemoji = "https://cdn.discordapp.com/emojis/642458714145816602.png?v=1"
        elif user.status.name == "streaming":
            statusemoji = "https://cdn.discordapp.com/emojis/642458713692569602.png?v=1"
        elif user.status.name == "idle":
            statusemoji = "https://cdn.discordapp.com/emojis/642458714003210240.png?v=1"

        activity = "Chilling in {} status".format(user.status)
        if user.activity is None:  # Default status
            pass
        else:
            acts = self.handle_custom(user), self.handle_playing(user), self.handle_listening(
                user), self.handle_streaming(user), self.handle_watching(user)
            status = [t for t in acts if None not in t]
            custom = [c in i in status if status[0] == discord.ActivityType.custom]
            # print(status)

        if roles:

            role_str = ", ".join([x.mention for x in roles])
            # 400 BAD REQUEST (error code: 50035): Invalid Form Body
            # In embed.fields.2.value: Must be 1024 or fewer in length.
            if len(role_str) > 1024:
                # Alternative string building time.
                # This is not the most optimal, but if you're hitting this, you are losing more time
                # to every single check running on users than the occasional user info invoke
                # We don't start by building this way, since the number of times we hit this should be
                # infintesimally small compared to when we don't across all uses of Red.
                continuation_string = (
                    "and {numeric_number} more roles not displayed due to embed limits."
                )
                available_length = 1024 - len(continuation_string)  # do not attempt to tweak, i18n

                role_chunks = []
                remaining_roles = 0

                for r in roles:
                    chunk = f"{r.mention}, "
                    chunk_size = len(chunk)

                    if chunk_size < available_length:
                        available_length -= chunk_size
                        role_chunks.append(chunk)
                    else:
                        remaining_roles += 1

                role_chunks.append(continuation_string.format(numeric_number=remaining_roles))

                role_str = "".join(role_chunks)

        else:
            role_str = None

        if status is None:
            data = discord.Embed(description="{}".format(activity), colour=user.colour)
        else:
            data = discord.Embed(
                description="{}\nCustom Status: {}".format(activity, custom), colour=user.colour
            )

        data.add_field(name="Joined Discord on", value=created_on)
        data.add_field(name="Joined this server on", value=joined_on)
        if role_str is not None:
            data.add_field(name="Roles", value=role_str, inline=False)
        if names:
            # May need sanitizing later, but mentions do not ping in embeds currently
            val = filter_invites(", ".join(names))
            data.add_field(name="Previous Names", value=val, inline=False)
        if nicks:
            # May need sanitizing later, but mentions do not ping in embeds currently
            val = filter_invites(", ".join(nicks))
            data.add_field(name="Previous Nicknames", value=val, inline=False)
        if voice_state and voice_state.channel:
            data.add_field(
                name="Current voice channel",
                value="{0.mention} ID: {0.id}".format(voice_state.channel),
                inline=False,
            )
        data.set_footer(text="Member #{} | User ID: {}".format(member_number, user.id))

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name
        # name = filter_invites(name)

        if user.avatar:
            avatar = user.avatar_url_as(static_format="png")
            data.set_author(name=name, url=avatar, icon_url=statusemoji)
            data.set_thumbnail(url=avatar)
        else:
            data.set_author(name=name)

        await ctx.send(embed=data)'''

    @commands.command(aliases=aliases, description=description)
    async def personinfo(self, ctx, member: discord.Member = None):
        '''async def personinfo(self, ctx, message):

        if int is message.content:
            uID = int
            member = (self.bot.get_user(uID))
            if uID is None:
                member = ctx.message.author.id

        if message.content.mention == discord.Member.mention:
            member = discord.Member.mention
            if ctx.content.mention is None:
                member = ctx.author'''

        if member is None:
            member = ctx.author

        uID = member.id

        online = "🟢"
        dnd = "🔴"
        offline = "⚫"
        idol = "🟡"

        roles = [role for role in member.roles]

        embed = discord.Embed(colour=ctx.message.author.top_role.colour, timestamp=datetime.datetime.utcnow(),
                              title=f"User Info -\n {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author} | uID:{ctx.author.id}")

        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=False)
        embed.add_field(name="Server Name:", value=member.mention, inline=False)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name="Roles:", value="_ _".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        # embed.add_field(name="Permissions", value=f"_ _".join([role.permissions for role in roles]), inline=False)
        # embed.add_field(name="Permissions", value=f"{[role.permissions for role in roles]}", inline=False)
        # embed.add_field(name="Key Permissions", value=member.guild_permissions, inline=False)

        # banner = f"https://cdn.discordapp.com/banners/{uID}/{member.user_banner}"
        # banner = f"https://cdn.discordapp.com/banners/{uID}/{member.banner}"

        # embed.add_field(name="Discord PFP:", value=member.avatar_url)
        embed.add_field(name="Discord PFP:", value="_ _")
        embed.set_image(url=member.avatar_url)
        # embed.add_field(name="Discord Banner:", value=member.banner_url)
        # embed.add_field(name="Discord Banner:", value=banner)

        if member.status.name == "offline":
            emoji = offline
        if member.status.name == "online":
            emoji = online
        if member.status.name == "dnd":
            emoji = dnd
        if member.status.name == 'idol':
            emoji = idol

        embed.add_field(name="Status:", value=f"{emoji}" + member.status.name, inline=False)
        # embed.add_field(name="User Status:", value=member._state, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Utility(bot))
