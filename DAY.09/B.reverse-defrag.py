'''
--- Part Two ---
Upon completion, two things immediately become clear. First, the disk 
definitely has a lot more contiguous free space, just like the amphipod 
hoped. Second, the computer is running much more slowly! Maybe introducing 
all of that file system fragmentation was a bad idea?

The eager amphipod already has a new plan: rather than move individual 
blocks, he'd like to try compacting the files on his disk by moving whole 
files instead.

This time, attempt to move whole files to the leftmost span of free space 
blocks that could fit the file. Attempt to move each file exactly once in 
order of decreasing file ID number starting with the file with the highest 
file ID number. If there is no span of free space to the left of a file 
that is large enough to fit the file, the file does not move.

The first example from above now proceeds differently:

00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..

The process of updating the filesystem checksum is the same; now, this 
example's checksum would be 2858.

Start over, now compacting the amphipod's hard drive using this new method 
instead. What is the resulting filesystem checksum?
'''

# READ THE INPUT FILE
file = open('input.txt', 'r')
line = file.read().strip()
file.close()
assert len(line) == 19999

# NORMALIZES THE INPUT
input = [int(x) for x in line]

# BUILD HELPER STRUCTURES TO QUICKLY ACCESS RELEVANT DATA
file_size  = []
free_space = {}
for i in range(10):
    free_space[i] = []

# GENERATE THE MEMORY STATE FROM THE INPUT
id = 0
empty = False
memory = []

for size in input:
    if empty:
        free_space[size] += [len(memory)]
        memory += [-1]*size
    else:
        file_size += [size]
        memory += [id]*size
        id += 1
    empty = not empty


def find_memory_space(min_size, memory_space):
    pos,size = 999999,0
    for i in range(min_size, 10):
        if memory_space[i][0] < pos:
            pos = memory_space[i][0]
            size = i
    return (pos, size)

def add_memory_space(space, memory_space):
    pos,size = space
    space = memory_space[size]
    for i in range(len(space)):
        if space[i] > pos:
            space.insert(i, pos)
            return
    space.append(pos)


#SOLUTION
tail = len(memory) - 1

while tail > 0:
    if memory[tail] != -1:
        # RETRIVES INFORMATION ABOUT THE FILE AT THE END
        id = memory[tail]
        size = file_size[id]
    
        # FINDS THE FIRST AVIABLE SPACE
        pos,space = find_memory_space(size, free_space)
        if pos < tail:
            # MOVES THE MEMORY
            for i in range(size):
                memory[ pos+i  ] = id
                memory[ tail-i ] = -1
            # UPDATES THE EMPTY SPACE TABLE
            free_space[space].pop(0)
            pos += size
            space -= size
            if space > 0:
                add_memory_space((pos,space), free_space)
    tail -= 1


# CALCULATES THE FINAL CHECKSUM
checksum = 0

for i in range(len(memory)):
    if memory[i] != -1:
        checksum += i * memory[i]

print(checksum) # 6353648390778
