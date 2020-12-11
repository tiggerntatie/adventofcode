# advent of code 11

with open("dec11a.txt") as f:
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
    
def personfar(x,y):
    tots = 0
    #upleft
    dist = min(x,y)
    for a in range(1,dist+1):
        if persons[y-a][x-a]:
            tots += 1
            break
    #up
    dist = y
    for a in range(1,dist+1):
        if persons[y-a][x]:
            tots += 1
            break
    #upright
    dist = min(w-x-1,y)
    for a in range(1,dist+1):
        if persons[y-a][x+a]:
            tots += 1
            break
    #right
    dist = w-x-1
    for a in range(1,dist+1):
        if persons[y][x+a]:
            tots += 1
            break
    #downright
    dist = min(w-x-1,h-y-1)
    for a in range(1,dist+1):
        if persons[y+a][x+a]:
            tots += 1
            break
    #up
    dist = h-y-1
    for a in range(1,dist+1):
        if persons[y+a][x]:
            tots += 1
            break
    #downleft
    dist = min(x,h-y-1)
    for a in range(1,dist+1):
        if persons[y+a][x-a]:
            tots += 1
            break
    #left
    dist = x
    for a in range(1,dist+1):
        if persons[y][x-a]:
            tots += 1
            break
    return tots

neighblimit = 5  # 5 for part 2, 4 for part 1
while True:
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
                else
                    neighbs = personfar(x,y)
                if neighbs == 0:
                    newpersons[y][x] = 1
                if neighbs >= 5:
                    newpersons[y][x] = 0
    if newpersons == persons:
        print(numpeeps)
        break
    persons = newpersons