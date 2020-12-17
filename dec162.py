# advent of code day 16
print("*******part2***********")
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
yournums = []
goodtickets = []
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
                fielddict[fd[0]] = set()
                for i in range(t[0],t[1]+1):
                    okset.add(i)
                    fielddict[fd[0]].add(i)
                for i in range(max(t[1],t[2]),t[3]+1):
                    okset.add(i)
                    fielddict[fd[0]].add(i)
        else:  # your or nearbystate
            if yourtickstate:
                yournums = [int(x) for x in field.split(',')]
                yourtickstate = False
                taketwo = True
            else:
                nums = [int(x) for x in field.split(',')]
                if all([x in okset for x in nums]):
                    # valid ticket
                    goodtickets.append(nums)
               
# process our data
fieldsavailable = [x for x in fielddict]
fielddef = {}  # map field name to position
positionsavailable = list(range(len(goodtickets[0])))
while len(fielddef) < len(fielddict):
    for i in positionsavailable:
        candidate = None
        candidatecount = 0
        for field in fieldsavailable:
            #print("check", field, "at position", i)
            if all([ticket[i] in fielddict[field] for ticket in goodtickets]):
                candidatecount += 1
                candidate = (field, i)
        if candidatecount == 1:
            fielddef[candidate[0]] = candidate[1]
            fieldsavailable.remove(candidate[0])
            positionsavailable.remove(candidate[1])
            print("found ", candidate)
            print("fields left", fieldsavailable)
            print("positions left", positionsavailable)
        
prod = 1
for field in fielddef:
    if field.find("departure") == 0:
        prod *= yournums[fielddef[field]]

# validate our conclusions
for field in fielddict:
    i = fielddef[field]
    for tick in goodtickets:
        if tick[i] not in fielddict[field]:
            print("oops")
        
print(yournums)
print(fielddef)
print(prod)
    
    