import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Client ready.")

client.run("Nzk5MzQzNjE0NDU0NjYxMTYw.YACMwA.DFOIdhF7Q3zIx00kIl9PS0n7ib0")

