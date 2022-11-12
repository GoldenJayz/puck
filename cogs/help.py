import discord
from discord.ext import commands

client = discord.Client()

class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(name="help", invoke_without_command=True, aliases=["commands, cmds"])
    async def help(self, ctx, member: discord.Member = None):
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
        embed.add_field(
            name="Games", value="Lists Games Commands \n**ex.** `-help games`")
        embed.add_field(
            name="Economy", value="Lists Economy Commands \n**ex.** `-help economy`")

        await ctx.send(embed=embed)

    @help.command(name="mod")
    async def mod(self, ctx, member: discord.Member = None):
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
    async def meme(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(
            color=0x5207df, timestamp=ctx.message.created_at, title="Meme Commands:")

        await ctx.send(embed=embed)


    @help.command(name="music")
    async def music(self, ctx):
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

    @help.command(name="games")
    async def games(self, ctx):
        embed = discord.Embed(
            color=0x3509ae, timestamp=ctx.message.created_at, title="Games Commands:")
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.add_field(
            name="8ball:", value="Tests your luck with the 8ball \n**ex.** `-8ball <question>`")
        embed.add_field(
            name="Love:", value="Shows how much love you have for another person! \n**ex.** `-love <user>`")
        embed.add_field(
            name="Hug:", value="Hug somebody! \n**ex.** `-hug <user>`")

        await ctx.send(embed=embed)

    @help.command(name="economy")
    async def economy(self, ctx):
        embed = discord.Embed(
            color=0x3509ae, timestamp=ctx.message.created_at, title="Economy Commands:")
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/767087798804283403/c763a1556e16a62e576fbb98a174a374.png?size=1024")
        embed.add_field(
            name="Balance:", value="Displays your balance \n**ex.** `-balance <user> (optional)`")
        embed.add_field(
            name="Beg:", value="Beg for money like a homeless person! \n**ex.** `-beg`")
        embed.add_field(
            name="Slots:", value="Gamble your money! \n**ex.** `-slots <amount>`")
        embed.add_field(
            name="Withdraw:", value="Withdraw your money from the bank! \n**ex.** `-withdraw <amount>`")
        embed.add_field(
            name="Deposit:", value="Deposit your money from your wallet to the bank! \n**ex.** `-deposit <amount>`")
        embed.add_field(
            name="Give:", value="Give money to anybody! \n**ex.** `-give <user> <amount>`")
        embed.add_field(
            name="Rob:", value="Mug another person just like in Detroit! \n**ex.** `-rob <user>`")
            

        await ctx.send(embed=embed)

#create more fun commands



    
    @commands.command()
    async def test(self, ctx):
        await MyMenu().start(ctx)




def setup(client):
    client.add_cog(help(client))
