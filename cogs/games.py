import discord
from discord.ext import commands
import datetime
import asyncio
import random
from tqdm import tqdm

client = discord.Client()
  


class games(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases=["8ball"])
    async def ball(self, ctx, *, args):
        randomlist = ['Maybe', 'Yes', 'No', ]
        randomgif = ['https://media3.giphy.com/media/141iprzbEPjCiQ/giphy.gif', 'https://i.imgur.com/akdtE4H.gif',
                     'https://thumbs.gfycat.com/QuestionableMajesticBillygoat-small.gif', ]

        embed = discord.Embed(title="8ball", color=0x0a0505,
                              timestamp=ctx.message.created_at)
        embed.add_field(name=f"Results for *{args}*", value=random.choice(randomlist))
        embed.set_thumbnail(url=(random.choice(randomgif)))
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def love(self, ctx, member: discord.Member = None):

        member = ctx.author if not member else member
        result = random.randrange(100)
        embed = discord.Embed(title="Love counter",
                              color=0x0a0505, timestamp=ctx.message.created_at)
        embed.add_field(
            name=f"Love between {ctx.author} and {member}", value=f"{random.randrange(100)}" + "%")
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        #if love meter random number is in range 0-50 place an arrangement of emojis

    @love.error
    async def love_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to mention a person!")


def setup(client):
      
    client.add_cog(games(client))
