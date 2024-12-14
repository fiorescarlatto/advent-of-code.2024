'''
--- Part Two ---
During the bathroom break, someone notices that these robots seem awfully 
similar to ones built and used at the North Pole. If they're the same type 
of robots, they should have a hard-coded Easter egg: very rarely, most of 
the robots should arrange themselves into a picture of a Christmas tree.

What is the fewest number of seconds that must elapse for the robots to 
display the Easter egg?
'''

# READ FILE INPUT LINE BY LINE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# OTHER INFORMATION
size = [101, 103]

# NORMALIZE THE INPUT
robots = []

for l in lines:
    l = l.strip().split(' ')
    start = l[0][2:].split(',')
    speed = l[1][2:].split(',')

    start = [int(s) for s in start]
    speed = [int(s) for s in speed]
    pos   = [0, 0]

    robots.append( [start,speed,pos] )


def treeness(robots, room):
    treeness = 0
    # COUNT THE NEIGHBOURS
    for r in robots:
        col,row = r[2]
        if row > 1 and row < len(room)-1:
            if col > 1 and col < len(room[row])-1:
                treeness += room[row-1][col-1]
                treeness += room[row-1][col-0]
                treeness += room[row-1][col+1]
                treeness += room[row-0][col-1]
                treeness += room[row-0][col+1]
                treeness += room[row+1][col-1]
                treeness += room[row+1][col-0]
                treeness += room[row+1][col+1]
    return treeness

def move(robots, time):
    room = []
    for _ in range(size[1]):
        room.append( [0]*size[0] )
    for r in robots:
        start, speed, _ = r
        pos = [ (start[0] + time * speed[0]) % size[0],
                (start[1] + time * speed[1]) % size[1] ]
        r[2] = pos
        room[pos[1]][pos[0]] += 1
    return room

def draw(room):
    for row in room:
        row = ['O' if r else ' ' for r in row]
        print(''.join(row))


# SOLUTION
tree = []

for seconds in range( size[0]*size[1] ):
    room = move(robots, seconds)
    tree.append( (treeness(robots, room),seconds) )

_, seconds = max(tree)

draw( move(robots, seconds) )
print(seconds) # 6620
