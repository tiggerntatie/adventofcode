# advent of code day 8

with open("dec08a.txt") as f:
    data = [x.split() for x in f.readlines()]
    
data = [(x[0],int(x[1])) for x in data]
print(data)