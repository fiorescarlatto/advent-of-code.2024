'''
--- Part Two ---
The staff don't really like some of the towel arrangements you came up 
with. To avoid an endless cycle of towel rearrangement, maybe you should 
just give them every possible option.

Here are all of the different ways the above example's designs can be made:

brwrr can be made in two different ways: b, r, wr, r or br, wr, r.

bggr can only be made with b, g, g, and r.

gbbr can be made 4 different ways:

  - g, b, b, r
  - g, b, br
  - gb, b, r
  - gb, br

rrbgbr can be made 6 different ways:

  - r, r, b, g, b, r
  - r, r, b, g, br
  - r, r, b, gb, r
  - r, rb, g, b, r
  - r, rb, g, br
  - r, rb, gb, r

bwurrg can only be made with bwu, r, r, and g.

brgr can be made in two different ways: b, r, g, r or br, g, r.

ubwu and bbrgwb are still impossible.

Adding up all of the ways the towels in this example could be arranged into 
the desired designs yields 16 (2 + 1 + 4 + 6 + 1 + 2).

They'll let you into the onsen as soon as you have the list. What do you 
get if you add up the number of different ways you could make each design?
'''

# INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    towels = file.readline()
    # SKIP EMPTY LINE
    file.readline()
    designs = file.readlines()

# NORMALIZE INPUT
towels  = towels.strip().split(', ')
designs = [a.strip() for a in designs]


# UISING CACHE TO AVOID RE-CALCULATING RECURSIONS
from functools import cache

@cache
def count_arrangements(design:str) -> int:
    if design == '':
        return 1
    count = 0
    for t in towels:
        if design.startswith(t):
            count += count_arrangements(design[len(t):])
    return count


# SOLUTION
total = 0

for d in designs:
    total += count_arrangements(d)

print(total) # 692575723305545
