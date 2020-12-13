# advent of code day 13 part 2

with open("dec13a.txt") as f:
    data = f.readlines()

mytime = int(data[0])

available = list(map(lambda x: x if x=='x' else int(x), data[1].strip().split(',')))
maxid = max(filter(lambda x: x!='x', available)))

t = mytime
finished = True
while not finished:
    for bus in available:
        if not t%bus:
            result = bus*(t-mytime)
            finished = True
    t += 1

print(result)
