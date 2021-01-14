import discord
from discord.ext import commands
import config

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Client ready.")

@client.event
async def on_member_join(member):
    print(f'{member} ' + config.onMemberJoin)

@client.event
async def on_member_remove(member):
    print(f'{member} ' + config.onMemberRemove)

client.run("Nzk5MzQzNjE0NDU0NjYxMTYw.YACMwA.DFOIdhF7Q3zIx00kIl9PS0n7ib0")

