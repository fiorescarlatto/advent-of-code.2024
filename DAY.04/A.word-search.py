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
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
assert len(lines) == 140

# NORMALIZE THE INPUT TO A list[list[str]]
lines = [list(x.strip()) for x in lines]
assert len(lines) == 140
assert len(lines[0]) == 140


def find(search_str:str, direction:tuple[int], start:tuple[int], matrix:list[list]):
    for i in range(len(search_str)):
        row = start[0] + i*direction[0]
        col = start[1] + i*direction[1]
        if matrix[row][col] != search_str[i]:
            return 0
    return 1

def find_all_at(search_str:str, start:tuple[int], matrix:list[list]):
    count = 0
    count += find(search_str, ( 1, 0), start, matrix)
    count += find(search_str, (-1, 0), start, matrix)
    count += find(search_str, ( 0, 1), start, matrix)
    count += find(search_str, ( 0,-1), start, matrix)
    count += find(search_str, ( 1, 1), start, matrix)
    count += find(search_str, ( 1,-1), start, matrix)
    count += find(search_str, (-1, 1), start, matrix)
    count += find(search_str, (-1,-1), start, matrix)
    return count

def padding(pad, amount:int, matrix:list[list]):
    for _ in range(amount):
        matrix.insert(0, [pad] * len(matrix[0]))
        matrix.append(   [pad] * len(matrix[0]))
    for i in range(len(matrix)):
        matrix[i] = [pad]*amount + matrix[i] + [pad]*amount


# SOLUTION
search = 'XMAS'
count = 0

# ADD PADDING AROUND TO ALLOW SEARCH OUT OF BOUNDS
padding('', len(search), lines)

# LOOK FOR MATCHES AT EACH POSITION
for row in range(len(search), len(lines) - len(search)):
    for col in range(len(search), len(lines[row]) - len(search)):
        count += find_all_at(search, (row,col), lines)

print(count) # 2543
