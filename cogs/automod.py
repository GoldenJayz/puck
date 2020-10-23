import discord
from discord.ext import commands
import datetime
import asyncio

client = discord.Client()

class automod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def
    




def setup(client):
    client.add_cog(automod(client))