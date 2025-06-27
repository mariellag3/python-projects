import requests
import json

req = requests.get("https://api.chucknorris.io/jokes/random")

print(req.json()["value"])