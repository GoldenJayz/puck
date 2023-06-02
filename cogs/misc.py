import discord
from discord.ext import commands
import requests
import time
import datetime
import json

start_time = time.time()


class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def weather(self, ctx, *, args):
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
                    text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

                embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))

                await ctx.send(embed=embed)

            elif temp_f < middle:
                embed = discord.Embed(
                    timestamp=ctx.message.created_at, title=f"Weather for **{name}**:")
                embed.add_field(
                    name="Results for " + f"*{name}*:", value="🥶 " + str(round(temp_f)) + "°F")
                embed.set_footer(
                    text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

                embed.add_field(name="Sky in " + f"*{name}*:", value=str(cd))

                await ctx.send(embed=embed)

            else:
                await ctx.send("Error!")

        except:
            await ctx.send(name + " does not exist!")

    @commands.command()
    async def owner(self, ctx):
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

    @commands.command(aliases=["cogs"])
    async def coglist(self, ctx):
        if ctx.author.id == 648362981721374723:
            embed = discord.Embed(
                color=0x5207df, timestamp=ctx.message.created_at, title="Mod Commands:")
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
            embed.add_field(name="Mod:", value="`-load mod`")
            embed.add_field(name="Meme", value="`-load meme`")
            embed.add_field(
                name="Automod", value="`-load automod`", inline=False)
            embed.add_field(name="Games", value="`-load games`")
            embed.add_field(name="Channel", value="`-load channel`")

            await ctx.send(embed=embed)

        else:
            await ctx.send('Only the bot owner can access this command!')

    @commands.command()
    async def stats(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(
            color=0x3509ae, timestamp=ctx.message.created_at, title="Stats:")
        guilds = len([s for s in client.guilds])
        r = requests.get("https://puckpanel.glitch.me/api/stats")
        users = r.json()
        all = int(users['members'])
        servers = int(users['guilds'])

        embed.add_field(name="Server Count", value=servers, inline=True)

        embed.add_field(name="User Count", value=all, inline=True)

        embed.add_field(
            name="Uptime:", value=f"{text}"
        )

        embed.add_field(
            name="Operating System", value=f"Windows 10 Home x64", inline=False
        )

        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command()
    async def emoji(self, ctx, args):
        """This was made while listening to mario kart music"""
        if ":" == args[0] and ":" == args[-1]:
            print("args")
        if "<" == args[0] and ">" == args[-1]:
            print(args)
            await ctx.send(args)

        else:
            await ctx.send("You need to send an emoji")
        # check if there is <> in message
        # then get the image of it

        #i need to add more to this later

        # else: await ctx.send("You need to send an emoji!")

    @emoji.error
    async def emoji_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(error)

    @commands.command()
    async def uptime(self, ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(
            colour=ctx.message.author.top_role.colour, timestamp=ctx.message.created_at)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        try:
            await ctx.send(embed=embed)

            with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json") as json_file:
                json_decoded = json.load(json_file)

            json_decoded['uptime'] = text

            with open("C:\\Users\\jmdan\\OneDrive\\Desktop\\Folder\\Coding\\Sites\\app\\static\\puckdata.json", 'w') as json_file:
                json.dump(json_decoded, json_file)

        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)


async def setup(client):
    await client.add_cog(misc(client))
