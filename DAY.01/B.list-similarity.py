'''
--- Part Two ---
Your analysis only confirmed what everyone feared: the two lists of 
location IDs are indeed very different.

Or are they?

The Historians can't agree on which group made the mistakes or how to read 
most of the Chief's handwriting, but in the commotion you notice an 
interesting detail: a lot of location IDs appear in both lists! Maybe the 
other numbers aren't location IDs at all but rather misinterpreted 
handwriting.

This time, you'll need to figure out exactly how often each number from the 
left list appears in the right list. Calculate a total similarity score by 
adding up each number in the left list after multiplying it by the number 
of times that number appears in the right list.

Here are the same example lists again:

3   4
4   3
2   5
1   3
3   9
3   3

For these example lists, here is the process of finding the similarity 
score:

  - The first number in the left list is 3. It appears in the right list 
    three times, so the similarity score increases by 3 * 3 = 9.
  - The second number in the left list is 4. It appears in the right list 
    once, so the similarity score increases by 4 * 1 = 4.
  - The third number in the left list is 2. It does not appear in the 
    right list, so the similarity score does not increase (2 * 0 = 0).
  - The fourth number, 1, also does not appear in the right list.
  - The fifth number, 3, appears in the right list three times; the 
    similarity score increases by 9.
  - The last number, 3, appears in the right list three times; the 
    similarity score again increases by 9.

So, for these example lists, the similarity score at the end of this 
process is 31 (9 + 4 + 0 + 0 + 9 + 9).

Once again consider your left and right lists. What is their similarity 
score?
'''

# READS THE INPUT LINE BY LINE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# NORMALIZES THE INPUT
list_A = []
list_B = []

for l in lines:
    a,b = l.split('   ')
    list_A.append( int(a) )
    list_B.append( int(b) )


def counts(list:list) -> dict:
    counts = {}
    for element in list:
        if element in counts.keys():
            counts[element] += 1
        else:
            counts[element]  = 1
    return counts


# SOLUTION
amounts = counts(list_B)
similarity = 0

for a in list_A:
    if a in amounts.keys():
        similarity += a * amounts[a]

print(similarity) # 22565391
