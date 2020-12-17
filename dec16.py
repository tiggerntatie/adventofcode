# advent of code day 16
print("******************")
import re

fieldspec = re.compile('([^:]+):.([\d]+)-([\d]+) or ([\d]+)-([\d]+)')

with open("dec16.txt") as f:
    data = [x.strip() for x in f.readlines()]
    

okset = set()
fielddict = {}
fieldstate = True
yourtickstate = True
takeone = False
taketwo = False
badsum = 0
for field in data:
    if takeone:
        takeone = False
    elif taketwo:
        takeone = True
        taketwo = False
    else:
        if fieldstate:
            if not field:
                fieldstate = False
                takeone = True
            else:
                fd = fieldspec.match(field).groups()
                t = [int(x) for x in fd[1:]]
                fielddict[fd[0]] = t
                for i in range(t[0],t[1]+1):
                    okset.add(i)
                for i in range(max(t[1],t[2]),t[3]+1):
                    okset.add(i)
        else:  # your or nearbystate
            if yourtickstate:
                nums = [int(x) for x in field.split(',')]
                yourtickstate = False
                taketwo = True
            else:
                nums = [int(x) for x in field.split(',')]
                badsum += sum(filter(lambda x: x not in okset, nums))
  
print(badsum)
