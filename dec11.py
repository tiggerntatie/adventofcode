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
        if y < h-1:
            tots += persons[x-1][y+1]
    if x < w-1:
        tots += persons[x+1][y]
        if y > 0:
            tots += persons[x+1][y-1]
        if y < h-1:
            tots += persons[x+1][y+1]
    if y > 0:
        tots += persons[x][y-1]
    if y < h-1:
        tots += persons[x][y+1]
    return tots

cycles = 0
while cycles < 10:
    print(persons)
    cycles += 1
    newpersons = [[0 for x in range(w)] for y in range(h)]
    for x in range(w):
        for y in range(h):
            if data[y][x] == 'L':
                newpersons[x][y]=persons[x][y]
                neighbs = personnear(x,y)
                print(neighbs)
                if neighbs == 0:
                    newpersons[x][y] = 1
                if neighbs >= 4:
                    newpersons[x][y] = 0
    if newpersons == persons:
        print("done")
        break
    persons = newpersons