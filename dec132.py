# advent of code day 13 part 2

with open("dec13a.txt") as f:
    data = f.readlines()


available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
#maxid = max(filter(lambda x: x!='x', available))
#minid = min(filter(lambda x: x!='x', available))
idmap = {key:val for val, key in filter(lambda x: x[1]!='x', enumerate(available))}
idlist = [id for id in idmap]

lastn = 0
lastid = idlist[0]
for id in idlist[1:]:
    delta = idmap[id-idmap[lastid]
    print(delta)
    for i in range(0,lastid*id,id):
        print(i)
        if not (i+delta)%id:
            print('**',i)
    


"""
finished = True
while not finished:
    for bus in available:
        if not t%bus:
            result = bus*(t-mytime)
            finished = True
    t += 1
"""
##print(result)
