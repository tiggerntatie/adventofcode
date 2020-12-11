# advent of code 11

with open("dec11a.txt") as f:
    data = f.readlines()

w = len(data[0])
h = len(data)
persons = [[0 for x in range(w)] for y in range(h)]

def personnear(x,y):
    tots = 0
    if x > 0:
        tots += persons[x-1][y]
        if y > 0:
            tots += persons[x-1][y-1]
        if y < h-2:
            tots += persons[x-1][y+1]
    if x < w-1:
        tots += persons[x+1][y]
        if y > 0:
            tots += persons[x+1][y-1]
        if y < h-2:
            tots += persons[x+1][y+1]
    if y > 0:
        tots += persons[x][y-1]
    if y < h-1:
        tots += persons[x][y+1]
    return tots

while True:
    newpersons = [[0 for x in range(w)] for y in range(h)]
    numpeeps = 0
    for x in range(w):
        for y in range(h):
            if data[y][x] == 'L':
                peep = persons[x][y]
                numpeeps += peep
                newpersons[x][y]=peep
                neighbs = personnear(x,y)
                if neighbs == 0:
                    newpersons[x][y] = 1
                if neighbs >= 4:
                    newpersons[x][y] = 0
    if newpersons == persons:
        print(numpeeps)
        break
    persons = newpersons