'''
--- Day 23: LAN Party ---
As The Historians wander around a secure area at Easter Bunny HQ, you come 
across posters for a LAN party scheduled for today! Maybe you can find it; 
you connect to a nearby datalink port and download a map of the local 
network (your puzzle input).

The network map provides a list of every connection between two computers. 
For example:

kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn

Each line of text in the network map represents a single connection; the 
line kh-tc represents a connection between the computer named kh and the 
computer named tc. Connections aren't directional; tc-kh would mean exactly 
the same thing.

LAN parties typically involve multiplayer games, so maybe you can locate it 
by finding groups of connected computers. Start by looking for sets of 
three computers where each computer in the set is connected to the other 
two computers.

In this example, there are 12 such sets of three inter-connected computers:

aq,cg,yn
aq,vc,wq
co,de,ka
co,de,ta
co,ka,ta
de,ka,ta
kh,qp,ub
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
ub,vc,wq

If the Chief Historian is here, and he's at the LAN party, it would be best 
to know that right away. You're pretty sure his computer's name starts with 
t, so consider only sets of three computers where at least one computer's 
name starts with t. That narrows the list down to 7 sets of three inter-
connected computers:

co,de,ta
co,ka,ta
de,ka,ta
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn

Find all the sets of three inter-connected computers. How many contain at 
least one computer with a name that starts with t?
'''

'''
--- Part Two ---
There are still way too many results to go through them all. You'll have to 
find the LAN party another way and go there yourself.

Since it doesn't seem like any employees are around, you figure they must 
all be at the LAN party. If that's true, the LAN party will be the largest 
set of computers that are all connected to each other. That is, for each 
computer at the LAN party, that computer will have a connection to every 
other computer at the LAN party.

In the above example, the largest set of computers that are all connected 
to each other is made up of co, de, ka, and ta. Each computer in this set 
has a connection to every other computer in the set:

ka-co
ta-co
de-co
ta-ka
de-ta
ka-de

The LAN party posters say that the password to get into the LAN party is 
the name of every computer at the LAN party, sorted alphabetically, then 
joined together with commas. (The people running the LAN party are clearly 
a bunch of nerds.) In this example, the password would be co,de,ka,ta.

What is the password to get into the LAN party?
'''

# READ INPUT FROM FILE
with open('input.txt', 'r', encoding='utf-8') as file:
    input = file.read().split('\n')

# CREATES A GRAPH
network = {}

for connection in input:
    A = connection[:2]
    B = connection[-2:]
    if A not in network.keys():
        network[A] = set()
    if B not in network.keys():
        network[B] = set()
    network[A].add(B)
    network[B].add(A)


# SOLUTION PART 1
total = set()

for A in network.keys():
    if A.startswith('t'):
        for B in network[A]:
            for C in network[A].intersection(network[B]):
                lan = [A, B, C]
                lan.sort()
                lan = ''.join(lan)

                total.add(lan)

print(len(total)) # 1314


def interconnected(lan):
    for pc in lan:
        if len(lan.difference(network[pc])) > 1:
            return False
    return True

# SOLUTION PART 2
party = []

for A in network.keys():
    if A.startswith('t'):
        for B in network[A]:
            lan = network[A].intersection(network[B])
            lan.add(A)
            lan.add(B)

            if len(party) < len(lan) and interconnected(lan):
                party = list(lan)
party.sort()

total = ''

for pc in party:
    total += pc+','

print(total[:-1]) # bg,bu,ce,ga,hw,jw,nf,nt,ox,tj,uu,vk,wp
