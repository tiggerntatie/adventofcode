# advent of code day 12

with open("dec12.txt") as f:
    data = [s.strip() for s in f.readlines()]

sin = {0:0, 90:1, 180:0, 270:-1}
cos = {0:1, 90:0, 180:-1, 270:0}
    
x = y = dir = 0
for op, val in [(x[:1],int(x[1:])) for x in data]:
    if op == 'N':
        y += val
    elif op == 'S':
        y -= val
    elif op == 'E':
        x += val
    elif op == 'W':
        x -= val
    elif op == 'R':
        dir -= val
    elif op == 'L':
        dir += val
    else:
        x += val*cos[dir%360]
        y += val*sin[dir%360]

print(abs(x)+abs(y))