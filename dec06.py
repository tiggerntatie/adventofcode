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

print(groups)