# advent of code day 8

with open("dec08a.txt") as f:
    data = [x.split() for x in f.readlines()]
    
data = [[x[0],int(x[1])] for x in data]
#print(data)

length = len(data)
acc = 0
def isloop():
    pc = 0
    global acc
    acc = 0
    visited = set()
    while not pc in visited:
        visited.add(pc)
        instr = data[pc]
        if instr[0] == "acc":
            acc += instr[1]
            pc += 1
        elif instr[0] == "jmp":
            pc += instr[1]
        else:
            pc += 1
        if pc == length:
            return False
    return True

for n, line in enumerate(data):
    old = line[0]
    if old == 'jmp':
        data[n][1] = 'nop'
    elif old == 'nop':
        data[n][1] = 'jmp'
    if isloop():
        data[n][1] = old
    else:
        break

print(acc)