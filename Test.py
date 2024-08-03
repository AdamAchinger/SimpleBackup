import json

with open("config.json") as config: 
    data = json.loads(config.read())

for plan_name, plan_details in data.items():
    target_dir_count = len(plan_details["targetDir"])
    print(plan_name)