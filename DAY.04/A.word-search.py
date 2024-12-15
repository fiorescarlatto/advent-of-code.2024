'''
--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a 
device and pushes the only button on it. After a brief flash, you recognize 
the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station 
tugs on your shirt; she'd like to know if you could help her with her word 
search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written 
backwards, or even overlapping other words. It's a little unusual, though, 
as you don't merely need to find one instance of XMAS - you need to find 
all of them. Here are a few ways XMAS might appear, where irrelevant 
characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word 
search again, but where letters not involved in any XMAS have been replaced 
with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS 
appear?
'''

# READ THE INPUT LINE BY LINE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# NORMALIZE THE INPUT
words = [list(x.strip()) for x in lines]

# SEARCH STRING
search = 'XMAS'


def find(string:str, direction:tuple[int], start:tuple[int], grid:list[list]) -> bool:
    for i in range(len(string)):
        row = start[0] + i*direction[0]
        col = start[1] + i*direction[1]
        if grid[row][col] != string[i]:
            return False
    return True

def find_all(string:str, start:tuple[int], grid:list[list]) -> int:
    d = [( 1, 0), (-1, 0), ( 0, 1), ( 0,-1), ( 1, 1), ( 1,-1), (-1, 1), (-1,-1)]
    count = 0
    for direction in d:
        count += find(string, direction, start, grid)
    return count

def pad(grid:list[list], filler = '.') -> None:
    grid.append(   [filler] * len(grid[0]))
    grid.insert(0, [filler] * len(grid[0]))
    for i in range(len(grid)):
        grid[i] = [filler] + grid[i] + [filler]


# SOLUTION
total = 0
# ADD PADDING AROUND TO AVOID SEARCHING OUT OF BOUNDS
pad(words, '')

# LOOK FOR MATCHES AT EACH POSITION
for row in range(1, len(words) - 1):
    for col in range(1, len( words[row] ) - 1):
        total += find_all(search, (row,col), words)

print(total) # 2543
