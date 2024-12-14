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
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

# NORMALIZE THE INPUT
robots = []

for l in lines:
    l = l.strip().split(' ')
    position = l[0][2:].split(',')
    velocity = l[1][2:].split(',')
    position = [int(p) for p in position]
    velocity = [int(v) for v in velocity]
    robots.append([position,velocity])

# OTHER INFORMATION
size = [101, 103]


def treeness(room):
    treeness = 0
    # JUST COUNTS THE NEIGHBOURS
    for row in range(1, len(room) - 1):
        for col in range(1, len( room[row] ) - 1):
            if room[row][col] > 0:
                treeness += 1 if room[row-1][col-1] > 0 else 0
                treeness += 1 if room[row-1][col-0] > 0 else 0
                treeness += 1 if room[row-1][col+1] > 0 else 0
                treeness += 1 if room[row-0][col-1] > 0 else 0
                treeness += 1 if room[row-0][col+1] > 0 else 0
                treeness += 1 if room[row+1][col-1] > 0 else 0
                treeness += 1 if room[row+1][col-0] > 0 else 0
                treeness += 1 if room[row+1][col+1] > 0 else 0
    return treeness

def room_state(size, seconds, robots):
    room = []
    # CREATE EMPTY ROOM
    for _ in range(size[1]):
        room.append( [0]*size[0] )
    # ADD ROBOTS TO THE ROOM
    for r in robots:
        position, velocity = r
        goal = [
            (position[0] + seconds * velocity[0]) % size[0], 
            (position[1] + seconds * velocity[1]) % size[1]
        ]     
        room[ goal[1] ][ goal[0] ] += 1
    return room

def draw(room):
    for row in room:
        row = ['.' if r == 0 else str(r) for r in row]
        print(''.join(row))


# SOLUTION
tree = []

for seconds in range(10000):
    room = room_state(size, seconds, robots)
    tree.append( (treeness(room), seconds) )

_, seconds = max(tree)

draw( room_state(size, seconds, robots) )
print(seconds) # 6620
