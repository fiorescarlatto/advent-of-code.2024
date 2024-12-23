
codes   = ['279A', '286A', '508A', '463A', '246A']
example = ['029A', '980A', '179A', '456A', '379A']

keypad = {
    '7':(0,0),'8':(0,1),'9':(0,2),
    '4':(1,0),'5':(1,1),'6':(1,2),
    '1':(2,0),'2':(2,1),'3':(2,2),
    ' ':(3,0),'0':(3,1),'A':(3,2),
}

name = ['^', 'A', '<', 'v', '>']
# CREATE A STARTING DICTIONARY {PATH:COST}
D = { x:{ y:1 for y in name } for x in name }
# CREATE A STEP DICTIONARY
step = {
    '^':{'^':'A', 'A':'>A', '<':'v<A', 'v':'vA', '>':'v>A'},
    'A':{'^':'<A', 'A':'A', '<':'v<<A', 'v':'<vA', '>':'vA'},
    '<':{'^':'>^A', 'A':'>>^A', '<':'A', 'v':'>A', '>':'>>A'},
    'v':{'^':'^A', 'A':'^>A', '<':'<A', 'v':'A', '>':'>A'},
    '>':{'^':'<^A', 'A':'^A', '<':'<<A', 'v':'<A', '>':'A'},
}


def dp_step(P) -> dict:
    D = {}
    for frm in name:
        D[frm] = {}
        for to in name:
            start = 'A'
            D[frm][to] = 0
            for char in step[frm][to]:
                D[frm][to] += P[start][char]
                start = char
    return D

def add(A:tuple, B:tuple) -> tuple:
    return (A[0] + B[0], A[1] + B[1])

def sequence(code):
    start = 'A'
    sequence = ''
    for char in code:
        step  = ''
        down  = keypad[char][0] - keypad[start][0]
        right = keypad[char][1] - keypad[start][1]
        hole  = False
        if right < 0:
            step += '<' * abs(right)
            if add(keypad[start], (0,right)) == keypad[' ']:
                hole = True
        if down > 0:
            step += 'v' * abs(down)
            if add(keypad[start], (down, 0)) == keypad[' ']:
                hole = True
        if right > 0:
            step += '>' * abs(right)
        if down < 0:
            step += '^' * abs(down)
        if hole:
            step = step[::-1]
        sequence += step+'A'
        start = char
    return sequence

def length(code, D):
    total = 0
    start = 'A'
    for char in sequence(code):
        total += D[start][char]
        start = char
    return total


# SOLUTION
total = 0
# CREATES A QUEUE OF 2 ROBOTS
for _ in range(2):
    D = dp_step(D)
# MEASURES THE STEPS
for code in codes:
    total += length(code, D) * int(code[:-1])

print(total) # 125742


# SOLUTION
total = 0
# ADDS 23 MORE ROBOTS
for _ in range(23):
    D = dp_step(D)
# MEASURES THE STEPS
for code in codes:
    total += length(code, D) * int(code[:-1])

print(total) # 157055032722640
