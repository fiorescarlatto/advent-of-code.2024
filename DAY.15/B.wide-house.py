
# READ INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split('\n')

# OTHER INFO
size = 50

# EXPAND THE WAREHOUSE
for row in range(size):
    wide = list(lines[row])
    for col in range(len(wide)):
        if wide[col] == '#':
           wide[col]  = '##'
        if wide[col] == '.':
           wide[col]  = '..'
        if wide[col] == 'O':
           wide[col]  = '[]'
        if wide[col] == '@':
           wide[col]  = '@.'
    lines[row] = ''.join(wide)

# NORMALIZES THE INPUT
warehouse = [list(x) for x in lines[:size]]
moves = ''.join( lines[size:] )

# GET THE ROBOT'S POSITION
robot = [0, 0]

for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
        if warehouse[row][col] == '@':
            robot = [row, col]


def mask_clear(mask, warehouse):
    for row in range(len(mask)):
        for col in range(len(mask[row])):
            if mask[row][col] > 0:
                warehouse[row][col] = '.'

def mask_apply(mask, warehouse):
    for row in range(len(mask)):
        for col in range(len(mask[row])):
            if mask[row][col] == 1:
                warehouse[row][col] = '['
            if mask[row][col] == 2:
                warehouse[row][col] = ']'

def move_box(box, d, mask, warehouse) -> bool:
    row,col = box
    mask[row][col]     = 1
    mask[row][col + 1] = 2
    # GET THE UPPER L AND R STATE
    left  = warehouse[row + d][col]
    right = warehouse[row + d][col + 1]
    # CHECK FOR SIMPLE CASES
    if left == '#' or right == '#':
        return False
    if left == '[' and right == ']':
        return move_box((row + d, col), d, mask, warehouse)
    # CHECK FOR LEFT AND RIGHT COMBINATIONS
    if left == '.':
        left = True
    elif left == ']':
        left = move_box((row + d, col - 1), d, mask, warehouse)
    if right == '.':
        right = True
    elif right == '[':
        right = move_box((row + d, col + 1), d, mask, warehouse)
    # COMBINES LEFT AND RIGHT
    return left and right
    

def move_v(robot, d, warehouse):
    row,col = robot
    # EASY CASE
    if warehouse[row + d][col] == '#':
        return False
    if warehouse[row + d][col] == '.':
        warehouse[row][col] = '.'
        warehouse[row + d][col] = '@'
        robot[0] += d
        return True
    # HARD CASE
    if warehouse[row + d][col] == '[':
        box = (row + d, col)
    else:
        box = (row + d, col - 1)
    # CREATE EMPTY MASK
    mask = []
    for i in range(len(warehouse)):
        mask.append([0] * len(warehouse[i]))
    # CHECK IF IT CAN MOVE
    if move_box(box, d, mask, warehouse):
        # APPLY NEW BOX DISPOSITION
        mask_clear(mask, warehouse)
        if d == -1:
            mask.pop(0)
            mask.append([0] * len(warehouse[-1]))
        else:
            mask.pop()
            mask.insert(0, [0] * len(warehouse[0]))
        mask_apply(mask, warehouse)
        # MOVE ROBOT
        warehouse[row][col] = '.'
        warehouse[row + d][col] = '@'
        robot[0] += d
        return True
    return False

def move_h(robot, d, warehouse):
    row,col = robot
    # FIND HOLE
    while True:
        col = col + d 
        if warehouse[row][col] == '#':
            return False
        elif warehouse[row][col] == '.':
            break
    # MOVE LINE OF BOXES
    for i in range(col, robot[1], -d):
        warehouse[row][i] = warehouse[row][i-d]
    warehouse[row][robot[1]] = '.'
    robot[1] += d
    return True

def move(robot, direction, warehouse):
    if direction == '>':
        return move_h(robot, 1, warehouse)
    if direction == '<':
        return move_h(robot,-1, warehouse)
    if direction == 'v':
        return move_v(robot, 1, warehouse)
    if direction == '^':
        return move_v(robot,-1, warehouse)


# SOLUTION
total = 0

for m in moves:
    move(robot, m, warehouse)

for row in range(len(warehouse)):
    for col in range(len(warehouse[row])):
        if warehouse[row][col] == '[':
            total += col + row * 100

print(total)