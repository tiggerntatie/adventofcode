# advent of code day 19
print("******* advent of code day 19 part 2 ***********")

import re, sys

rule = re.compile("([\d]+): ([\S]+) ?([\S]+)? ?([\S]+)? ?([\S]+)? ?([\S]+)?")

fname = "dec19b.txt"
with open(fname) as f:
    data = [s.strip() for s in f.readlines()]
    mid = data.index("")
    rules = data[:mid]
    messages = data[mid+1:]

maxmessage = max([len(s) for s in messages])
    
ruletree = {}

done = False
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

## Add extra rules:
if True:
    ruletree[8] = [[42], [42, 8]]
    ruletree[11] = [[42, 31], [42, 11, 31]]

# return match T/F and remaining message
def matchvector(v, m):
    for n in v:
        if not m:
            # out of message chars
            return False, ""
        if n in ['a','b']:
            if n == m[0]:
                m = m[1:]
            else:
                # mismatched literal. no match.
                return False, ""
        else:
            ok, m = matchrule(n, m)
            if not ok:
                return False, m
    return True, m
            
# return match T/F and remaining message            
def matchrule(n, m):
    step = 0
    for vector in ruletree[n]:
        step += 1
        ok, msg = matchvector(vector, m)
        if ok:
            return True, msg
    return False, msg


"""
bbabbbbaabaabba, ababaaaaaabaaab, and ababaaaaabbbaba
"""
count = 0
for msg in messages:
    ok, m = matchrule(0, msg)
    if ok and not m:
        print(msg)
        count += 1

print(count)            
            
