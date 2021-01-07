import discord
from discord.ext import commands
import json
from datetime import date

client = commands.Bot(command_prefix="-")
client.remove_command("help")

extensions = {
	"cogs.mod",
	"cogs.economy",
	"cogs.channel",
	"cogs.games",
	"cogs.help",
	"cogs.misc"
	#guild cog coming soon
}

today = date.today()

#create convo cog

#add new commands to help command
		
@client.event		
async def on_ready():
	"""Puck Initilization"""
	print(f"{client.user} is now online")
	await client.change_presence(activity=discord.Streaming(name='Type -help for a list of commands!', url='https://www.twitch.tv/savagepatchboy'))
	for e in extensions:
		client.load_extension(e)
		get = e[-1]
		splicedcogname = e[5:-1] + get
		print(f"Loaded {splicedcogname} extension on {today}")
		with open('//home//pi//Desktop//cogs//loadlog.json') as f:
			load = json.load(f)
		
		#make a json key with the date and the data inside the today date key
		load[f'{today} - {e}'] = f"{e} Loaded successfully on {today}"
		
		with open("//home//pi//Desktop//cogs//loadlog.json", 'w') as f:
			json.dump(load, f, indent = 4, sort_keys=True)

#get the date and display it inside a json key. After this I want to put it into the Api and test out NGROK for hosting.
#log everything into a json file then display it on the website.

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
		
		



		
		


client.run("token")
