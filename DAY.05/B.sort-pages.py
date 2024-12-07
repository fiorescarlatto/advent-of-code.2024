'''
--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, you 
have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to 
put the page numbers in the right order. For the above example, here are 
the three incorrectly-ordered updates and their correct orderings:

  - 75,97,47,61,53 becomes 97,75,47,61,53.
  - 61,13,29 becomes 61,29,13.
  - 97,13,75,29,47 becomes 97,75,47,29,13.

After taking only the incorrectly-ordered updates and ordering them 
correctly, their middle page numbers are 47, 29, and 47. Adding these 
together produces 123.

Find the updates which are not in the correct order. What do you get if you 
add up the middle page numbers after correctly ordering just those updates?
'''

# OPEN THE INPUT FILE
file = open('input.txt', 'r', encoding='utf-8')

# READ ALL THE PAGE RULES
first: list[str] = []
for i in range(1176):
    first.append(file.readline())
assert file.readline() == '\n'

# READ ALL THE MANUALS
second = file.readlines()

file.close()

# NORMALIZES THE INPUT
# CREATE DICTIONARY OF PAGE RULES
rules = {}
for r in first:
    before,after = r.strip().split('|')
    if before not in rules.keys():
        rules[before] = set()
    rules[before].add(after)

# CREATE LIST OF MANUALS
manuals = [s.strip().split(',') for s in second]


def middle_page(manual: list[str]):
    return int(manual[len(manual)//2])

def page_is_ordered(previous_pages: list[str], not_allowed: set):
    for p in previous_pages:
        if p in not_allowed:
            return False
    return True

def manual_is_ordered(manual: list[str], rules: dict[set]):
    for i in range(len(manual)):
        previous_pages = manual[0:i]
        page_rules = rules[manual[i]] if manual[i] in rules.keys() else set()
        if not page_is_ordered(previous_pages, page_rules):
            return False
    return True

def sort_pages(manual: list[str], rules: dict[set]):
    sorted = []
    for page in manual:
        if len(sorted) == 0:
            sorted.append(page)
            continue

        page_rules = rules[page] if page in rules.keys() else set()
        for pos in range(len(sorted), -1, -1):
            if page_is_ordered(sorted[0:pos], page_rules):
                break
        sorted.insert(pos, page)
    return sorted


# SOLUTION
total = 0

for m in manuals:
    if not manual_is_ordered(m, rules):
        sorted_manual = sort_pages(m, rules)
        total += middle_page(sorted_manual)

print(total) # 4151
