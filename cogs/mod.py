import discord
from discord.ext import commands
import datetime
import asyncio


client = discord.Client()


class mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    # error when trying to ban someone not in the guild
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        embed = discord.Embed(title="Banned", color=0x719fd0,
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_footer(text=f"{member} has been slain by the ban hammer! 😳")
        embed.add_field(name="User:", value=f"{member}", inline=False)

        await ctx.send(embed=embed)
        await member.ban(reason=None)
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must specify a user!")
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"```{error}```")
    

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                member = ctx.author if not member else member

                embed = discord.Embed(
                    title="Unbanned", color=0xb1a720, timestamp=ctx.message.created_at)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
                embed.set_author(
                    icon_url=ctx.author.avatar_url, name=ctx.author)
                embed.set_footer(text=f"{member} has been unbanned!")
                # add more to this command
                embed.add_field(name="User:", value=f"{member}", inline=False)

                await ctx.channel.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must specify a user!")
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"```{error}```")

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        embed = discord.Embed(title="Kicked", color=0x719fd0,
                              timestamp=ctx.message.created_at)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.set_author(icon_url=ctx.author.avatar_url, name=ctx.author)
        embed.set_footer(text=f"{member} has been kicked! 😳")
        embed.add_field(name="User:", value=f"{member}", inline=False)
        await ctx.send(embed=embed)
        await member.kick(reason=None)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must specify a user!")
        
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"```{error}```")

    @commands.command(aliases=["ui"])
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(color=0x00188f, timestamp=ctx.message.created_at)
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)
        embed.add_field(name="Account Created at:", inline=False,
                        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Guild at:", inline=False,
                        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        await ctx.send(embed=embed)
    

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        amount = int(limit)

        embed = discord.Embed(title="Purge", color=0xff0000,
                              timestamp=ctx.message.created_at)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="Messages Deleted:", value=limit)

        msg = await ctx.send(embed=embed)

        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed, delete_after=5.0)

    @commands.command(pass_context=True, aliases=["guildinfo", "server", "guild", "si"])
    async def serverinfo(self, ctx):
        message = discord.Message
        icon_url = ctx.message.guild.icon_url
        if ctx.message.guild.icon:
            embed = discord.Embed(title="Server Info:",
                                  color=0x00188f, timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=icon_url)

            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Guild Name:",
                            value=f"{ctx.message.guild.name}")
            embed.add_field(name="Guild Owner:",
                            value=f"<@{ctx.message.guild.owner_id}>")

            embed.add_field(name="Guild Description",
                            value=ctx.message.guild.description)

            embed.add_field(name="Rules Channel:",
                            value=ctx.message.guild.rules_channel)

            embed.add_field(name="Shard:", value=ctx.message.guild.shard_id)

            embed.add_field(name="Guild Created on:",
                            value=f"{ctx.message.guild.created_at} UTC")

            await ctx.send(embed=embed)

        elif ctx.message.guild.icon == None:
            embed = discord.Embed(title="Server Info:",
                                  color=0x00188f, timestamp=ctx.message.created_at)
            embed.set_thumbnail(
                url="https://beeimg.com/images/d98703602722.png")

            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Guild name:",
                            value=f"{ctx.message.guild.name}")
            embed.add_field(name="Guild owner:",
                            value=f"<@{ctx.message.guild.owner_id}>")

            embed.add_field(name="Guild Description",
                            value=ctx.message.guild.description)

            embed.add_field(name="Rules Channel:",
                            value=ctx.message.guild.rules_channel)

            embed.add_field(name="Shard:", value=ctx.message.guild.shard_id)

            embed.add_field(name="Guild Created on:",
                            value=f"{ctx.message.guild.created_at} UTC")

            await ctx.send(embed=embed)

    @commands.command(aliases=["permissions", "perm"])
    async def perms(self, ctx, member: discord.Member = None, args=None):
        """Shows the guild permissions of the user"""
        # this was made listening to really hype splatoon music
        member = ctx.author if not member else member
        perm_list = [perm[0] for perm in member.guild_permissions if perm[1]]

        if args == "tuple":
            await ctx.send(f"```py\n{perm_list}```")

        if args == None:

            embed = discord.Embed(
                color=0xa9daea, timestamp=ctx.message.created_at, title="Permissions")
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
            # I know I could've done this in a better way, but your boi is too lazy to do that
            if "administrator" in perm_list:
                embed.add_field(name="Administrator", value="True")
                if "ban_members" in perm_list:
                    embed.add_field(name="Ban Members", value="True")

                    if "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="True")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                    if not "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="False")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                if not "ban_members" in perm_list:
                    embed.add_field(name="Ban Members", value="False")

                    if "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="True")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                    if not "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="False")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

            if not "administrator" in perm_list:
                embed.add_field(name="Administrator", value="False")
                # if not administrator set something else in the embed
                if "ban_members" in perm_list:
                    embed.add_field(name="Ban Members", value="True")

                    if "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="True")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                    if not "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="False")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                if not "ban_members" in perm_list:
                    embed.add_field(name="Ban Members", value="False")

                    if "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="True")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

                    if not "kick_members" in perm_list:
                        embed.add_field(name="Kick Members", value="False")

                        if "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="True")

                        if not "view_audit_log" in perm_list:
                            embed.add_field(
                                name="View Audit Log", value="False")

            await ctx.send(embed=embed)

    @perms.error
    async def perms_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            # probably return the shit as an embed idk
            await ctx.send("Member not found!")


def setup(client):
    client.add_cog(mod(client))
