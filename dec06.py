# advent of code day 6

data = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b"
]

group = []
groups = []
for person in data:
    if person:
        group.append(person)
    else:
        groups.append(group)
        group = []
groups.append(group)

total = 0
for group in groups:
    groupset = set()
    for person in group:
        for q in person:
            groupset.add(q)
    total += len(groupset)
    
print(total)