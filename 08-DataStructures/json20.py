komputer = {
    "procesor":"AMD Ryzen 5",
    "zasilaczV":500,
    "panel_gorny":["USB 3.1 Gen.1", "wejscie mikrofonowe", "wyjscie słuchawkowe"],
    "gwarancja":True,
    "porty_wewnetrzne":{"PCI-ex16":1, "SataIII":6,"PCI-ex1":3}
}
'''
for k,v in komputer.items():
    print(k,":",v)
    '''
import json
p=json.dumps(komputer, indent=4)
print(p)
with open("komputer.json","w") as file:
    file.write(p)