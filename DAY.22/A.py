
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

secrets = [int(x) for x in lines]
example = [1, 10, 100, 2024]

def mix(A, B):
    return A ^ B

def prune(A):
    return A % 16777216 # LAST 24 BITS

def random(seed):
    seed = prune(mix(seed, seed *  64))   # s ^ s << 6  & 24bit
    seed = prune(mix(seed, seed // 32))   # s ^ s >> 5  & 24bit
    seed = prune(mix(seed, seed * 2048))  # s ^ s << 11 & 24bit
    return seed

def market_cap(seed, end):
    for _ in range(end):
        seed = random(seed)
    return seed


# SOLUTION
total = 0

for number in secrets:
    total += market_cap(number, 2000)
    
print(total) # 13461553007
