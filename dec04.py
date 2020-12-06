# advent of code day 4
#
# Required fields:

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
import re
prog = re.compile("(\S+):(\S+)")

fields = ["byr","iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

tempfields = fields[::]
tempfields.remove("cid")

data = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]

with open("dec04.txt") as f:
    data = f.readlines()

passdict = {}
count = 0
for record in data:
    if record:
        fields = record.split()
        for field in fields:
            subfield = prog.search(field)
            passdict[subfield.groups()[0]] = subfield.groups()[1]
    else:
        print(passdict.keys())
        if all([x in passdict for x in tempfields]):
            count += 1
        passdict = {}

print(count)

