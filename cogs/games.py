import discord
from discord.ext import commands
import datetime
import random
from PIL import Image
from io import BytesIO


class games(commands.Cog):

    def __init__(self, client):
        self.client = client
        

    async def editimage(self, embed, first, target):
        IMAGE = Image.open("heart.jpg")
        AUTHOR_PFP = first.avatar
        TARGET_PFP = target.avatar
        AUTHOR_DATA = BytesIO(await AUTHOR_PFP.read())
        TARGET_DATA = BytesIO(await TARGET_PFP.read())
        APFP = Image.open(AUTHOR_DATA)
        APFP = APFP.resize((354,354))
        TPFP = Image.open(TARGET_DATA)
        TPFP = TPFP.resize((354,354))
        IMAGE.paste(TPFP, (800,212))
        IMAGE.save("/home/server/Desktop/Jaden/puck/profile.jpg")
        IMAGE.paste(APFP, (120,212))
        IMAGE.save("/home/server/Desktop/Jaden/puck/profile.jpg")

    async def lovemaker(self, ctx, embed, first, member):
        resultint: int = random.randrange(0,11)
        stringed_result: str = ""
        EMOJI: str = "<:redbar:870829592326316052>"
        BLANK_EMOJI: str = "<:blackbar:870829932304007168>"
        for i in range(resultint):
            stringed_result += EMOJI
            if i == resultint-1:
                blank_emojis: int = 10 - resultint
                for x in range(blank_emojis):
                    stringed_result += BLANK_EMOJI
        if resultint == 0:
            for i in range(10):
                stringed_result += BLANK_EMOJI
            embed.add_field(name=f"{first} <3 {member}", value=f"{resultint}% {stringed_result} <:rip:871045842373591080>")
        else:
            embed.add_field(name=f"{first} <3 {member}", value=f"{resultint}0% {stringed_result}")


    @commands.command(aliases=["8ball"])
    async def ball(self, ctx, *, args):
        randomlist = ['Maybe', 'Yes', 'No', ]
        randomgif = ['https://media3.giphy.com/media/141iprzbEPjCiQ/giphy.gif', 'https://i.imgur.com/akdtE4H.gif',
                     'https://thumbs.gfycat.com/QuestionableMajesticBillygoat-small.gif', ]

        embed = discord.Embed(title="8ball", color=0x0a0505,
                              timestamp=ctx.message.created_at)
        embed.add_field(name=f"Results for *{args}*", value=random.choice(randomlist))
        embed.set_thumbnail(url=(random.choice(randomgif)))
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command()
    async def love(self, ctx, *args: discord.Member):
        if len(args) > 2:
            await ctx.send("You may only provide 2 people")
        elif len(args) == 0:
            await ctx.send("You have to provide atleast 1 other person")
        elif len(args) == 2:
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0xd09adf)
            file = discord.File("/home/server/Desktop/Jaden/puck/profile.jpg", filename="profile.jpg")
            embed.set_image(url="attachment://profile.jpg")
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f"{ctx.author.avatar}")
            author = ctx.author
            await self.lovemaker(ctx, embed, args[0], args[1])
            await self.editimage(embed, args[0], args[1])
            await ctx.send(file=file, embed=embed)
        elif len(args) == 1:
            embed = discord.Embed(timestamp=datetime.datetime.utcnow(), colour=0xd09adf)
            file = discord.File("/home/server/Desktop/Jaden/puck/profile.jpg", filename="profile.jpg")
            embed.set_image(url="attachment://profile.jpg")
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f"{ctx.author.avatar}")
            author = ctx.author
            await self.lovemaker(ctx, embed, author, args[0])
            await self.editimage(embed, author, args[0])
            await ctx.send(file=file, embed=embed)

    @love.error
    async def love_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to mention a person!")

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        member = ctx.author if not member else member
        huglist = ["https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?itemid=7324587", "https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498", "https://media1.tenor.com/images/af76e9a0652575b414251b6490509a36/tenor.gif?itemid=5640885", "https://media1.tenor.com/images/c2156769899d169306d16b063a55d0b2/tenor.gif?itemid=14584871"]
        #i copy and pasted here cause im lazy
        embed = discord.Embed(title="Hug",
                              color=0xd400ff, timestamp=ctx.message.created_at)
        embed.add_field(
            name=f"{ctx.author} hugged {member}!", value=f"*{ctx.author} ran up to {member} and gave them a big fat hug*")
        embed.set_image(url=random.choice(huglist))
        embed.set_footer(
            text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)
    
    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Bro what are you doing!? You cannot hug yourself :(((")


async def setup(client):
    await client.add_cog(games(client))
