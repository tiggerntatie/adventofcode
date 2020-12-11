# advent of code 11

with open("dec11a.txt") as f:
    data = f.readlines()

w = len(data[0])
h = len(data)
persons = [[0 for x in range(w)] for y in range(h)]
persons[1][1]=1
print(persons)

def personat(x,y):
    pass
    