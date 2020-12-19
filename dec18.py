# advent of code day 18

print("****** advent of code 18 ******")

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

def evalit(e):
    mye = e
    os = []
    ns = []
    while (mye or os):
        if len(ns) >= 3 and ns[-1] == ')' and ns[-3] == '(':
                ns.pop()
                ns.pop(-2)
        elif os and len(ns) >= 2 and type(ns[-1]) is int  and type(ns[-2]) is int:
            if os[-1] == '*':
                ns[-2] = ns[-1]*ns[-2]
            else:
                ns[-2] = ns[-1]+ns[-2]
            ns.pop()
            os.pop()
        else:
            o, mye = getoper(mye)
            if o:
                os.append(o)
            else:
                n, mye = getnum(mye)
                if n != None:
                    ns.append(n)
    return ns[0]
    
    
tots = 0
for expr in data:
    tots += evalit(expr)        

print(tots)