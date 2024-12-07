'''
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all 
away to the North Pole prototype suit manufacturing lab... in the year 
1518! It turns out that having direct access to history is very convenient 
for a group of historians.

You still have to be careful of time paradoxes, and so it will be important 
to avoid anyone from 1518 while The Historians search for the Chief. 
Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The 
Historians can search safely?

You start by making a map (your puzzle input) of the situation. For 
example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the 
guard is currently facing up from the perspective of the map). Any 
obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves 
repeatedly following these steps:

  - If there is something directly in front of you, turn right 90 degrees.
  - Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she 
reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Because there is now an obstacle in front of the guard, she turns right 
before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Reaching another obstacle (a spool of several very long polymers), she 
turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...

This process continues for a while, but the guard eventually leaves the 
mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..

By predicting the guard's route, you can determine which specific positions 
in the lab will be in the patrol path. Including the guard's starting 
position, the positions visited by the guard before leaving the area are 
marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..

In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard 
visit before leaving the mapped area?
'''

# READ THE INPUT FILE
file = open('input.txt', 'r', encoding='utf-8')
room = file.readlines()
file.close()
assert len(room) == 130

# NORMALIZE THE INPUT TO A 2D MATRIX
room = [list(r.strip()) for r in room]

direction = {
    '^': (-1,  0), 
    '>': ( 0,  1),
    'v': ( 1,  0),
    '<': ( 0, -1)
}

turn = {
    '^': '>', 
    '>': 'v',
    'v': '<',
    '<': '^'
}

# GETS THE POSITION AND ORIENTATION OF THE GUARD
guard = { 'pos': (0, 0), 'dir': '^' }

for row in range( len(room) ):
    for col in range( len(room[row]) ):
        if room[row][col] in direction.keys():
            guard['pos'] = (row, col)
            guard['dir'] = room[row][col]


def next_step(guard):
    pos = guard['pos']
    dir = direction[ guard['dir'] ]
    return (pos[0] + dir[0], pos[1] + dir[1])

def next_rotation(guard):
    return turn[ guard['dir'] ]

def pos_in_bounds(pos, room):
    return pos[0] in range(len(room)) and pos[1] in range(len(room[ pos[0] ]))

def pos_is_empty(pos, room):
    return room[ pos[0] ][ pos[1] ] != '#' 

def pos_is_new(pos, room):
    return room[ pos[0] ][ pos[1] ] == '.'

def mark_position(pos, room):
    room[ pos[0] ][ pos[1] ] = 'x'

# SOLUTION
visited = 1

while(True):
    # MARK THE CURRENT POSITION AS VISITED
    mark_position(guard['pos'], room)
    pos = next_step(guard)

    if not pos_in_bounds(pos, room):
        # GUARD LEFT THE ROOM
        break

    if pos_is_empty(pos, room):
        # MOVE GUARD TO NEW POSITION
        guard['pos'] = pos

        # ADD TO VISITED IF IT'S A NEW POSITION
        if pos_is_new(pos, room):
            visited += 1
    else:
        # TURN TO THE RIGHT
        guard['dir'] = next_rotation(guard)

print(visited) # 4819
