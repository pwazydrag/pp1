import json
with open("notowania.json") as file:
    data = json.load(file)

for x in data["Rates"]["Rate"]:
    print(x["Currency"], x["Mid"])