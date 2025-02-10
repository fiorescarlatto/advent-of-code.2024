with open('input.txt', 'r', encoding='utf-8') as file:
    input,wires = file.read().split('\n\n')

input = [i.split(':') for i in input.splitlines()]
input = {i[0]: int(i[1]) for i in input}

wires = [w.split(' -> ') for w in wires.splitlines()]
wires = {w[1]: w[0].split(' ') for w in wires}

def OR(A, B):
    return A | B
def AND(A, B):
    return A & B
def XOR(A, B):
    return A ^ B

gate = {'OR':OR, 'AND':AND, 'XOR':XOR}

def find(A:str, G:str, B:str):
    for w in wires:
        if wires[w] == [A, G, B] or wires[w] == [B, G, A]:
            return w
    return ''

def swap(A:str, B:str):
    if A in wires and B in wires:
        swap = wires[A]
        wires[A] = wires[B]
        wires[B] = swap

i = 1
prev = 'ppj'
solution = []
while i < 45:
    x = f'x{i:02}'
    y = f'y{i:02}'
    z = f'z{i:02}'
    
    AxB   = find(x, 'XOR', y)
    AaB   = find(x, 'AND', y)
    sum   = find(AxB, 'XOR', prev)
    carry = find(AxB, 'AND', prev)
    carry = find(AaB, 'OR' , carry)

    print(f'{i:02} x:{AxB}, a:{AaB}, s:{sum}, c:{carry}')

    if sum == '': # CARRY ERROR, SWAP CARRY WIRES
        swap(AaB, AxB)
        solution += [AxB, AaB]
        print(f'swapped {AxB} <-> {AaB}')
        continue
    elif sum != z: # SUM ERROR, SWAP SUM WIRES
        swap(z, sum)
        solution += [z, sum]
        print(f'swapped {z} <-> {sum}')
        continue

    prev = carry
    i += 1

print()
solution.sort()
print(','.join(solution)) # fvw,grf,mdb,nwq,wpq,z18,z22,z36
