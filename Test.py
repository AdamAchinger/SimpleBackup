import json

with open("config.json") as config: 
    data = json.loads(config.read())

for plan_name, plan_details in data.items():
    print(plan_details["sourceDir"])
