# advent of code day 3

data = ["..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))

with open("dec03.txt") as f:
    data = f.readlines()
    
w = len(data[0])
for xstep, ystep in slopes:
    y = 0
    x = 0
    count = 0
    while y < len(data):
        if data[y][x%w] == '#':
            count += 1
        x += xstep
        y += ystep
    
print(count)