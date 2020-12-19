# advent of code day 18

print("****** advent of code 18 part 2 ******")

with open("dec18.txt") as f:
    data = [x.strip() for x in f.readlines()]


sdigits = [str(i) for i in range(10)]
    
def getnum(e):
    if not e:
        return None, ""
    if e[0] in ['(',')']:
        return e[0], e[1:].strip()
    accum = 0
    if e[0] not in sdigits:
        return None, e
    while e and e[0] in sdigits:
        accum *= 10
        accum += int(e[0])
        e = e[1:]
    return accum, e.strip()

def getoper(e):
    if not e:
        return "", ""
    if e[0] not in ['*','+']:
        return None, e
    return e[0], e[1:].strip()

def gettoken(inp):
    e = inp[::]
    while e and e[0] == ' ':
        e = e[1:]
    if not e:
        return e
    if e and e[0] in [')','(','*','+']:
        return e[0], e[1:]
    elif e and e[0] in sdigits:
        return getnum(e)

def getparen(e):  # scan for unbalanced ) and return before and after text
    level = 1
    for i, c in enumerate(e):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        if level == 0:
            return e[:i], e[i+1:]
    
def evalit(e):
    n = []
    o = []
    #print("entering evalit with ", e)
    while e:
        #print(o, n)
        t, e = gettoken(e)
        if t == '(':
            s, e = getparen(e) # returns parenthetical + rest
            n.append(evalit(s))
        elif t in ['*','+']:
            o.append(t)
        else:
            n.append(t)
            if len(n) == 2 and o[-1] == '+':
                n[-2] = n[-1]+n[-2]
                n.pop()
                o.pop()
    #print("stripping +")
    while '+' in o:
        #print(o,n)
        i = o.index('+')
        n[i] = n[i]+n[i+1]
        n.pop(i+1)
        o.pop(i)
    #print(o,n)
    while o:
        if o[-1] == "*":
            n[-2] = n[-2]*n[-1]
        o.pop()
        n.pop()
    #print("leaving evalit with ", n[0])
    return n[0]      
                    
    
tots = 0
for expr in data:
    tots += evalit(expr)        
#print(evalit(data[4]))

print(tots)