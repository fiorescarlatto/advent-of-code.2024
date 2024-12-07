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
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
assert len(lines) == 140

# NORMALIZE THE INPUT TO A LIST OF LISTS OF STRINGS
lines = [list(x.strip()) for x in lines]
assert len(lines) == 140
assert len(lines[0]) == 140


def window_at(pos:tuple[int], size:tuple[int], matrix:list[list]):
    window = []
    for row in range(size[0]):
        r = []
        for col in range(size[1]):
            r.append(matrix[ pos[0]+row ][ pos[1]+col ])
        window.append(r)
    return window

def sliding_window(size:tuple[int], matrix:list[list]):
    sw = []
    for row in range(len(matrix) - (size[0]-1)):
        for col in range(len(matrix[row]) - (size[1]-1)):
            sw.append(window_at((row, col), size, matrix))
    return sw

def pattern_match(pattern:list[list], matrix:list[list]):
    for row in range(len(pattern)):
        for col in range(len(pattern[row])):
            if pattern[row][col] != '' and pattern[row][col] != matrix[row][col]:
                return False
    return True


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

# SOLUTION
count = 0

# FOR EACH 3x3 WINDOW COUNTS THE MATCHIN PATTERNS
for w in sliding_window((3,3), lines):
    for p in patterns:
        if pattern_match(p, w):
            count += 1

print(count) # 1930
