# advent of code day 8

with open("dec08a.txt") as f:
    data = [x.split() for x in f.readlines()]
    
data = [(x[0],int(x[1])) for x in data]
print(data)

pc = 0
acc = 0
visited = set()

while pc not in visited:
    visited.add(pc)
    instr = data[pc]
    if instr[0] == "acc":
        acc += instr[1]
    elif instr[0] == "jmp":
        pc += instr[1]

print(acc)