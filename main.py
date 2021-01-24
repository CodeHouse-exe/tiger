import config
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import tokens
import time

client = commands.Bot(command_prefix = config.prefix)
status = cycle(config.status)

@client.event
async def on_ready():
    global _output
    _output = print(f'[{time.time}] Client ready.')
    changeStatus.start()

if config.messageOnJoin == True:
    @client.event
    async def on_member_join(member):
        global _output
        _output = print(f'[{time.time}] {member} {config.onMemberJoin}')

if config.messageOnRemove == True:
    @client.event
    async def on_member_remove(member):
        global _output
        _output = print(f'[{time.time}] {member} {config.onMemberRemove}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(config.commandNotFound)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ["8ball", "8Ball"])
async def _8Ball(ctx, *, question):
    responses = config._8BallResponses
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

@client.command()
async def spam(ctx, amount : int):
    time.sleep(2)
    for index in range(0, amount):
        await ctx.send(f"Spam")
        index += 1

@spam.error
async def spamError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(config.spamMissingArg)

@client.command(aliases = ["surprise", "rr"])
async def rickroll(ctx):
    rr = open("tiger/rickroll.txt", "r")
    await ctx.send(f"Here goes. \nReady?")
    time.sleep(2)
    for word in rr:
        await ctx.send(word)

@client.command()
@commands.bot_has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    global _output
    await member.kick(reason = reason)
    await ctx.send(f"Kicked {member.mention} ")
    if reason == None:
        _output = print(f'[{time.time}] Kicked {member.name}#{member.discriminator} - no reason given.')
    elif reason != None:
        _output = print(f"[{time.time}] Kicked {member.name}#{member.discriminator} for {reason}")

@client.command()
@commands.bot_has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    global _output
    if reason == None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for no reason, apparently.")
        _output = print(f"[{time.time}] Banned {member.mention} - no reason given.")
    elif reason != None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for {reason}")
        _output = print(f"[{time.time}] Banned {member.mention} for {reason}")

@client.command()
@commands.bot_has_permissions(ban_members = True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberDiscriminator = member.split("#")

    for banEntry in bannedUsers:
        user = banEntry.user

        if (user.name, user.discriminator) == (memberName, memberDiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"User {user.name}#{user.discriminator} successfully unbanned. Welcome back!")

@client.command()
@commands.bot_has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

@clear.error
async def clearError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(config.clearMissingArg)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(config.missingPerms)

@tasks.loop(minutes=15)
async def changeStatus():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(config.token)