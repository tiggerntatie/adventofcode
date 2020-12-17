# advent of code day 17 part 2
print("***** day 17 part 2 *****")
ndeltas = []
for dz in [-1,0,1]:
    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            for dq in [-1,0,1]:
                if any([dq,dx,dy,dz]):
                    ndeltas.append((dq,dx,dy,dz))


def ncount(p):
    tots = 0
    for dv in ndeltas:
        if (p[0]+dv[0], p[1]+dv[1], p[2]+dv[2], p[3]+dv[3]) in state:
            tots += 1
    return tots

with open("dec17.txt") as f:
    data = [x.strip() for x in f.readlines()]

state = set()
for y,row in enumerate(data):
    for x,c in enumerate(row):
        if c == "#":
            state.add((x,y,0,0))


            
for i in range(6):
    newstate = set()
    for c in state:
        n = ncount(c)
        if n == 2 or n == 3:
            newstate.add(c)
        # check for births
        for dq, dx, dy, dz in ndeltas:
            tp = (c[0]+dq, c[1]+dx, c[2]+dy, c[3]+dz)
            if tp not in state:
                if ncount(tp) == 3:
                    newstate.add(tp)
    state = newstate

print(len(state))
            