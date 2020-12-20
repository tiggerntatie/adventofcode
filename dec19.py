# advent of code day 19
print("******* advent of code day 19 ***********")

import re

rule = re.compile("([\d]+): ([\S]+) ?([\S]+)? ?([\S]+)? ?([\S]+)? ?([\S]+)?")

with open("dec19.txt") as f:
    data = [s.strip() for s in f.readlines()]
    mid = data.index("")
    rules = data[:mid]
    messages = data[mid+1:]

    
ruletree = {}

for r in rules:
    m = rule.match(r)
    n = int(m.groups()[0])
    args = list(filter(lambda x: not x is None, m.groups()[1:]))
    pipe = args.index("|") if "|" in args else None
    if len(args) == 1 and args[0][0] == '"':
        ruletree[n] = args[0][1]  # literal rule
    elif pipe:
        ruletree[n] = [[int(x) for x in args[:pipe]], [int(x) for x in args[pipe+1:]]]
    else:
        ruletree[n] = [[int(x) for x in args],]
        
#print(ruletree)

def getruleslist(nl):  # return a list of rules strings from a list of numbers
    if not nl:
        return [""]
    rules = getrules(nl[0])
    otherrules = getruleslist(nl[1:])
    finalrules = []
    for rule in rules:
        for otherrule in otherrules:
            finalrules.append("".join(rule) + "".join(otherrule))
    return finalrules
                
def getrules(n):  # return a list of rule strings in "aaab" format
    if ruletree[n] in ["a","b"]:
        return [ruletree[n],]
    else:
        finalrules = []
        for vector in ruletree[n]:
            finalrules.extend(getruleslist(vector))
        return finalrules

masterlist = set()
for n in ruletree:
    [masterlist.add(x) for x in getrules(n)]

print(sum([msg in masterlist for msg in messages]))
    
