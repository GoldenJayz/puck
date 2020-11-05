import discord
import os
from discord.ext import commands
import sys

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
    embed.add_field(name="Mod", value="Lists Mod Commands \n**ex.** `-commands mod`")
    
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

@client.command()
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
async def cogs(ctx):
    if ctx.author.id == 648362981721374723 or 306767358574198786:
        
        em = discord.Embed( 
            title='Cogs',
            description='',
            colour = discord.Colour.orange()
        )
        await ctx.send('', embed=em)
    
    else:
        await ctx.send('Only the bot owner can access this command!')

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 648362981721374723 or 306767358574198786:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send('Cog unloaded')
    
    else:
        await ctx.send("This is an bot owner only command!")

client.run(str(os.environ.get('BOT_TOKEN')))
