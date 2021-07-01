import discord
from discord.ext import commands
import random
import time
import os
import json

os.chdir("C:\\Users\\RAMESH\\PycharmProjects\\Official Bot")
limages = [
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/384.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/383.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/382.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/483.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/484.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/487.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/250.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/244.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/245.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/243.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/146.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/145.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/144.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/718.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/717.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/716.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/377.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/378.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/379.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/380.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/381.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/480.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/481.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/482.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/485.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/486.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/488.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/638.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/639.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/640.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/641.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/642.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/643.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/644.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/645.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/646.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/785.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/786.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/787.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/788.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/789.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/790.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/791.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/792.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/800.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/888.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/889.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/890.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/891.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/892.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/893.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/894.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/895.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/896.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/897.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/898.png"
]

mimages = [
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/719.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/491.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/151.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/251.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/385.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/386.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/489.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/490.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/492.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/493.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/494.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/647.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/648.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/649.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/720.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/721.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/801.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/802.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/807.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/808.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/809.png",
]

ubs = [
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/793.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/794.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/795.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/796.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/797.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/798.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/799.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/803.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/804.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/805.png",
    "https://assets.pokemon.com/assets/cms2/img/pokedex/full/806.png"
]

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("bot is ready")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Please check your Permissions")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arg.")
        await ctx.message.delete()
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Please check your command.")
        await ctx.message.delete()
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Please check to whom you Mention.")
        await ctx.message.delete()
    else:
        raise error


@client.command(aliases=['Hi', 'hi'])
async def hello(ctx):
    await ctx.send("Hi")


@client.command()
async def status(ctx):
    await ctx.send("Welcome to the server. We are growing this server, so pls support us.")


@client.command(aliases=["purge"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="no reason provided"):
    await member.send(member.mention + "has been kicked from Ash's Hometown, because =" + reason)
    await member.kick(reason=reason)


@client.command(aliases=["b"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="no reason provided"):
    await member.send(member.name + "has been banned from Ash's Hometown, Because:" + reason)
    await member.ban(reason=reason)


@client.command(aliases=["ub"])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user
        if (user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + "has been unbanned!")
            return

    await ctx.send(member + "was not found")


@client.command(aliases=["m"])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(846793370725515264)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + "has been muted")


@client.command(aliases=["um"])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(846793370725515264)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + "has been unmuted")


@client.command()
@commands.has_permissions(kick_members=True)
async def whois(ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, discription=member.mention, colour=discord.Colour.red())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Made by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command(aliases=["ls"])
async def lspawn(ctx):
    embed = discord.Embed(colour=discord.Colour.red())

    random_link = random.choice(limages)

    embed.set_image(url=random_link)

    await ctx.send(embed=embed)


@client.command(aliases=["ms"])
async def mspawn(ctx):
    bruh = discord.Embed(colour=discord.Colour.red())

    random_choice = random.choice(mimages)

    bruh.set_image(url=random_choice)

    await ctx.send(embed=bruh)


@client.command(aliases=["ubs"])
async def ubspawn(ctx):
    hell = discord.Embed(colour=discord.Colour.red())

    random_no = random.choice(ubs)

    hell.set_image(url=random_no)

    await ctx.send(embed=hell)


@client.command()
async def timer(ctx):
    time.sleep(15)
    await ctx.send("15 sec ended")


@client.command(aliases=["bal"])
async def balance(ctx):
    user = ctx.author
    await open_account(ctx.author)

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s Balance")
    em.add_field(name="Wallet Balance", value=wallet_amt)
    em.add_field(name="Bank Balance", value=bank_amt)
    await ctx.send(embed=em)


@client.command()
async def beg(ctx):
    user = ctx.author
    await open_account(ctx.author)

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you {earnings} coins")

    users[str(user.id)]["wallet"] += earnings

    with open("Data.json", "w")as f:
        json.dump(users, f)



async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 50
        users[str(user.id)]["bank"] = 100

    with open("Data.json", "w")as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("Data.json", "r") as f:
        users = json.load(f)

    return users




client.run("ODQ4NDY3NTIxOTY2MzA5NDE2.YLNC9Q.o7P5yH7nYOEi9FwL5r4wXbxJIjY")
