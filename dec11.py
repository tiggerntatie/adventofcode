# advent of code 11

with open("dec11.txt") as f:
    data = f.readlines()

w = len(data[0])
h = len(data)
persons = [[0 for x in range(w)] for y in range(h)]

def personnear(x,y):
    tots = 0
    if x > 0:
        tots += persons[y][x-1]
        if y > 0:
            tots += persons[y-1][x-1]
        if y < h-1:
            tots += persons[y+1][x-1]
    if x < w-1:
        tots += persons[y][x+1]
        if y > 0:
            tots += persons[y-1][x+1]
        if y < h-1:
            tots += persons[y+1][x+1]
    if y > 0:
        tots += persons[y-1][x]
    if y < h-1:
        tots += persons[y+1][x]
    return tots

chairmap = {}
# get list of coordinate tuples of nearby chairs
def nearchairs(x,y):
    nears = []
    #upleft
    dist = min(x,y)
    for a in range(1,dist+1):
        if data[y-a][x-a]=='L':
            nears.append((x-a,y-a))
            break
    #up
    dist = y
    for a in range(1,dist+1):
        if data[y-a][x]=='L':
            nears.append((x,y-a))
            break
    #upright
    dist = min(w-x-1,y)
    for a in range(1,dist+1):
        if data[y-a][x+a]=='L':
            nears.append((x+a,y-a))
            break
    #right
    dist = w-x-1
    for a in range(1,dist+1):
        if data[y][x+a]=='L':
            nears.append((x+a,y))
            break
    #downright
    dist = min(w-x-1,h-y-1)
    for a in range(1,dist+1):
        if data[y+a][x+a]=='L':
            nears.append((x+a,y+a))
            break
    #up
    dist = h-y-1
    for a in range(1,dist+1):
        if data[y+a][x]=='L':
            nears.append((x,y+a))
            break
    #downleft
    dist = min(x,h-y-1)
    for a in range(1,dist+1):
        if data[y+a][x-a]=='L':
            nears.append((x-a,y+a))
            break
    #left
    dist = x
    for a in range(1,dist+1):
        if data[y][x-a]=='L':
            nears.append((x-a,y))
            break
    chairmap[(x,y)]=nears
    
    


neighblimit = 5  # 5 for part 2, 4 for part 1
# map out the chairs
print(w,h)
for x in range(w):
    for y in range(h):
        if data[y][x] == 'L':
            nearchairs(x,y)

iterations = 0
while iterations < 5:
    iterations += 1
    newpersons = [[0 for x in range(w)] for y in range(h)]
    numpeeps = 0
    for x in range(w):
        for y in range(h):
            if data[y][x] == 'L':
                peep = persons[y][x]
                numpeeps += peep
                newpersons[y][x]=peep
                if neighblimit == 4:
                    neighbs = personnear(x,y)
                else:
                    neighbs = sum([persons[c[1]][c[0]] for c in chairmap[(x,y)]])
                if neighbs == 0:
                    newpersons[y][x] = 1
                if neighbs >= neighblimit:
                    newpersons[y][x] = 0
    if newpersons == persons:
        print(numpeeps)
        break
    persons = newpersons