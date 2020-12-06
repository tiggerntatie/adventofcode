# dec02.py
#
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
#
# How many passwords are valid?
import re

count = 0
prog = re.compile("(\d+)-(\d+) (\S): (\S+)")
with file("dec02.txt") as f:
    pwds = f.readlines()
    for p in pwds:
        m = prog.search(p).groups()
        c = m[3].count(m[2])
        if m[0] <= c <= m[1]:
            count += 1
print(count)
