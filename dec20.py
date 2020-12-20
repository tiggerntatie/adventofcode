# advent of code day 20
import re, math

rtile = re.compile("Tile ([\d]+)")

print("****** advent of code day 20 ******")

with open("dec20.txt") as f:
    data = [x.strip() for x in f.readlines()]
    
while "" in data:
    data.remove("")

    
tild = {}
    
for i in range(0,len(data),11):
    td = data[i:i+11]
    num = rtile.match(td[0]).groups()[0]
    top = td[1]
    right = "".join([x[-1] for x in td[1:]])
    bot = td[-1][::-1]
    left = "".join([x[0] for x in td[-1:0:-1]])
    tild[num] = ((top, right, bot, left),(top[::-1], right[::-1], bot[::-1], left[::-1]))
    
# corner blocks will match exactly two other blocks
corners = []
matchcounts = {}
for n in tild:
    matches = set()
    for i in range(4):
        for k in range(2):
            matchcounts[n] = 0
            count = 0
            for m in tild:
                if n != m:
                    for j in range(4):
                        for l in range(2):
                            if tild[n][k][i] == tild[m][l][j]:
                                #print(n,k,i, "matches", m,l,j)
                                matches.add(m)
                                count += 1
            matchcounts[n] = count
    if len(matches) == 2:
        corners.append(n)

prod = 1
for corner in corners:
    prod *= int(corner)
print(matchcounts['3833'])
print(prod)
print("side of square is: ", math.sqrt(len(tild)))
print(corners)