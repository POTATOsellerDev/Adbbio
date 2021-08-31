#--------------TO DO-----------------------------------
# Moderation Commands Maybe idk
# Make code not ugly and organize
# Have A unique use to bot so people will use it
# Find a free Host cuz i anit be having a rasberry pi
# cringe tiktoks
#
#
#
#-------------------------------------------------------

#imports
import discord
from discord import colour
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
import random
from random import choice
import requests
import os
import asyncio
from io import BytesIO
#Important Thing or bot will be botshit
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix=">", case_insensitive=True, intents = intents)
@client.event
async def on_ready():
    print('bot started')
    change_status.start()
@tasks.loop(seconds=20)
async def change_status():
    status = [f"On {len(client.guilds)} Server|>help", "with Your Hopes And Dreams",  ">help"]
    await client.change_presence(activity=discord.Game(choice(status)))


#Test Command
@client.command()
async def Hello(ctx):
    await ctx.send("hello")
#ping Command
@client.command()
async def ping(ctx):
    Emb = discord.Embed(title="Ping", description= f"Pong! {round(client.latency * 1000)}ms", color= ctx.author.color)
    await ctx.send(embed=Emb)








#Dont Reveal
client.run('Your token here')
