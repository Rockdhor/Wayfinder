import discord
import os
import requests
import json
import random
from replit import db
import handlers
from keep_alive import keep_alive

client = discord.Client()
listener = "$"

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

@client.event
async def on_message(message):
  if message.author == client:
    return 

  msg = message.content

  if msg.startswith(listener+'pokemon show'):
    name = msg.split()[2]
    pkmn = handlers.get_pokemon(name)
    if pkmn == None:
      await message.reply("Oak's words echoed... There's a time and place for everything, but not now.")
    else:
      embed = discord.Embed(title=pkmn[0]) #https://pokeapi.co/api/v2/version/1/
      embed.set_image(url=pkmn[1])
      response = await message.reply(embed = embed)
      #response = await message.reply("*"+pkmn[0]+"*")
      #pic = (await message.channel.send(""+pkmn[1]).id)
      await response.add_reaction("⬅️")
      await response.add_reaction("➡️")
    return
  if msg.startswith(listener+'misu'):
    await message.reply(handlers.get_misu())
    return
  if msg.startswith(listener+'help'):
    await message.reply("All right! Check your private messages.")
    await message.author.send(handlers.get_commands())
    return
 
  
    

keep_alive()
client.run(os.getenv('TOKEN'))