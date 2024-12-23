
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

secrets = [int(x) for x in lines]
example = [1, 2, 3, 2024]


def random(seed):
    # IMPROVED RANDOM FOR SPEED
    seed = (seed ^ (seed << 6 )) & 16777215
    seed = (seed ^ (seed >> 5 )) & 16777215
    seed = (seed ^ (seed << 11)) & 16777215
    return seed

def market(seed):
    market = {}
    cost = seed % 10
    keys = (0, 0, 0, 0)

    for _ in range(3):
        seed = random(seed)
        diff = seed % 10 - cost
        cost = seed % 10
        keys = (keys[1], keys[2], keys[3], diff)
    
    for _ in range(1997):
        seed = random(seed)
        diff = seed % 10 - cost
        cost = seed % 10
        keys = (keys[1], keys[2], keys[3], diff)
        if keys not in market.keys():
            market[keys] = cost
    
    return market

def join(A:dict, B:dict) -> None:
    for k in B.keys():
        if k in A.keys():
            A[k] = A[k] + B[k]
        else:
            A[k] = B[k]


# SOLUTION
M = {}
for number in secrets:
    join(M, market(number))

print(max(M.values())) # 1499
