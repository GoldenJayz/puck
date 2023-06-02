import discord
from discord.ext import commands



class slock(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["sl", "slock"])
    async def serverlock(self, ctx):
		text_channel_list = []
		for guild in client.guilds:
			for channel in guild.text_channels:
				text_channel_list.append(channel)
				overwrite = discord.PermissionOverwrite()
				overwrite.send_messages = False
				overwrite.read_messages = True
				await channel.set_permissions(member, overwrite=overwrite)

				

async def setup(client):
    await client.add_cog(slock(client))
