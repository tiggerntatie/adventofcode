# advent of code day 13 part 2

with open("dec13a.txt") as f:
    data = f.readlines()
available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(available))}
idlist = [id for id in idmap]

step = idlist[0]
start = 0
answer = 0
for id in idlist[1:]:
    delta = idmap[id]
    print("delta ", delta)
    for i in range(start,step*id,step):
        if not (i+delta)%id:
            # found a divisor of solution
            step = step*id
            start = i    
print(start)

