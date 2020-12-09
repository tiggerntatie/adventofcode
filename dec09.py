# advent of code day 9

source = "dec09.txt"
if source == "dec09a.txt":
    preamble = 5
else:
    preamble = 25
    
with open(source) as f:
    data = [int(x) for x in f.readlines()]
    
def validnum(n):
    num = data[n]
    p = data[n-preamble:n]
    for nn in range(len(p)-1):
        x = p[nn]
        if x <= num:
            if num - x in p[nn+1:]:
                return True
    return False

def checkweak(start, val):
    x = start
    tot = data[x]
    while tot < val:
        x += 1
        tot += data[x]
    if tot == val:
        sublist = data[start:x+1]
        return True, min(sublist)+max(sublist)
    return False, 0
    
for nn,x in enumerate(data[preamble:]):
    if not validnum(nn+preamble):
        print(x)
        xfinal = x
        break
        
for nn, x in enumerate(data):
    weak, val = checkweak(nn, xfinal)
    if weak:
        print(val)
        break

