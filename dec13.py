# advent of code day 13

with open("dec13a.txt") as f:
    data = f.readlines()

mytime = int(data[0])
available = list(map(lambda x: int(x), filter(lambda x: x!='x', data[1].strip().split(','))))

t = mytime
finished = False
while not finished:
    for bus in available:
        print(bus, t, t%bus)
        if not t%bus:
            result = bus*(t-mytime)
            finished = True
    t += 1
    if t-mytime > 1000:
        finished = True
    
print(result)
