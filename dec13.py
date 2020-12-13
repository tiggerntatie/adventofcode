# advent of code day 13

with open("dec13a.txt") as f:
    data = f.readlines()

mytime = int(data[0])
available = filter(lambda x: x!='x', data[1].strip().split(','))

t = mytime
finished = False
while not finished:
    for bus in available:
        if not t%bus:
            result = bus*(t-mytime)
            finished = True
    t += 1
    
print(result)
