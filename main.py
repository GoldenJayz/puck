import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix="-", intents=intents)
client.remove_command("help")

extensions = {
	"cogs.mod",
	"cogs.economy",
	"cogs.channel",
	"cogs.games",
	"cogs.misc",
	"cogs.help"
	#guild cog coming soon
}

#create convo cog

#add new commands to help command
		
@client.event		
async def on_ready():
	"""Puck Initilization"""
	print(f"{client.user} is now online")
	await client.change_presence(activity=discord.Streaming(name="\"I want a women and not a girl\" - Blake", url='https://www.twitch.tv/savagepatchboy'))
	for e in extensions:
		await client.load_extension(e)

#this just makes the bot ignore the commandnotfound error

@client.command()
async def lock(ctx, channel: discord.TextChannel=None):
	member = ctx.author
	role = discord.utils.get(member.guild.roles, name="Gay Fuck")
	channel = channel or ctx.channel
	overwrite = channel.overwrites_for(role)
	overwrite.send_messages = False
	await channel.set_permissions(role, overwrite=overwrite)

	await ctx.send('Channel locked.')


client.run("force pushed my token :/")
