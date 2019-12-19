import json
with open("euro.json") as file:
    data = json.load(file)
print("NBP - 10 ostatnich notowań EURO")
print()
print("Data", "\t\t", "Kurs\t")
print("=============================")
pom=-1
for k,v in data.items():
  if k=="rates":
      for f in v:
          print(f["effectiveDate"],"\t\t", f["mid"])
