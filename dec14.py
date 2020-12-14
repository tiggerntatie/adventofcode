# advent of code day 14

import re
memread = re.compile(".*\[(\d+)\] = (\d+)")

currmask = 0
currsetmask = 0
multipliers = 0
mem = {}
maskcount = n

with open("dec14.txt") as f:
    for cmd in f.readlines():
        if cmd[1] == 'a':
            maskcount += 1
            if maskcount == 10:
                break
            # mask command
            mask = cmd[7:]
            masksetlen = mask.count('X')
            multipliers = []
            found = -1
            for i in range(masksetlen):
                found = mask[::-1].find('X', found+1)
                multipliers.append(2**found)
            currsetmask = int('0b'+mask.replace('X','0'), 2)
            currmask = int('0b'+mask.replace('0','1').replace('X','0'), 2)
        else:
            # mem command
            res = memread.match(cmd)
            addr, val = (int(x) for x in res.groups())
            newaddr = addr & currmask  # clear the X bits
            newaddr |= currsetmask  # set certain bits
            for i in range(2**masksetlen):
                tempaddr = newaddr
                tempi = i
                for n in multipliers:
                    tempaddr += (tempi&1)*n
                    tempi //= 2
                mem[tempaddr] = val

print(sum(mem.values()))