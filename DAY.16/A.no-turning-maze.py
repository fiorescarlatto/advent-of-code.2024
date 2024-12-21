'''
--- Day 16: Reindeer Maze ---
It's time again for the Reindeer Olympics! This year, the big event is the 
Reindeer Maze, where the Reindeer compete for the lowest score.

You and The Historians arrive to search for the Chief right as the event is 
about to start. It wouldn't hurt to watch a little, right?

The Reindeer start on the Start Tile (marked S) facing East and need to 
reach the End Tile (marked E). They can move forward one tile at a time 
(increasing their score by 1 point), but never into a wall (#). They can 
also rotate clockwise or counterclockwise 90 degrees at a time (increasing 
their score by 1000 points).

To figure out the best place to sit, you start by grabbing a map (your 
puzzle input) from a nearby kiosk. For example:

###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############

There are many paths through this maze, but taking any of the best paths 
would incur a score of only 7036. This can be achieved by taking a total of 
36 steps forward and turning 90 degrees a total of 7 times:


###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############

Here's a second example:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################

In this maze, the best paths cost 11048 points; following one such path 
would look like this:

#################
#...#...#...#..E#
#.#.#.#.#.#.#.#^#
#.#.#.#...#...#^#
#.#.#.#.###.#.#^#
#>>v#.#.#.....#^#
#^#v#.#.#.#####^#
#^#v..#.#.#>>>>^#
#^#v#####.#^###.#
#^#v#..>>>>^#...#
#^#v###^#####.###
#^#v#>>^#.....#.#
#^#v#^#####.###.#
#^#v#^........#.#
#^#v#^#########.#
#S#>>^..........#
#################

Note that the path shown above includes one 90 degree turn as the very 
first move, rotating the Reindeer from facing East to facing North.

Analyze your map carefully. What is the lowest score a Reindeer could 
possibly get?
'''

# READ INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

# NORMALIZE INPUT
maze  = [list(row) for row in lines]

def find(maze, tile):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == tile:
                return (row,col)
    return (0,0)

start = find(maze, 'S')
goal  = find(maze, 'E')

# DELETE THE S AND E FROM THE MAZE
maze[start[0]][start[1]] = '.'
maze[ goal[0]][ goal[1]] = '.'


def add(A:tuple, B:tuple) -> tuple:
    return (A[0] + B[0], A[1] + B[1])

def traverse(maze, start, end):
    visited = set()
    turn  = [(-1, 0),( 0, 1),( 1, 0),( 0,-1)]
    deer = [(0, start, 1)]

    while len(deer) > 0:
        deer.sort(key = lambda x: -x[0])
        score,pos,facing = deer.pop()

        visited.add(pos)
        if pos == end:
            return score

        for rotation,cost in [(0,1), (1,1001), (3,1001)]:
            rotation = (facing + rotation) % 4
            row,col  = add(pos, turn[rotation])

            if (row,col) not in visited and maze[row][col] == '.':
                deer.append( (score+cost, (row,col), rotation) )


# SOLUTION
total = traverse(maze, start, goal)

print(total) # 74392
