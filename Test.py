import json

with open("config.json") as config: 
    data = json.loads(config.read())

backupsCount = len(data)

dupa = data.items()["targetDir"]
print(dupa)