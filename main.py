import config
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import tokens
import time

client = commands.Bot(command_prefix = config.prefix)

@client.event
async def on_ready():
    if config.customStatus == True:
        await client.change_presence(status = discord.Status.online, activity = discord.Game(config.status))
    
    print("Client ready.")

if config.messageOnJoin == True:
    @client.event
    async def on_member_join(member):
        print(f'{member} ' + config.onMemberJoin)

if config.messageOnRemove == True:
    @client.event
    async def on_member_remove(member):
        print(f'{member} ' + config.onMemberRemove)

@client.event
async def onCommandError(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('I know no such thing.')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ["8ball", "8Ball"])
async def _8Ball(ctx, *, question):
    responses = ["Certainly!", "Absolutely.", "Without a doubt.", "Yes. For definite.", "You can rely on it.", "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.", "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now", "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.", "Doesn't look too good to me.", "more like a no..."]
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
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Kicked {member.mention} ")
    if reason == None:
        print(f"Kicked {member.name}#{member.discriminator} - no reason given.")
    elif reason != None:
        print(f"Kicked {member.name}#{member.discriminator} for {reason}")

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if reason == None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for no reason, apparently.")
        print(f"Banned {member.mention} - no reason given.")
    elif reason != None:
        await member.ban(reason = reason)
        await ctx.send(f"Banned {member.mention} for {reason}")
        print(f"Banned {member.mention} for {reason}")

@client.command()
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    memberName, memberDiscriminator = member.split("#")

    for banEntry in bannedUsers:
        user = banEntry.user

        if (user.name, user.discriminator) == (memberName, memberDiscriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"User {user.name}#{user.discriminator} successfully unbanned. Welcome back!")

@client.command()
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit = amount)

@clear.error
async def clearError(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("So, uh, how many messages do you want to delete? Let's try that again shall we?")

@tasks.loop(seconds = 10)
async def changeStatus():
    status = cycle([config.status])
    await client.change_presence(activity = discord.Game(next(status)))

client.run(tokens.token)
