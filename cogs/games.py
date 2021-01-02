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

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        huglist = ["https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587", "https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498", "https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885", "https://media1.tenor.com/images/c2156769899d169306d16b063a55d0b2/tenor.gif?itemid=14584871"]
        #i copy and pasted here cause im lazy
        embed = discord.Embed(title="Hug",
                              color=0xd400ff, timestamp=ctx.message.created_at)
        embed.add_field(
            name=f"{ctx.author} hugged {member}!", value=f"*{ctx.author} ran up to {member} and gave them a big fat hug*")
        embed.set_image(url=random.choice(huglist))
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
    
    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bro what are you doing!? You cannot hug yourself :(((")


def setup(client):
      
    client.add_cog(games(client))
