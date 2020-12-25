import discord
import os
from discord.ext import commands
import sys
import requests
import json
import datetime
import time


start_time = time.time()

client = commands.Bot(command_prefix='-')
client.remove_command("help")


async def api():
    time.sleep(1)
    while True:
        r = requests.get("https://www.jaden.cf/api/bY5wd6iPS2jxubp0")
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\puk.json") as json_file:
            json_decoded = json.load(json_file)

        json_decoded['uptime'] = text

        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\puk.json", 'w') as json_file:
            json.dump(json_decoded, json_file)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='puck 57% python 43% javascript', url='https://www.twitch.tv/savagepatchboy'))
    print('We have logged in as {0.user}'.format(client))


@client.group(name="help", invoke_without_command=True, aliases=["commands, cmds"])
async def help(ctx, member: discord.Member = None):
    embed = discord.Embed(
        color=0xa9daea, timestamp=ctx.message.created_at, title="Commands:")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Mod", value="Lists Mod Commands \n**ex.** `-help mod`")
    embed.add_field(
        name="Music", value="Lists Music Commands \n**ex.** `-help music`")

    await ctx.send(embed=embed)


@help.command(name="mod")
async def mod(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(
        color=0x5207df, timestamp=ctx.message.created_at, title="Mod Commands:")
    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
    embed.add_field(
        name="Ban:", value="Bans member (needs admin permission) \n**ex.** `-ban @Gold#1337`")
    embed.add_field(
        name="Unban:", value="Unbans member (needs admin permission) \n**ex.** `-unban Gold#1337`")
    embed.add_field(
        name="Kick:", value="Kicks member (needs admin permission) \n**ex.** `-kick @Gold#1337`", inline=False)
    embed.add_field(
        name="Userinfo:", value="Displays the info of desired user \n**ex.** `-userinfo @Gold#1337`")
    embed.add_field(
        name="Purge:", value="Deletes any desired amount of messages \n**ex.** `-purge 5`")
    embed.add_field(
        name="Serverinfo:", value="Displays server information \n**ex.** `-serverinfo`")

    await ctx.send(embed=embed)


@help.command(name="meme")
async def meme(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(
        color=0x5207df, timestamp=ctx.message.created_at, title="Meme Commands:")

    await ctx.send(embed=embed)


@help.command(name="music")
async def music(ctx):
    embed = discord.Embed(
        color=0x3509ae, timestamp=ctx.message.created_at, title="Music Commands:")
    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
    embed.add_field(
        name="Play:", value="Plays a song \n**ex.** `-play <youtube link>`")
    embed.add_field(
        name="Skip:", value="Skips song in queue \n**ex.** `-skip`")
    embed.add_field(
        name="Stop:", value="Stops/clears the queue \n**ex.** `-stop`", inline=False)
    embed.add_field(
        name="Join:", value="Joins the users voice channel \n**ex.** `-join`")
    embed.add_field(
        name="Leave:", value="Leaves the users voice channel \n**ex.** `-leave`")
    embed.add_field(
        name="Loop:", value="Loops the current song \n**ex.** `-loop`")
    embed.add_field(
        name="Volume:", value="Adjusts the volume \n**ex.** `-volume <num 0-2>`")
    embed.add_field(
        name="Search:", value="Searches for a song\n**ex.** `-search`")

    await ctx.send(embed=embed)


@client.command()
async def stats(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(
        color=0x3509ae, timestamp=ctx.message.created_at, title="Stats:")
    guilds = len([s for s in client.guilds])
    r = requests.get("https://puckpanel.glitch.me/api/stats")
    users = r.json()
    all = int(users['members'])

    embed.add_field(name="Server Count", value=guilds, inline=True)

    embed.add_field(name="User Count", value=all, inline=True)

    embed.add_field(
        name="Uptime:", value=f"{text}"
    )

    embed.add_field(
        name="Operating System", value=f"Windows 10 Home x64", inline=False
    )

    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@client.command()
async def owner(ctx):
    if ctx.author.id == 648362981721374723:
        embed = discord.Embed(
            color=0x3509ae, timestamp=ctx.message.created_at, title="Owner cmds")

        embed.add_field(
            name="Cogslist", value="Shows avalible cogs to load"
        )
        embed.add_field(
            name="start", value="starts the uptime api timer"
        )

        await ctx.send(embed=embed)

    else:
        await ctx.send("You're not the bot owner!")


@client.command(aliases=["cogs"])
async def coglist(ctx):
    if ctx.author.id == 648362981721374723:
        embed = discord.Embed(
            color=0x5207df, timestamp=ctx.message.created_at, title="Mod Commands:")
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.add_field(name="Mod:", value="`-load mod`")
        embed.add_field(name="Meme", value="`-load meme`")
        embed.add_field(name="Automod", value="`-load automod`", inline=False)
        embed.add_field(name="Games", value="`-load games`")
        embed.add_field(name="Channel", value="`-load channel`")

        await ctx.send(embed=embed)

    else:
        await ctx.send('Only the bot owner can access this command!')


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 648362981721374723:
        client.load_extension(f'cogs.{extension}')
        await ctx.send('Cog loaded')

    else:
        await ctx.send("This is an bot owner only command")


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 648362981721374723:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog unloaded')

    else:
        await ctx.send("This is an bot owner only command!")


@client.command()
async def weather(ctx, *, args):
    name = args
    try:
        r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +
                         name + "&appid=ff4c64d9183dbb2893d31ae24cc39ca9")
        json_object = r.json()
        temp_k = float(json_object['main']['temp'])
        temp_f = (temp_k - 273.15) * 1.8 + 32

        climate = r.json()["weather"]
        cd = climate[0]["main"]

        middle = 50

        if temp_f > middle:
            embed = discord.Embed(
                timestamp=ctx.message.created_at, title=f"Weather for **{name}**:")
            embed.add_field(
                name="Tempature in " + f"*{name}*:", value="🥵 " + str(round(temp_f)) + "°F")
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))

            await ctx.send(embed=embed)

        elif temp_f < middle:
            embed = discord.Embed(
                timestamp=ctx.message.created_at, title=f"Weather for **{name}**:")
            embed.add_field(
                name="Results for " + f"*{name}*:", value="🥶 " + str(round(temp_f)) + "°F")
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))

            await ctx.send(embed=embed)

        else:
            await ctx.send("Error!")

    except:
        await ctx.send(name + " does not exist!")


@client.command()
async def leks(ctx):
    if ctx.author.id == 648362981721374723:
        await ctx.send("nobody asked leks")
    else:
        await ctx.send("u suck")


@client.command()
async def start(ctx):
    await api()


@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(
        colour=ctx.message.author.top_role.colour, timestamp=ctx.message.created_at)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(
        text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
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
    if ctx.author.id == 648362981721374723:

        await ctx.send("Shutting down bot!")

        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json") as json_file:
            json_decoded = json.load(json_file)

        json_decoded['uptime'] = "Offline"

        with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json", 'w') as json_file:
            json.dump(json_decoded, json_file)

        await quit()

    else:
        await ctx.send("Only the owner can close the bot!")

client.run(str(os.environ.get('BOTTOKEN')))
#need to crash the bot for testing purposes.
