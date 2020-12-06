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

## Part 2 validation:

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

import re
prog = re.compile("(\S+):(\S+)")
hgtval = re.compile("(\d+)(cm|in)")
hclval = re.compile("#[0-9,a-f]{6}")
pidval = re.compile("[0-9]{9}")

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

# four invalid passports for part 2
data = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007"
]

# four valid passports for part 2
data = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
]


def validheight(s):
    f = hgtval.search(s)
    if f:
        unit = f.groups()[1]
        value = int(f.groups()[0])
        return (unit == "cm" and (150 <= value <= 193)) or (59 <= value <= 76)
    else:
        return False

def finishrecord(d):
    if all([x in d for x in tempfields]):
        # Further validation
        for k,v in d.items():
            if (
                (k == "byr" and not (1920 <= int(v) <= 2002)) or
                (k == "iyr" and not (2010 <= int(v) <= 2020)) or
                (k == "eyr" and not (2020 <= int(v) <= 2030)) or
                (k == "hgt" and not validheight(v)) or
                (k == "hcl" and not hclval.search(v)) or
                (k == "ecl" and not v in ["amb","blu","brn","gry","grn","hzl","oth"]) or
                (k == "pid" and not pidval.search(v))
                ):  
                return 0
        print(d)
        return 1
    else:
        return 0

    

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
        count += finishrecord(passdict)
        passdict = {}
count += finishrecord(passdict)

print(count)

