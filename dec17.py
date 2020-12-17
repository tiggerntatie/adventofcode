# advent of code day 17
print("***** day 17 *****")
ndeltas = []
for dz in [-1,0,1]:
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            if dx or dy or dz:
                ndeltas.append((dx,dy,dz))


def ncount(p):
    tots = 0
    for dv in ndeltas:
        if (p[0]+dv[0], p[1]+dv[1], p[2]+dv[2]) in state:
            tots += 1
    return tots

with open("dec17.txt") as f:
    data = [x.strip() for x in f.readlines()]

state = set()
for y,row in enumerate(data):
    for x,c in enumerate(row):
        if c == "#":
            state.add((x,y,0))


            
for i in range(6):
    newstate = set()
    for c in state:
        n = ncount(c)
        if n == 2 or n == 3:
            newstate.add(c)
        # check for births
        for dx, dy, dz in ndeltas:
            tp = (c[0]+dx, c[1]+dy, c[2]+dz)
            if tp not in state:
                if ncount(tp) == 3:
                    newstate.add(tp)
    state = newstate

print(len(state))
            