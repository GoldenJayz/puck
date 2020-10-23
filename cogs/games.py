import discord
from discord.ext import commands
import datetime
import asyncio
import random

client = discord.Client()

class games(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["8ball"])
    async def ball(self, ctx):
        randomlist = ['Maybe','Yes','No',]
        randomgif = ['https://media3.giphy.com/media/141iprzbEPjCiQ/giphy.gif', 'https://i.imgur.com/akdtE4H.gif', 'https://thumbs.gfycat.com/QuestionableMajesticBillygoat-small.gif',]
        
        embed = discord.Embed(title="8ball", color=0x0a0505, timestamp=ctx.message.created_at)
        embed.add_field(name="Results:", value=random.choice(randomlist))
        embed.set_thumbnail(url= (random.choice(randomgif)))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)
    




def setup(client):
    client.add_cog(games(client))