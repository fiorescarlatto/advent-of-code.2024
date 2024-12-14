
# READ INPUT FROM FILE
file = open('input.txt', 'r', encoding='utf-8')
input = []
while True:
    a = file.readline()
    b = file.readline()
    p = file.readline()
    _ = file.readline()
    if a == '':
        break
    input.append([a,b,p])
file.close()

# NORMALIZES THE INPUT
for i in range(len(input)):
    input[i][0] = input[i][0][10:].strip()
    input[i][1] = input[i][1][10:].strip()
    input[i][2] = input[i][2][ 7:].strip()
    input[i][0] = [int(x[2:]) for x in input[i][0].split(', ')]
    input[i][1] = [int(x[2:]) for x in input[i][1].split(', ')]
    input[i][2] = [int(x[2:]) for x in input[i][2].split(', ')]
    # CORRECTS FOR MEASUREMENT MISTAKE
    input[i][2] = [x+10000000000000 for x in input[i][2]]


from fractions import Fraction
import math

class point:
    x: Fraction
    y: Fraction

    def __init__(self, x, y = None):
        if y == None:
            self.x = Fraction(x[0])
            self.y = Fraction(x[1])
        else:
            self.x = Fraction(x)
            self.y = Fraction(y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y)
    def __sub__(self, other):
        return point(self.x-other.x, self.y-other.y)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

def intersection(A:point, B:point, C:point, D:point):
    ab = Fraction(B.y - A.y, B.x - A.x)
    cd = Fraction(D.y - C.y, D.x - C.x)
    x = (ab*A.x - cd*C.x + C.y-A.y) / (ab - cd)
    y = ab * (x - A.x) + A.y
    return point(x, y)


# SOLUTION
total = 0

for machine in input:
    # GET THE COORDINATES OF A, B AND THE PRIZE P
    a = point(machine[0])
    b = point(machine[1])
    p = point(machine[2])

    if a.magnitude() / 3 > b.magnitude():
        print('this doesnt work!')
        break
    
    # CALCULATES THE INTERSECTION OF OB and PA
    o = point(0, 0) # ORIGIN
    i = intersection(o, b, p, p+a)

    if i.x.is_integer() and i.y.is_integer():
        if i.x <= p.x and i.y <= p.y: # inside the bounds
            if i.x % b.x == 0 and i.y % b.y == 0: # divisible by vector b
                if i.x // b.x == i.y // b.y: # dimensions aligned
                    tokens = i.x // b.x
                    rx = p.x-i.x
                    ry = p.y-i.y
                    if rx % a.x == 0 and ry % a.y == 0: #remainder divisible by vector a
                        if rx // a.x == ry // a.y: # dimensons aligned
                            tokens += 3 * rx // a.x
                            total += tokens

print(total) # 107824497933339
