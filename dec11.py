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

while True:
    newpersons = [[0 for x in range(w)] for y in range(h)]
    numpeeps = 0
    for x in range(w):
        for y in range(h):
            if data[x][y] == 'L':
                peep = persons[y][x]
                numpeeps += peep
                newpersons[y][x]=peep
                neighbs = personnear(x,y)
                if neighbs == 0:
                    newpersons[y][x] = 1
                if neighbs >= 4:
                    newpersons[y][x] = 0
    if newpersons == persons:
        print(numpeeps)
        break
    persons = newpersons