# advent of code day 5

"""
BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
"""

data = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL"]
    
def seatinfo(bpass):
    row = int(bpass[0:7].replace('F','0').replace('B','1'), 2)
    col = int(bpass[7:].replace('R','1').replace('L','0'), 2)
    id = row*8 + col
    return row, col, id

print(seatinfo(data[0]))