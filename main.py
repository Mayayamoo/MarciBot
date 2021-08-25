import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix="?")

@client.command()
async def marci(ctx):
  await ctx.send('fuck marci')

@client.command()
async def lucas(ctx):
  await ctx.send('fuck lucas') or ctx.send('lucas, youre a sweetie pie')
@client.command()
async def ree(ctx):
  await ctx.send("REEEEEEEEEEEE")

@client.command()
async def true(ctx):
  await ctx.send("So True!")

@client.command()
async def genocide(ctx):
  await ctx.send('Genocide bad \U0001F97A')

@client.command()
async def liar(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/787153421174046743/817418073958776892/What_a_weaselly_liar_dude._SOURCE_1.mp4')

@client.command()
async def rosie(ctx):
  await ctx.send ('fuck rosie!')

@client.command()
async def femboymaths(ctx):
  await ctx.send ('follow femboymaths on twitter! theyre soooo cool!')
@client.command()
async  def chloe(ctx):
  await ctx.send('literally a dairy cow')

@client.command()
async def boobs(ctx):
  await ctx.send(' <:MarciPog:810317890124251137>')
keep_alive()
client.run(os.getenv('TOKEN'))
