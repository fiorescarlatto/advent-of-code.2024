
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

PROGRAM_LITERAL = lines[4][9:].strip().replace(',', '')
PROGRAM = [int(x) for x in PROGRAM_LITERAL]
REG = [int(x[12:]) for x in lines[:3]]
A, B, C = (0, 1, 2)
IP = 0
OUT = ''


def combo(op: int) -> int:
    if op <= 3:
        return op
    elif op == 4:
        return REG[A]
    elif op == 5:
        return REG[B]
    elif op == 6:
        return REG[C]
    raise Exception

def adv(op): # 0
    global IP, REG
    REG[A] = REG[A] // (2 ** combo(op))
    IP = IP + 2

def bxl(lit): # 1
    global IP, REG
    REG[B] = REG[B] ^ lit
    IP = IP + 2

def bst(op): # 2
    global IP, REG
    REG[B] = combo(op) % 8
    IP = IP + 2

def jnz(lit): # 3
    global IP, REG
    if REG[A] == 0:
        IP = IP + 2
    else:
        IP = lit

def bxc(none): # 4
    global IP, REG
    REG[B] = REG[B] ^ REG[C]
    IP = IP + 2

def out(op): # 5
    global IP, OUT
    OUT = OUT + str( combo(op) % 8 )
    IP = IP + 2

def bdv(op): # 6
    global IP, REG
    REG[B] = REG[A] // (2 ** combo(op))
    IP = IP + 2

def cdv(op): # 7
    global IP, REG
    REG[C] = REG[A] // (2 ** combo(op))
    IP = IP + 2


decode = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

for i in range(1):
    OUT = ''
    IP  = 0

    #2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0
    a = 7*8
    a = (a + 4)*8 # 2 4
    a = (a + 3)*8 # 2 3 6
    a = (a + 1)*8 # 1
    a = (a + 0)*8 # 0 6
    a = (a + 0)*8 # 0 4 5
    a = (a + 3)*8 # 3
    a = (a + 0)*8 # 0 7
    a = (a + 3)*8 # 3
    a = (a + 6)*8 # 1 6
    a = (a + 6)*8 # 2 6
    a = (a + 0)*8 # 0 1 2
    a = (a + 1)*8 # 1
    a = (a + 6)*8 # 1 6
    a = (a + 3)*8 # 3
    a = a + 3 # 3 5

    for b in range(8):
        c = (a + b) // (2 ** (b ^ 7))
        o = (b ^ c) % 8
        print(b, o)

    REG = [a, 0, 0]

    while IP < len(PROGRAM):
        instruction = PROGRAM[IP]
        operand = PROGRAM[IP+1]
        decode[instruction](operand)

    if OUT == PROGRAM_LITERAL:
        print(a)
    print(OUT)
