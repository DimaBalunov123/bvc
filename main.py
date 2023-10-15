import discord
from discord.ext import commands

import os, random

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='/', intents = discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def animal(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

bot.run('MTE2MDE2NzUyNjQ0MTk1NTQ0MA.G1LVJJ.wwc5dvssK5d1LzRdB3-JdvrvBQ26BKq5n0fcMY')
