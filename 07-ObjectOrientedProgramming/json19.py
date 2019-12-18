import json
with open("euro.json") as file:
    data = json.load(file)
for k,v in data.items():
    print(k,":",v)