import discord
import os
from discord.ext import commands
import sys
import requests
import json
import datetime
import time

start_time = time.time()

client = commands.Bot(command_prefix = '-')
client.remove_command("help")


@client.event
async def on_ready():
    await client.change_presence(activity = discord.Streaming(name = 'lul this bot isnt completed', url = 'https://www.twitch.tv/savagepatchboy'))
    print('We have logged in as {0.user}'.format(client))

@client.group(name="help", invoke_without_command=True, aliases=["commands, cmds"])
async def help(ctx, member: discord.Member = None):
    embed=discord.Embed(color=0xa9daea, timestamp=ctx.message.created_at, title="Commands:")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Mod", value="Lists Mod Commands \n**ex.** `-help mod`")
    
    await ctx.send(embed=embed)

@help.command(name="mod")
async def mod(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Mod Commands:")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
    embed.add_field(name="Ban:", value="Bans member (needs admin permission) \n**ex.** `-ban @Gold#1337`")
    embed.add_field(name="Unban:", value="Unbans member (needs admin permission) \n**ex.** `-unban Gold#1337`")
    embed.add_field(name="Kick:", value="Kicks member (needs admin permission) \n**ex.** `-kick @Gold#1337`", inline=False)
    embed.add_field(name="Userinfo:", value="Displays the info of desired user \n**ex.** `-userinfo @Gold#1337`")
    embed.add_field(name="Purge:", value="Deletes any desired amount of messages \n**ex.** `-purge 5`")

    await ctx.send(embed=embed)

@help.command(name="meme")
async def meme(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Meme Commands:")

    await ctx.send(embed=embed)

@client.command(aliases=["cogs"])
async def coglist(ctx):
    if ctx.author.id == 648362981721374723 or 306767358574198786:
        embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Mod Commands:")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.add_field(name="Mod:", value="`-load mod`")
        embed.add_field(name="Meme", value="`-load meme`")
        embed.add_field(name="Automod", value="`-load automod`", inline=False)
        embed.add_field(name="Games", value="`-load games`")

        await ctx.send(embed=embed)
    
    else:
        await ctx.send('Only the bot owner can access this command!')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == 648362981721374723 or 306767358574198786:
        client.load_extension(f'cogs.{extension}')
        await ctx.send('Cog loaded')
    
    else:
        await ctx.send("This is an bot owner only command")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 648362981721374723 or 306767358574198786:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog unloaded')
    
    else:
        await ctx.send("This is an bot owner only command!")


@client.command()
async def weather(ctx):

  await ctx.send("Please enter a city name!")
  cityName = await client.wait_for("message")
  name = str(cityName.content)
  if ctx.author == cityName.author:
    try:
      r = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+str(cityName.content)+"&appid=ff4c64d9183dbb2893d31ae24cc39ca9")
      json_object = r.json()
      temp_k = float(json_object['main']['temp'])
      temp_f = (temp_k - 273.15) * 1.8 + 32
      
      climate = r.json()["weather"]
      cd = climate[0]["main"]
      
      middle = 50
      
      if temp_f > middle:
        embed = discord.Embed(timestamp=ctx.message.created_at, title=f"Weather for **{name}**:")
        embed.add_field(name="Tempature in " + f"*{name}*:", value="🥵 " + str(round(temp_f)) + "°F")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))

        
        await ctx.send(embed=embed)

      elif temp_f < middle:
        embed = discord.Embed(timestamp=ctx.message.created_at, title=f"Weather for **{name}**:")
        embed.add_field(name="Results for " + f"*{name}*:", value="🥶 " + str(round(temp_f)) + "°F")
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))
        
        await ctx.send(embed=embed)
      
      else:
        await ctx.send("Error!")
    
    except:
      await ctx.send(name + " does not exist!")
      
  
  elif not ctx.author == cityName.author:
    await ctx.send("bruh u aint the message author")

@client.command()
async def leks(ctx):
    if ctx.author.id == 648362981721374723:
        await ctx.send("nobody asked leks")
    else:
        await ctx.send("u suck")

@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=ctx.message.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    try:
        await ctx.send(embed=embed)
        
        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json") as json_file:
            json_decoded = json.load(json_file)
        
        json_decoded['uptime'] = text
        
        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json", 'w') as json_file:
            json.dump(json_decoded, json_file)

            
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)

@client.command()
async def close(ctx):
    if ctx.author.id == 648362981721374723 or 306767358574198786:

        await ctx.send("Shutting down bot!")
        
        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json") as json_file:
            json_decoded = json.load(json_file)
        
        json_decoded['uptime'] = "Offline"
        
        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json", 'w') as json_file:
            json.dump(json_decoded, json_file)
        
        await quit()
    
    else:
        await ctx.send("Only the owner can close the bot!")

client.run(str(os.environ.get('BOT_TOKEN')))
