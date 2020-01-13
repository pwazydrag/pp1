import re
import collections
tab=[]
with open ('DontMakeMeWait.txt', 'r') as file:
    for line in file:
        t = re.findall('[a-zA-Z]', line)
        for xyz in t:
            xyz = xyz.lower()
            tab.append(xyz)
print(collections.Counter(tab))
#print(tab)
