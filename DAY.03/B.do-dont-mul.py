'''
--- Part Two ---
As you scan through the corrupted memory, you notice that some of the 
conditional statements are also still intact. If you handle some of the 
uncorrupted conditional statements in the program, you might be able to get 
an even more accurate result.

There are two new instructions you'll need to handle:

  - The do() instruction enables future mul instructions.
  - The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning 
of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time 
the mul(5,5) and mul(11,8) instructions are disabled because there is a 
don't() instruction before them. The other mul instructions function 
normally, including the one at the end that gets re-enabled by a do() 
instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the 
results of just the enabled multiplications?
'''

# READS THE WHOLE FILE INTO A SINGLE STRING
with open('input.txt', 'r', encoding='utf-8') as file:
    memory = file.read()

import re
# USING REGULAR EXPRESSIONS TO FIND mul(n,n)|do()|don't()
regex = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)|do\(\)|don't\(\)"
instructions:list[str] = re.findall(regex, memory)

# SOLUTION
total = 0
execute = True

# CALCULATES EACH MULT
for i in instructions:
    if i == 'do()':
        execute = True
    elif i == "don't()":
        execute = False
    elif execute:
        # NORMALIZES THE mul(n,n) INSTRUCTION TO A [list] OF [int]
        i = i.replace('mul(', '')
        i = i.replace(')', '')
        i = [int(x) for x in i.split(',')]
        # CALCULATES THE mul INSTRUCTION
        total += i[0] * i[1]

print(total) # 98729041
