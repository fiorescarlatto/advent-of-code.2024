'''
--- Part Two ---
As you go to win the first prize, you discover that the claw is nowhere 
near where you expected it would be. Due to a unit conversion error in your 
measurements, the position of every prize is actually 10000000000000 higher 
on both the X and Y axis!

Add 10000000000000 to the X and Y position of every prize. After making 
this change, the example above would now look like this:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=10000000008400, Y=10000000005400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=10000000012748, Y=10000000012176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=10000000007870, Y=10000000006450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=10000000018641, Y=10000000010279

Now, it is only possible to win a prize on the second and fourth claw 
machines. Unfortunately, it will take many more than 100 presses to do so.

Using the corrected prize coordinates, figure out how to win as many prizes 
as possible. What is the fewest tokens you would have to spend to win all 
possible prizes?
'''

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
