import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")
client.remove_command("help")

extensions = {
	"cogs.mod",
	"cogs.economy",
	"cogs.channel",
	"cogs.games",
	"cogs.music",
	"cogs.help",
	"cogs.misc"
	#guild cog coming soon
}

#add did u know command?

#create would you rather command randomized and user selected

#create convo cog

#add new commands to help command
		
@client.event		
async def on_ready():
	"""Puck Initilization"""
	print(f"{client.user} is now online")
	await client.change_presence(activity=discord.Streaming(name='Puck is being tested right now!', url='https://www.twitch.tv/savagepatchboy'))
	for e in extensions:
		client.load_extension(e)

#this just makes the bot ignore the commandnotfound error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return True



# @client.event
# async def on_message(message):
	# if message.content == "-emoji":
		# if ":" == message.content[0] and ":" == message.content[-1]:
			# emoji = message.content[1:-1]
			# string the emoji name and id together then say it back
		
		



		
		

client.run("token goes here")
