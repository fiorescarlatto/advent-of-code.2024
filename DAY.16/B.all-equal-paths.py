'''
--- Part Two ---
Now that you know what the best paths look like, you can figure out the 
best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the 
edges of the tile. While determining which of these tiles would be the best 
spot to sit depends on a whole bunch of factors (how comfortable the seats 
are, how far away the bathrooms are, whether there's a pillar blocking your 
view, etc.), the most important factor is whether the tile is on one of the 
best paths through the maze. If you sit somewhere else, you'd miss all the 
action!

So, you'll need to determine which tiles are part of any best path through 
the maze, including the S and E tiles.

In the first example, there are 45 tiles (marked O) that are part of at 
least one of the various best paths through the maze:

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############

In the second example, there are 64 tiles that are part of at least one of 
the best paths:

#################
#...#...#...#..O#
#.#.#.#.#.#.#.#O#
#.#.#.#...#...#O#
#.#.#.#.###.#.#O#
#OOO#.#.#.....#O#
#O#O#.#.#.#####O#
#O#O..#.#.#OOOOO#
#O#O#####.#O###O#
#O#O#..OOOOO#OOO#
#O#O###O#####O###
#O#O#OOO#..OOO#.#
#O#O#O#####O###.#
#O#O#OOOOOOO..#.#
#O#O#O#########.#
#O#OOO..........#
#################

Analyze your map further. How many tiles are part of at least one of the 
best paths through the maze?
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


def sub(A:tuple, B:tuple) -> tuple:
    return (A[0] - B[0], A[1] - B[1])

def add(A:tuple, B:tuple) -> tuple:
    return (A[0] + B[0], A[1] + B[1])

def traverse(maze, start, end):
    visited = []
    for row in range(len(maze)):
        visited.append([999999999] * len(maze[row]))

    turn = [(-1, 0),( 0, 1),( 1, 0),( 0,-1)]
    deer = [(0, start, 1)]

    while len(deer) > 0:
        deer.sort(key = lambda x: -x[0])
        score,pos,facing = deer.pop()
        
        if visited[pos[0]][pos[1]] > score:
            visited[pos[0]][pos[1]] = score

        row,col = add(pos, turn[facing])
        if maze[row][col] == '.':
            if visited[row][col] > score+1:
                deer.append( (score+1, (row,col), facing) )
        else:
            if pos != end:
                visited[pos[0]][pos[1]] += 1000
        
        for rotation,cost in [(1,1001), (3,1001)]:
            rotation = (facing + rotation) % 4

            row,col  = add(pos, turn[rotation])
            if maze[row][col] == '.':
                if visited[row][col] > score+cost:
                    deer.append( (score+cost, (row,col), rotation) )
    return visited


def mark_paths(maze, cost, start):
    moves  = [(-1, 0),( 0, 1),( 1, 0),( 0,-1)]
    search = [(start, (0,0))]

    while len(search) > 0:
        pos,p_move = search.pop(0)
        maze[pos[0]][pos[1]] = 'O'

        for move in moves:
            row,col = add(pos, move)
            if cost[row][col] < cost[pos[0]][pos[1]]:
                search.append( ((row,col), move) )
                if move != p_move:
                    p = sub(pos, p_move)
                    n = add(pos, p_move)
                    if cost[p[0]][p[1]] == cost[n[0]][n[1]] + 2:
                        search.append((n, p_move))


# SOLUTION
cost = traverse(maze, start, goal)
mark_paths(maze, cost, goal)
maze[start[0]][start[1]] = 'O'

total = 0

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == 'O':
            total += 1

# with open('log.csv', 'w') as file:
#     for row in maze:
#         for tile in row:
#             file.write(tile+',')
#         file.write('\n')

print(total) # 426
