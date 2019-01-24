# permission 67584
# for example: !shopifydelay 50 10 will return 660ms.

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

token = open('token.txt','r').read()

@client.event
async def on_ready():
    print('Started the bot.')
    await client.change_presence(game=discord.Game(name="Calculating..."))

@client.command()
async def shopifydelay(*args):
    lst = list(args)
    proxynum = int(lst[0])
    tasknum = int(lst[1])
    # shopify will ban around 3200ms, so I am using 3300ms just to be safe.
    delay = 3300/proxynum/tasknum *100
    await client.say(f'Use at a delay around {delay} ms.')

client.run(token)
