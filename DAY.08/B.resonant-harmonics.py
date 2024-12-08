'''
--- Part Two ---
Watching over your shoulder as you work, one of The Historians asks if you 
took the effects of resonant harmonics into your calculations.

Whoops!

After updating your model, it turns out that an antinode occurs at any grid 
position exactly in line with at least two antennas of the same frequency, 
regardless of distance. This means that some of the new antinodes will 
occur at the position of each antenna (unless that antenna is the only one 
of its frequency).

So, these three T-frequency antennas now create many antinodes:

T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
..........

In fact, the three T-frequency antennas are all exactly in line with two 
antennas, so they are all also antinodes! This brings the total number of 
antinodes in the above example to 9.

The original example now has 34 antinodes, including the antinodes that 
appear on every antenna:

##....#....#
.#.#....0...
..#.#0....#.
..##...0....
....0....#..
.#...#A....#
...#..#.....
#....#.#....
..#.....A...
....#....A..
.#........#.
...#......##

Calculate the impact of the signal using this updated model. How many 
unique locations within the bounds of the map contain an antinode?
'''

# READ INPUT LINE BY LINE
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
assert len(lines) == 50

# NORMALIZE INPUT TO A GRID
input = [list(l.strip()) for l in lines]
assert len(input) == 50

# MAKE A MAP OF ALL ANTENNAS AND POSITIONS
map = {}
for row in range(len(input)):
    for col in range(len( input[row] )):
        if input[row][col] != '.':
            antenna = input[row][col]
            if antenna in map.keys():
                map[antenna] += [(row,col)]
            else:
                map[antenna]  = [(row,col)]


def all_pairs(collection):
    pairs = []
    for i in range(len(collection)):
        for j in range(i+1, len(collection)):
            pairs.append( (collection[i],collection[j]) )
    return pairs

def in_bounds(p, matrix):
    return p[0] in range(len(matrix)) and p[1] in range(len(matrix[ p[0] ]))

def point_distance(a, b):
    return (b[0]-a[0], b[1]-a[1])

def point_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


#SOLUTION
antinodes = set()

for antenna, positions in map.items():
    for p in all_pairs(positions):
        distance = point_distance(p[1], p[0])
        antinode = p[0]
        while in_bounds(antinode, input):
            antinodes.add(antinode)
            antinode = point_add(antinode, distance)
        distance = point_distance(p[0], p[1])
        antinode = p[1]
        while in_bounds(antinode, input):
            antinodes.add(antinode)
            antinode = point_add(antinode, distance)

print(len(antinodes)) # 1015
