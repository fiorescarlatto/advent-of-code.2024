'''
--- Part Two ---
The Historians aren't as used to moving around in this pixelated universe 
as you are. You're afraid they're not going to be fast enough to make it to 
the exit before the path is completely blocked.

To determine how fast everyone needs to go, you need to determine the first 
byte that will cut off the path to the exit.

In the above example, after the byte at 1,1 falls, there is still a path to 
the exit:

O..#OOO
O##OO#O
O#OO#OO
OOO#OO#
###OO##
.##O###
#.#OOOO

However, after adding the very next byte (at 6,1), there is no longer a 
path to the exit:

...#...
.##..##
.#..#..
...#..#
###..##
.##.###
#.#....

So, in this example, the coordinates of the first byte that prevents the 
exit from being reachable are 6,1.

Simulate more of the bytes that are about to corrupt your memory space. 
What are the coordinates of the first byte that will prevent the exit from 
being reachable from your starting position? (Provide the answer as two 
integers separated by a comma with no other characters.)
'''

# READ INPUT LINE BY LINE
with open('input.txt') as file:
    lines = file.readlines()

# NORMALIZE INPUT
blocks = []

for line in lines:
    col,row = [int(x) for x in line.strip().split(',')]
    blocks.append( (row,col) )

# OTHER INFORMATION
size = 71
room = [[1] * size for _ in range(size)]

for i in range(1024):
    row,col = blocks[i]
    room[row][col] = 0


def in_bounds(grid, row, col):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row])

def traverse(maze, start, end):
    visited = set()
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    queue = [(start,0)]
    
    while len(queue) > 0:
        pos,cost = queue.pop(0)
        if pos == end:
            return cost
        for m in moves:
            row = pos[0] + m[0]
            col = pos[1] + m[1]
            if (row,col) in visited:
                continue
            if in_bounds(maze, row, col) and maze[row][col]:
                visited.add(   (row,col) )
                queue.append( ((row,col), cost+1) )
    return 0


# SOLUTION
for i in range(1024, len(blocks)):
    row,col = blocks[i]
    room[row][col] = 0
    if not traverse(room, (0,0), (70,70)):
        break

print(f'{col},{row}') # 20,12
