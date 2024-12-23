'''
--- Part Two ---
The programs seem perplexed by your list of cheats. Apparently, the two-
picosecond cheating rule was deprecated several milliseconds ago! The 
latest version of the cheating rule permits a single cheat that instead 
lasts at most 20 picoseconds.

Now, in addition to all the cheats that were possible in just two 
picoseconds, many more cheats are possible. This six-picosecond cheat saves 
76 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#1#####.#.#.###
#2#####.#.#...#
#3#####.#.###.#
#456.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

Because this cheat has the same start and end positions as the one above, 
it's the same cheat, even though the path taken during the cheat is 
different:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S12..#.#.#...#
###3###.#.#.###
###4###.#.#...#
###5###.#.###.#
###6.E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

Cheats don't need to use all 20 picoseconds; cheats can last any amount of 
time up to and including 20 picoseconds (but can still only end when the 
program is on normal track). Any cheat time not used is lost; it can't be 
saved for another cheat later.

You'll still need a list of the best cheats, but now there are even more to 
choose between. Here are the quantities of cheats in this example that save 
50 picoseconds or more:

  - There are 32 cheats that save 50 picoseconds.
  - There are 31 cheats that save 52 picoseconds.
  - There are 29 cheats that save 54 picoseconds.
  - There are 39 cheats that save 56 picoseconds.
  - There are 25 cheats that save 58 picoseconds.
  - There are 23 cheats that save 60 picoseconds.
  - There are 20 cheats that save 62 picoseconds.
  - There are 19 cheats that save 64 picoseconds.
  - There are 12 cheats that save 66 picoseconds.
  - There are 14 cheats that save 68 picoseconds.
  - There are 12 cheats that save 70 picoseconds.
  - There are 22 cheats that save 72 picoseconds.
  - There are 4 cheats that save 74 picoseconds.
  - There are 3 cheats that save 76 picoseconds.

Find the best cheats using the updated cheating rules. How many cheats 
would save you at least 100 picoseconds?
'''

# READ INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

# NORMALIZE INPUT
maze  = [list(row) for row in lines]

def find(grid, tile):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == tile:
                return (row,col)

start = find(maze, 'S')
end   = find(maze, 'E')

# DELETE THE S AND E FROM THE MAZE
maze[start[0]][start[1]] = '.'
maze[  end[0]][  end[1]] = '.'

# CONSTANTS
WALL  = 999999999
MOVES = [(-1, 0),( 0, 1),( 1, 0),( 0,-1)]


def add(A:tuple, B:tuple) -> tuple:
    return (A[0] + B[0], A[1] + B[1])

def sub(A:tuple, B:tuple) -> tuple:
    return (A[0] - B[0], A[1] - B[1])

def distance(A:tuple, B:tuple) -> int:
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


def measure(maze, start):
    score = [[WALL] * len(maze[0]) for _ in range(len(maze))]
    queue = [(start, 0)]

    while len(queue) > 0:
        pos,cost = queue.pop(0)
        # UPDATES COST
        if score[pos[0]][pos[1]] > cost:
            score[pos[0]][pos[1]] = cost
        # QUEUES NEXT MOVES
        for m in MOVES:
            move = add(pos, m)
            if maze[move[0]][move[1]] == '.': # ROAD TILE
                if score[move[0]][move[1]] > cost+1:
                    queue.append( (move, cost+1) )
    return score

def in_bounds(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])

def cut(start, end, score):
    return score[end[0]][end[1]] - score[start[0]][start[1]] - distance(start, end)

def all_cuts(start, size, score):
    cuts = 0
    for row in range(start[0] - size, start[0] + size+1):
        for col in range(start[1] - size, start[1] + size+1):
            if not in_bounds(score, row, col):
                continue
            if score[row][col] == WALL:
                continue
            end = (row,col)
            if distance(start, end) > size:
                continue
            if cut(start, end, score) >= 100:
                cuts += 1
    return cuts

# SOLUTION
total = 0
score = measure(maze, start)

for row in range(len(score)):
    for col in range(len(score[row])):
        if score[row][col] != WALL:
            total += all_cuts((row,col), 20, score)

print(total) # 961364
