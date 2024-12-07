'''
--- Part Two ---
While The Historians begin working around the guard's patrol route, you 
borrow their fancy device and step outside the lab. From the safety of a 
supply closet, you time travel through the last few months and record the 
nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they 
explain that the guard's patrol area is simply too large for them to safely 
search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction 
won't cause a time paradox. They'd like to place the new obstruction in 
such a way that the guard will get stuck in a loop, making the rest of the 
lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would 
like to know all of the possible positions for such an obstruction. The new 
obstruction can't be placed at the guard's starting position - the guard is 
there right now and would notice.

In the above example, there are only 6 different positions where a new 
obstruction would cause the guard to get stuck in a loop. The diagrams of 
these six situations use O to mark the new obstruction, | to show a 
position where the guard moves up/down, - to show a position where the 
guard moves left/right, and + to show a position where the guard moves both 
up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...

Option two, put a stack of failed suit prototypes in the bottom right 
quadrant of the mapped area:


....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the 
standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...

Option four, put an alchemical retroencabulator near the bottom left 
corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...

Option five, put the alchemical retroencabulator a bit to the right 
instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...

Option six, put a tank of sovereign glue right next to the tank of 
universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..

It doesn't really matter what you choose to use as an obstacle so long as 
you and The Historians can put it into position without the guard noticing. 
The important thing is having enough options that you can find one that 
minimizes time paradoxes, and in this example, there are 6 different 
positions you could choose.

You need to get the guard stuck in a loop by adding a single new 
obstruction. How many different positions could you choose for this 
obstruction?
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

def guard_state(guard):
    return guard['dir'] + str(guard['pos'])

def is_loop(guard, room):
    state = set()

    while(True):
        if guard_state(guard) in state:
            # SEEN STATE, WE ARE LOOPING
            return True
        else:
            # MARK THE CURRENT STATE AS SEEN
            state.add(guard_state(guard))
        
        pos = next_step(guard)
        if not pos_in_bounds(pos, room):
            # GUARD LEFT THE ROOM
            return False
        if pos_is_empty(pos, room):
            # MOVE GUARD TO NEW POSITION
            guard['pos'] = pos
        else:
            # TURN TO THE RIGHT
            guard['dir'] = next_rotation(guard)


# SOLUTION
loops = 0

for row in range(len(room)):
    for col in range(len(room[row])):
        # IF THE SQUARE IS EMPTY
        if room[row][col] == '.':
            # ADD TEST OBJECT
            room[row][col] = '#'
            # CLONE GUARD
            g = dict(guard.items())
            # COUNT IF IT'S A LOOP
            if is_loop(g, room):
                loops += 1
                print((row,col))
            # REMOVE TEST OBJECT
            room[row][col] = '.'

print(loops) # 1796
