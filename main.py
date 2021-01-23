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
    print(f'[{time.time}] Client ready.')
    changeStatus.start()

if config.messageOnJoin == True:
    @client.event
    async def on_member_join(member):
        print(f'[{time.time}] {member} {config.onMemberJoin}')

if config.messageOnRemove == True:
    @client.event
    async def on_member_remove(member):
        print(f'[{time.time}] {member} {config.onMemberRemove}')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('I know no such thing.')

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
        await ctx.send("So, uh, how many messages do you want me to send? Let's try that again shall we?")

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
    await member.kick(reason = reason)
    await ctx.send(f"Kicked {member.mention} ")
    if reason == None:
        print(f'[{time.time}] Kicked {member.name}#{member.discriminator} - no reason given.')
    elif reason != None:
        print(f"[{time.time}] Kicked {member.name}#{member.discriminator} for {reason}")

@client.command()
@commands.bot_has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    if reason == None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for no reason, apparently.")
        print(f"[{time.time}] Banned {member.mention} - no reason given.")
    elif reason != None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for {reason}")
        print(f"[{time.time}] Banned {member.mention} for {reason}")

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
        await ctx.send("So, uh, how many messages do you want to delete? Let's try that again shall we?")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that. Ask an admin")

@tasks.loop(minutes=config.statusInterval)
async def changeStatus():
    await client.change_presence(activity=discord.Game(next(status)))

client.run(tokens.token)
