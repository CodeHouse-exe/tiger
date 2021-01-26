import config
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import time
from datetime import datetime


def get_time():
    dateTimeObj = datetime.now()
    timeNow = f"{dateTimeObj.hour}:{dateTimeObj.minute}:{dateTimeObj.second}"
    return timeNow


client = commands.Bot(command_prefix=config.prefix)
status = cycle(config.status)


@client.event
async def on_ready():
    global _output
    print(f'[{get_time()}] Client ready.')
    change_status.start()


if config.messageOnJoin:
    @client.event
    async def on_member_join(member):
        global _output
        _output = print(f'[{get_time()}] {member} {config.onMemberJoin}')

if config.messageOnRemove:
    @client.event
    async def on_member_remove(member):
        global _output
        print(f'[{get_time()}] {member} {config.onMemberRemove}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(config.commandNotFound)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")


@client.command(aliases=["8ball", "8Ball"])
async def _8_ball(ctx, *, question):
    responses = config._8_ball_responses
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")


@client.command()
async def spam(ctx, amount: int):
    time.sleep(2)
    for index in range(0, amount):
        await ctx.send(f"Spam")
        index += 1


@spam.error
async def spam_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(config.spamMissingArg)


@client.command(aliases=["surprise", "rr"])
async def rickroll(ctx):
    rr = open("tiger/rickroll.txt", "r")
    await ctx.send(f"Here goes. \nReady?")
    time.sleep(2)
    for word in rr:
        await ctx.send(word)


@client.command()
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    global _output
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention} ")
    if reason is None:
        print(f'[{get_time()}] Kicked {member.name}#{member.discriminator} - no reason given.')
    elif reason is not None:
        print(f"[{get_time()}] Kicked {member.name}#{member.discriminator} for {reason}")


@client.command()
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    global _output
    if reason is None:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} for no reason, apparently.")
        print(f"[{get_time()}] Banned {member.mention} - no reason given.")
    elif reason is not None:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention} for {reason}")
        print(f"[{get_time()}] Banned {member.mention} for {reason}")


@client.command()
@commands.bot_has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for banEntry in banned_users:
        user = banEntry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"User {user.name}#{user.discriminator} successfully unbanned. Welcome back!")


@client.command()
@commands.bot_has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(config.clearMissingArg)
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(config.missingPerms)


@tasks.loop(minutes=15)
async def change_status():
    new_status = next(status)
    await client.change_presence(activity=discord.Game(new_status))
    print(f"[{get_time()}] Status set to Playing {new_status}.")


client.run(config.token)
