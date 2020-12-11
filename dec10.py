# advent of code day 10

with open("dec10a.txt") as f:
    data = [0] + sorted([int(x) for x in f.readlines()])

print(data)

last = 0
ones = 0
threes = 0
for i,j in enumerate(data[1:]):
    d = j-data[i]
    if d == 1:
        ones += 1
    elif d == 3:
        threes += 1
threes += 1

print(ones*threes)

nodemap = {}
datalen = len(data)

def numpaths(n):
    print("entering", n)
    thisjolt = data[n]
    thesum = 0
    for i in (1,2,3):
        print("branch ", i)
        if n<datalen-i and data[n+i] - thisjolt <= 3:
            thesum += nodemap.get(n+i, numpaths(n+i))
    nodemap[n] = thesum
    return thesum
    
print(numpaths(0))
    