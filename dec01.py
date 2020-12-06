# Advent of code 01
def checkfirst(nlist):
    a = nlist[0]
    if not len(nlist):
        return 0
    for n in nlist[1:]:
        if a+n == 2020:
            return a*n
    return checkfirst(nlist[1:])

with open("dec01.txt") as f:
    nums = [int(x) for x in f.readlines()]
    print(checkfirst(nums))
    