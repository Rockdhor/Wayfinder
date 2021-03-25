import random
import requests
import json
from bs4 import BeautifulSoup

commands = """```diff
+ Welcome to Wayfinder
Thank you for your interest, here's a list of commands to get you started.

+pokemon show <name>
This command shows a picture of the requested Pokemon.
-name = {pokemon name}

+misu
This command shows a random picture of a cat.

+help
This command displays this message.
```"""

def get_pokemon(id):
  name = id.capitalize()
  url = "https://www.pokemon.com/us/pokedex/" + name
  response = requests.get(url)
  results = BeautifulSoup(response.text, 'html.parser')
  try:
    sprite = results.find("div", class_="profile-images").img['src']
  except:
    return None
    
  print(sprite)
  
  return (name, sprite)

def get_misu():
  url = "https://api.thecatapi.com/v1/images/search"
  response = requests.get(url)
  json_date = json.loads(response.content)
  return json_date[0]['url']

def get_commands():
  return (commands)