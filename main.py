import config
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = config.prefix)

@client.event
async def on_ready():
    print("Client ready.")

if config.messageOnJoin == True:
    @client.event
    async def on_member_join(member):
        print(f'{member} ' + config.onMemberJoin)

if config.messageOnRemove == True:
    @client.event
    async def on_member_remove(member):
        print(f'{member} ' + config.onMemberRemove)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ["8ball"])
async def _8Ball(ctx, *, question):
    responses = ["Certainly!", "So shall be it.", "Without a doubt.", "Yes. For definite.", "You can rely on it.", "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.", "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now", "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.", "Doesn't look to good to me.", "more like a no..."]
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

client.run("Nzk5MzQzNjE0NDU0NjYxMTYw.YACMwA.DFOIdhF7Q3zIx00kIl9PS0n7ib0")