# advent of code day 14

import re
memread = re.compile(".*\[(\d+)\] = (\d+)")

currmask = 0
mem = {}

with open("dec14a.txt") as f:
    for cmd in f.readlines():
        if cmd[1] == 'a':
            # mask command
            mask = cmd[7:]
        else:
            # mem command
            res = re.search(cmd)
            print(dir(res))
