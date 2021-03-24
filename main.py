import discord
import os
import requests
import json
import random
from replit import db
import handlers
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
  if message.author == client:
    return 

  msg = message.content

  if msg.startswith('「enseñame a'):
    name = msg.split()[2]
    pkmn = handlers.get_pokemon(name)
    if pkmn == None:
      await message.channel.send("Hay un tiempo y lugar para todo, pero no para eso.")
    else:
      await message.channel.send("Dale, aqui esta " + pkmn[0] + ".")
      await message.channel.send(pkmn[1])

  if msg.startswith('「misu'):
    await message.channel.send(handlers.get_misu())
  

 
  
    

keep_alive()
client.run(os.getenv('TOKEN'))