# advent of code day 20
import re, math

rtile = re.compile("Tile ([\d]+)")

print("****** advent of code day 20 part 2 ******")

with open("dec20.txt") as f:
    data = [x.strip() for x in f.readlines()]
    
while "" in data:
    data.remove("")

    
tild = {}
    
for i in range(0,len(data),11):
    td = data[i:i+11]
    num = int(rtile.match(td[0]).groups()[0])
    bs = [td[1], "".join([x[-1] for x in td[1:]]), td[-1], "".join([x[0] for x in td[1:]])]
    s = []
    # all permutations of rotation and flippage
    for rot in range(4):
        if rot == 0:
            t = bs
        elif rot == 1:
            t = [bs[3][::-1],bs[0], bs[1][::-1], bs[2]]
        elif rot == 2:
            t = [bs[2][::-1], bs[3][::-1], bs[0][::-1], bs[1][::-1]]
        else:
            t = [bs[1], bs[2][::-1], bs[3], bs[0][::-1]]
        for flip in range(2):
            if flip == 0:
                t = [t[2], t[1][::-1], t[0], t[3][::-1]]
            else:
                t = [t[0][::-1], t[3], t[2][::-1], t[1]]
            s.append(t)
    tild[num] = s
                
# corner blocks will match exactly two other blocks
corners = []
matchcounts = {}

for n in tild:
    matchset = set()
    countlist = []
    for r in tild[n]:
        count = 0
        for m in tild:
            if m != n:
                for s in tild[m]:
                    if r[0] == s[2] or r[2] == s[0] or r[1] == s[3] or r[3] == s[1]:
                        matchset.add(m)
                        count += 1
        countlist.append(count)
    if len(matchset) == 2:
        print("two matches, countlist = ", countlist)
        corners.append(n)

prod = 1
for corner in corners:
    prod *= int(corner)
print(prod)
print("side of square is: ", math.sqrt(len(tild)))
print(corners)

grid = {}
for c in corners:
    grid[(0,0)] = c
    for x in range(12):
        for y in range(12):
            pass
        