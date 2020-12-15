# advent of code day 15



inp = [0,13,16,17,1,10,6]
#inp = [0,3,6]

# sample solution (2020th number) is 436
print("Starting")
agemap = {}
deltamap = {}
num = 0
first = False
for i in range(30000000):
    if i < len(inp):
        num = inp[i]
        agemap[num] = i
        first = True
    else:
        if first:
            num = 0
        else:
            num = deltamap[num]
        first = num not in agemap
        if not first:
            deltamap[num] = i - agemap[num]
        agemap[num] = i
print(num)