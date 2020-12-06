# dec02.py
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
#
# How many passwords are valid?
import re

count = 0
count2 = 0
prog = re.compile("(\d+)-(\d+) (\S): (\S+)")
with open("dec02.txt") as f:
    pwds = f.readlines()
    for p in pwds:
        m = prog.search(p).groups()
        c = m[3].count(m[2])
        a = int(m[0])
        b = int(m[1])
        if a <= c <= b:
            count += 1
        if (m[3][a-1] == m[2]) != (m[3][b-1] == m[2]):
            count2 += 1
print(count)
print(count2)
