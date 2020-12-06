# Advent of code 01
def checkfirst(sum, qty, nlist):
    a = nlist[0]
    if not len(nlist):
        return 0
    if (qty == 3):
        if prod := checkfirst(sum-a, 2, nlist[1:]):
            return a*prod
        return checkfirst(sum, 3, nlist[1:])
    else:
        for n in nlist[1:]:
            if a+n == sum:
                return a*n
        return checkfirst(sum, 2, nlist[1:])

with open("dec01.txt") as f:
    nums = [int(x) for x in f.readlines()]
    print("day 1: ", checkfirst(2020, 2, nums))
    print("day 2: ", checkfirst(2020, 3, nums))
    
    