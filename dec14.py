# advent of code day 14

import re
memread = re.compile(".*\[(\d+)\] = (\d+)")

currpassmask = 0
currsetmask = 0
mem = {}

with open("dec14a.txt") as f:
    for cmd in f.readlines():
        if cmd[1] == 'a':
            # mask command
            mask = cmd[7:]
            currpassmask = int('0b'+mask.replace('1','0').replace('X','1'), 2)
            currsetmask = int('0b'+mask.replace('X','0'), 2)
        else:
            # mem command
            res = memread.match(cmd)
            addr, val = (int(x) for x in res.groups())
            mem[addr] = (val & currpassmask) | currsetmask

print(sum(mem.values()))