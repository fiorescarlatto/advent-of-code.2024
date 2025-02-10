with open('input.txt', 'r', encoding='utf-8') as file: text = file.read().split('\n\n')
input = {i.split(':')[0]:int(i.split(':')[1]) for i in text[0].splitlines()}
wires = {w.split(' -> ')[1]:w.split(' -> ')[0].split(' ') for w in text[1].splitlines()}
gate  = {'OR':lambda a,b:a|b, 'AND':lambda a,b:a&b, 'XOR':lambda a,b:a^b}
def run(id:str):return gate[wires[id][1]](run(wires[id][0]),run(wires[id][2])) if id in wires else input[id]
print(sum(map(lambda x:2**x[0]*run(x[1]), [(i,f'z{i:02}') for i in range(46)])))