
# READ INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

# NORMALIZES THE INPUT
warehouse = [list(x) for x in lines[:50]]
moves = ''.join( lines[50:] )

# GET THE ROBOT'S POSITION
robot = [0, 0]

for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
        if warehouse[row][col] == '@':
            robot = [row, col]

# POSSIBLE DIRECTIONS
directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}


def move(robot, direction, warehouse):
    d = directions[direction]
    p = (robot[0], robot[1])
    while True:
        p = (p[0] + d[0], p[1] + d[1])
        if warehouse[p[0]][p[1]] == '#':
            return False
        elif warehouse[p[0]][p[1]] == '.':
            break
    warehouse[p[0]][p[1]] = 'O'
    warehouse[robot[0]][robot[1]] = '.'
    robot[0] = robot[0] + d[0]
    robot[1] = robot[1] + d[1]
    warehouse[robot[0]][robot[1]] = '@'
    return True


# SOLUTION
total = 0

for m in moves:
    move(robot, m, warehouse)

for row in range(len(warehouse)):
    for col in range(len(warehouse[col])):
        if warehouse[row][col] == 'O':
            total += 100*row + col

print(total) # 1415498
