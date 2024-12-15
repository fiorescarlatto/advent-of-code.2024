'''
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that 
this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're 
supposed to find two MAS in the shape of an X. One way to achieve that is 
like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. 
Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have 
been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search 
side and try again. How many times does an X-MAS appear?
'''

# READ THE INPUT LINE BY LINE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# NORMALIZE THE INPUT
words = [list(x.strip()) for x in lines]

# DEFINE MY SEARCH PATTERNS
patterns = [
    [['M','' ,'M'],
     ['' ,'A','' ],
     ['S','' ,'S']
    ],
    [['M','' ,'S'],
     ['' ,'A','' ],
     ['M','' ,'S']
    ],
    [['S','' ,'S'],
     ['' ,'A','' ],
     ['M','' ,'M']
    ],
    [['S','' ,'M'],
     ['' ,'A','' ],
     ['S','' ,'M']
    ]   
]


def window(grid:list[list], pos:tuple[int], size:tuple[int]) -> list[list]:
    window = []
    for row in range( size[0] ):
        window.append( grid[ pos[0]+row ][ pos[1] : pos[1]+size[1] ] )
    return window

def sliding_windows(grid:list[list], size:tuple[int]):
    for row in range( len(grid) - ( size[0]-1 ) ):
        for col in range( len( grid[row] ) - ( size[1]-1 ) ):
            yield window(grid, (row,col), size)

def pattern_match(pattern:list[list], grid:list[list]) -> bool:
    for row in range( len(pattern) ):
        for col in range( len( pattern[row] ) ):
            if pattern[row][col] != '' and pattern[row][col] != grid[row][col]:
                return False
    return True


# SOLUTION
count = 0

# FOR EACH 3x3 WINDOW COUNTS THE MATCHING PATTERNS
for w in sliding_windows(words, (3,3)):
    for p in patterns:
        if pattern_match(p, w):
            count += 1

print(count) # 1930
