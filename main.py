import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")
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
	await client.change_presence(activity=discord.Streaming(name='Puck goes brrrrrrrr', url='https://www.twitch.tv/savagepatchboy'))
	for e in extensions:
		client.load_extension(e)

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


# @client.event
# async def on_message(message):
	# if message.content == "-emoji":
		# if ":" == message.content[0] and ":" == message.content[-1]:
			# emoji = message.content[1:-1]
			# string the emoji name and id together then say it back
		
		



		
		

client.run("NzY3MDg3Nzk4ODA0MjgzNDAz.X4s0Lw.PtZjDiAG8uYQ3Omf2-rhpzgO2CQ")
