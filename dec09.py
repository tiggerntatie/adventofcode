# advent of code day 9

source = "dec09a.txt"
if source == "dec09a.txt":
    preamble = 5
else:
    preamble = 25
    
with open(source) as f:
    data = [int(x) for x in f.readlines()]
    
print(data)
