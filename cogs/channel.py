import discord
from discord.ext import commands
import datetime
import asyncio
import requests
import time
import math

client = discord.Client()


class channel(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def create(self, ctx, args):
        guild = ctx.message.guild

        perms = {
            ctx.message.guild.default_role: discord.PermissionOverwrite(connect=False),
            ctx.message.guild.me: discord.PermissionOverwrite(connect=True),
            ctx.message.author: discord.PermissionOverwrite(connect=True)
        }

        await guild.create_voice_channel(name=args, overwrites=perms)

        await ctx.send(f"Created a voice channel called {args}")

    @commands.command()
    async def invite(self, ctx, member: discord.Member):
        try:
            perms = {
                member: discord.PermissionOverwrite(connect=True),
                ctx.message.guild.default_role: discord.PermissionOverwrite(connect=False),
                ctx.message.guild.me: discord.PermissionOverwrite(connect=True),
                ctx.message.author: discord.PermissionOverwrite(connect=True)
            }

            await ctx.author.voice.channel.edit(overwrites=perms)

            await ctx.send(f"{member} is now allowed to join the private VC!")

        except:
            await ctx.send("You need to mention somebody!")

    @commands.command()
    async def delete(self, ctx):
        try:
            await ctx.author.voice.channel.delete()

            await ctx.send("Channel has been deleted!")

        except:
            await ctx.send("You have to be inside a voice channel!")


def setup(client):
    client.add_cog(channel(client))
