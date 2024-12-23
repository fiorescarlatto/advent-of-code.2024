'''
--- Day 20: Race Condition ---
The Historians are quite pixelated again. This time, a massive, black 
building looms over you - you're right outside the CPU!

While The Historians get to work, a nearby program sees that you're idle 
and challenges you to a race. Apparently, you've arrived just in time for 
the frequently-held race condition festival!

The race takes place on a particularly long and twisting code path; 
programs compete to see who can finish in the fewest picoseconds. The 
winner even gets their very own mutex!

They hand you a map of the racetrack (your puzzle input). For example:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

The map consists of track (.) - including the start (S) and end (E) 
positions (both of which also count as track) - and walls (#).

When a program runs through the racetrack, it starts at the start position. 
Then, it is allowed to move up, down, left, or right; each such move takes 
1 picosecond. The goal is to reach the end position as quickly as possible. 
In this example racetrack, the fastest time is 84 picoseconds.

Because there is only a single path from the start to the end and the 
programs all go the same speed, the races used to be pretty boring. To make 
things more interesting, they introduced a new rule to the races: programs 
are allowed to cheat.

The rules for cheating are very strict. Exactly once during a race, a 
program may disable collision for up to 2 picoseconds. This allows the 
program to pass through walls as if they were regular track. At the end of 
the cheat, the program must be back on normal track again; otherwise, it 
will receive a segmentation fault and get disqualified.

So, a program could complete the course in 72 picoseconds (saving 12 
picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...12....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

Or, a program could complete the course in 64 picoseconds (saving 20 
picoseconds) by cheating for the two moves marked 1 and 2:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...12..#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

This cheat saves 38 picoseconds:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.####1##.###
#...###.2.#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

This cheat saves 64 picoseconds and takes the program directly to the end:

###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..21...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############

Each cheat has a distinct start position (the position where the cheat is 
activated, just before the first move that is allowed to go through walls) 
and end position; cheats are uniquely identified by their start position 
and end position.

In this example, the total number of cheats (grouped by the amount of time 
they save) are as follows:

  - There are 14 cheats that save 2 picoseconds.
  - There are 14 cheats that save 4 picoseconds.
  - There are 2 cheats that save 6 picoseconds.
  - There are 4 cheats that save 8 picoseconds.
  - There are 2 cheats that save 10 picoseconds.
  - There are 3 cheats that save 12 picoseconds.
  - There is one cheat that saves 20 picoseconds.
  - There is one cheat that saves 36 picoseconds.
  - There is one cheat that saves 38 picoseconds.
  - There is one cheat that saves 40 picoseconds.
  - There is one cheat that saves 64 picoseconds.

You aren't sure what the conditions of the racetrack will be like, so to 
give yourself as many options as possible, you'll need a list of the best 
cheats. How many cheats would save you at least 100 picoseconds?
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

def all_cuts(start, score):
    cuts = set()

    for m in MOVES:
        row = start[0] + m[0]
        col = start[1] + m[1]
        if not in_bounds(score, row, col):
            continue
        if score[row][col] != WALL:
            continue

        for k in MOVES:
            row = start[0] + m[0] + k[0]
            col = start[1] + m[1] + k[1]
            if not in_bounds(score, row, col):
                continue
            if score[row][col] == WALL:
                continue
            if cut(start, (row,col), score) >= 100:
                cuts.add( (row,col) )

    return len(cuts)

# SOLUTION
total = 0
score = measure(maze,start)

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == '.':
            total += all_cuts((row,col), score)

print(total) # 1311
