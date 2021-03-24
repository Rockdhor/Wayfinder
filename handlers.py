import random
import requests
import json

def get_pokemon(id):
  id = str(id).lower()
  url = "https://pokeapi.co/api/v2/pokemon/"+id+"/"
  response = requests.get(url)
  if str(response.status_code) == "404":
    return None
  json_date = json.loads(response.content)
  
  

  name = json_date['name']
  name = name.capitalize()
  url = random.choice(json_date['forms'])["url"]
  response = requests.get(url)
  json_date = json.loads(response.content)
  sprite = json_date["sprites"]["front_default"]
  
  return (name, sprite)

def get_misu():
  url = "https://api.thecatapi.com/v1/images/search"
  response = requests.get(url)
  json_date = json.loads(response.content)
  return json_date[0]['url']