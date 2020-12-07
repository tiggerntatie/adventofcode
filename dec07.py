# advent of code day 7

data = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags."
    ]
    
data = [
    "shiny gold bags contain 2 dark red bags.",
    "dark red bags contain 2 dark orange bags.",
    "dark orange bags contain 2 dark yellow bags.",
    "dark yellow bags contain 2 dark green bags.",
    "dark green bags contain 2 dark blue bags.",
    "dark blue bags contain 2 dark violet bags.",
    "dark violet bags contain no other bags."
    ]
    
targetbag = "shiny gold bag"

# So, in this example, the number of bag colors that can eventually 
# contain at least one shiny gold bag is 4.

# for each color, build a list of number/color tuples that match

def containscolor(start, target):
    for num, color in color_dict[start]:
        if num:
            if color == target or containscolor(color, target):
                return True
    return False

def containscount(start):
    count = 0
    for num, color in color_dict[start]:
        if num:
            count += num*(1 + containscount(color))
        else:
            return 1
    return count

color_dict = {}

#with open("dec07.txt") as f:
#    data = f.readlines()

for bag in data:
    color, contents = bag.split("s contain")
    contents = [x.strip(' s') for x in contents.strip('.').split(', ')]
    contents = [(int(x[:x.find(' ')].replace('no','0')), x[x.find(' '):].strip()) for x in contents]
    color_dict[color] = contents

count = 0
for color in color_dict:
    if containscolor(color, targetbag):
        count += 1
    

# print(count)
print(containscount(targetbag))
