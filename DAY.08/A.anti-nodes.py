'''
--- Day 8: Resonant Collinearity ---
You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge 
antenna. Much to your surprise, it seems to have been reconfigured to emit 
a signal that makes people 0.1% more likely to buy Easter Bunny brand 
Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such 
antennas. Each antenna is tuned to a specific frequency indicated by a 
single lowercase letter, uppercase letter, or digit. You create a map (your 
puzzle input) of these antennas. For example:

............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............

The signal only applies its nefarious effect at specific antinodes based on 
the resonant frequencies of the antennas. In particular, an antinode occurs 
at any point that is perfectly in line with two antennas of the same 
frequency - but only when one of the antennas is twice as far away as the 
other. This means that for any pair of antennas with the same frequency, 
there are two antinodes, one on either side of them.

So, for these two antennas with frequency a, they create the two antinodes 
marked with #:

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........

Adding a third antenna with the same frequency creates several more 
antinodes. It would ideally add four antinodes, but two are off the right 
side of the map, so instead it adds only two:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
..........

Antennas with different frequencies don't create antinodes; A and a count 
as different frequencies. However, antinodes can occur at locations that 
contain antennas. In this diagram, the lone antenna with frequency capital 
A creates no antinodes but has a lowercase-a-frequency antinode at its 
location:

..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
..........

The first example has antennas with two different frequencies, so the 
antinodes they create look like this, plus an antinode overlapping the 
topmost A-frequency antenna:

......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.

Because the topmost A-frequency antenna overlaps with a 0-frequency 
antinode, there are 14 total unique locations that contain an antinode 
within the bounds of the map.

Calculate the impact of the signal. How many unique locations within the 
bounds of the map contain an antinode?
'''

# READ INPUT LINE BY LINE
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
assert len(lines) == 50

# NORMALIZE INPUT TO A GRID
input = [list(l.strip()) for l in lines]
assert len(input) == 50

# MAKE A MAP OF ANTENNAS TO EXISTING POSITIONS
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
        antinode = point_add(p[0], distance)
        if in_bounds(antinode, input):
            antinodes.add(antinode)
        distance = point_distance(p[0], p[1])
        antinode = point_add(p[1], distance)
        if in_bounds(antinode, input):
            antinodes.add(antinode)

print(len(antinodes)) # 291
