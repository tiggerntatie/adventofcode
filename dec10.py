# advent of code day 10

with open("dec10a.txt") as f:
    data = [0] + sorted([int(x) for x in f.readlines()])

print(data)

last = 0
ones = 0
threes = 0
for i,j in enumerate(data[1:]):
    d = j-data[i]
    print(d)
    if d == 1:
        ones += 1
    elif d == 3:
        threes += 1
threes += 1

print(ones*threes)