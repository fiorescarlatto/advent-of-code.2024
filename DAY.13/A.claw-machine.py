'''
--- Day 13: Claw Contraption ---
Next up: the lobby of a resort on a tropical island. The Historians take a 
moment to admire the hexagonal floor tiles before spreading out.

Fortunately, it looks like the resort has a new arcade! Maybe you can win 
some prizes from the claw machines?

The claw machines here are a little unusual. Instead of a joystick or 
directional buttons to control the claw, these machines have two buttons 
labeled A and B. Worse, you can't just put in a token and play; it costs 
3 tokens to push the A button and 1 token to push the B button.

With a little experimentation, you figure out that each machine's buttons 
are configured to move the claw a specific amount to the right (along the X 
axis) and a specific amount forward (along the Y axis) each time that 
button is pressed.

Each machine contains one prize; to win the prize, the claw must be 
positioned exactly above the prize on both the X and Y axes.

You wonder: what is the smallest number of tokens you would have to spend 
to win as many prizes as possible? You assemble a list of every machine's 
button behavior and prize location (your puzzle input). For example:

Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279

This list describes the button configuration and prize location of four 
different claw machines.

For now, consider just the first claw machine in the list:

  - Pushing the machine's A button would move the claw 94 units along the 
  - X axis and 34 units along the Y axis.
  - Pushing the B button would move the claw 22 units along the X axis and 
  - 67 units along the Y axis.
  - The prize is located at X=8400, Y=5400; this means that from the 
  - claw's initial position, it would need to move exactly 8400 units 
  - along the X axis and exactly 5400 units along the Y axis to be 
  - perfectly aligned with the prize in this machine.

The cheapest way to win the prize is by pushing the A button 80 times and 
the B button 40 times. This would line up the claw along the X axis (because 
80*94 + 40*22 = 8400) and along the Y axis (because 80*34 + 40*67 = 5400). 
Doing this would cost 80*3 tokens for the A presses and 40*1 for the B 
presses, a total of 280 tokens.

For the second and fourth claw machines, there is no combination of A and B 
presses that will ever win a prize.

For the third claw machine, the cheapest way to win the prize is by pushing 
the A button 38 times and the B button 86 times. Doing this would cost a 
total of 200 tokens.

So, the most prizes you could possibly win is two; the minimum tokens you 
would have to spend to win all (two) prizes is 480.

You estimate that each button would need to be pressed no more than 100 
times to win a prize. How else would someone be expected to play?

Figure out how to win as many prizes as possible. What is the fewest tokens 
you would have to spend to win all possible prizes?
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


# SOLUTION
total = 0

for machine in input:
    # GET THE COORDINATES OF A, B AND THE PRIZE P
    ax,ay = machine[0]
    bx,by = machine[1]
    px,py = machine[2]

    # TOKEN COST FOR THIS MACHINE
    tokens = 0

    for i in range(101):
        for j in range(101):
            if i == 0 and j == 0:
                continue
            # IF I REACH THE POINT P
            if px == i*ax + j*bx and py == i*ay + j*by:
                # CALCULATE THE REQUIRED TOKENS
                tokens = 3*i + j

    total += tokens

print(total) # 26299
