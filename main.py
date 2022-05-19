import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Sajbot started')

# @client.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason=reason)

# @client.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason=reason)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def miesmuschel(ctx, *, question):
    responses = [
        'Ja',
        'Nein',
        'Man munckelt',
        'Frag doch einfach nochmal'
        ]
    await ctx.send(f'Frage: {question}? \nAntwort: {random.choice(responses)}')

client.run('')
