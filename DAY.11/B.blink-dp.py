'''
--- Part Two ---
The Historians sure are taking a long time. To be fair, the infinite 
corridors are very large.

How many stones would you have after blinking a total of 75 times?
'''

# READS THE INPUT LINE FROM THE FILE
file = open('input.txt', 'r', encoding='utf-8')
line = file.read().strip()
file.close()

# NORMALIZES THE INPUT
stones = [int(s) for s in line.split(' ')]
assert len(stones) == 8


# USING CACHING (OR DP)
from functools import cache
@cache
def count_stones(stone, count):
    if count == 0:
        return 1
    else:
        length = len( str(stone) )
        if stone == 0:
            return count_stones(1, count-1)
        if length % 2 == 0:
            half = 10 ** ( length // 2 )
            r = count_stones(stone // half, count-1) 
            r+= count_stones(stone  % half, count-1)
            return r
        else:
            return count_stones(stone * 2024, count-1)


# SOLUTION
total = 0

for s in stones:
    total += count_stones(s, 75)

print(total) # 237149922829154
