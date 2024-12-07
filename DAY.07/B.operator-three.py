'''
--- Part Two ---
The engineers seem concerned; the total calibration result you gave them is 
nowhere close to being within safety tolerances. Just then, you spot your 
mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right 
inputs into a single number. For example, 12 || 345 would become 12345. All 
operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only 
addition and multiplication, the above example has three more equations 
that can be made true by inserting operators:

  - 156: 15 6 can be made true through a single concatenation: 
    15 || 6 = 156.
  - 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
  - 192: 17 8 14 can be made true using 17 || 8 + 14.

Adding up all six test values (the three that could be made before using 
only + and * plus the new three that can now be made by also using ||) 
produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which 
equations could possibly be true. What is their total calibration result?
'''

# INPUT FROM FILE LINE BY LINE
file = open('input.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()
assert len(lines) == 850 # input.txt

# NORMALIZE THE INPUT
input = []

for l in lines:
    value,numbers = l.split(':')
    # CONVERT NUMBERS TO INT
    value   = int( value )
    numbers = [int(x) for x in numbers.strip().split(' ')]

    input.append( (value,numbers) )


def all_results(numbers):
    result = [ numbers[0] ]
    for i in range(1, len(numbers)):
        r = [int( str(x) + str( numbers[i] ) ) for x in result]
        r+= [x * numbers[i] for x in result]
        r+= [x + numbers[i] for x in result]
        result = r
    return result


# SOLUTION
total = 0

for i in input:
    value,numbers = i
    if value in all_results(numbers):
        total += value

print(total) # 227921760109726
