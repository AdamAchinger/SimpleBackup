import json

with open("config.json") as config: 
    data = json.loads(config.read())

print(data)