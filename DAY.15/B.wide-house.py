'''
--- Part Two ---
The lanternfish use your information to find a safe moment to swim in and 
turn off the malfunctioning robot! Just as they start preparing a festival 
in your honor, reports start coming in that a second warehouse's robot is 
also malfunctioning.

This warehouse's layout is surprisingly similar to the one you just helped. 
There is one key difference: everything except the robot is twice as wide! 
The robot's list of movements doesn't change.

To get the wider warehouse's map, start with your original map and, for 
each tile, make the following changes:

If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.

This will produce a new warehouse map which is twice as wide and with wide 
boxes that are represented by []. (The robot does not change size.)

The larger example from before would now look like this:

####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

Because boxes are now twice as wide but the robot is still the same size 
and speed, boxes can be aligned such that they directly push two other 
boxes at once. For example, consider this situation:

#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^

After appropriately resizing this map, the robot would push around these 
boxes as follows:

Initial state:
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############

Move <:
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############

Move v:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############

Move <:
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############

Move <:
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############

Move ^:
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############

Move ^:
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############

This warehouse also uses GPS to locate the boxes. For these larger boxes, 
distances are measured from the edge of the map to the closest edge of the 
box in question. So, the box shown below has a distance of 1 from the top 
edge of the map and 5 from the left edge of the map, resulting in a GPS 
coordinate of 100 * 1 + 5 = 105.

##########
##...[]...
##........

In the scaled-up version of the larger example from above, after the robot 
has finished all of its moves, the warehouse would look like this:

####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################

The sum of these boxes' GPS coordinates is 9021.

Predict the motion of the robot and boxes in this new, scaled-up warehouse. 
What is the sum of all boxes' final GPS coordinates?
'''

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