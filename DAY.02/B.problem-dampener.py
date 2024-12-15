'''
--- Part Two ---
The engineers are surprised by the low number of safe reports until they 
realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor 
safety systems tolerate a single bad level in what would otherwise be a 
safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from 
an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

  - 7 6 4 2 1: Safe without removing any level.
  - 1 2 7 8 9: Unsafe regardless of which level is removed.
  - 9 7 6 2 1: Unsafe regardless of which level is removed.
  - 1 3 2 4 5: Safe by removing the second level, 3.
  - 8 6 4 4 1: Safe by removing the third level, 4.
  - 1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can 
remove a single level from unsafe reports. How many reports are now safe?
'''

# READS THE INPUT LINE BY LINE
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# NORMALIZES THE INPUT
reports:list[list] = []

for report in lines:
    reports.append( [int(level) for level in report.split(' ')] )


def is_safe(report: list[int]) -> bool:
    if len(report) <= 1:
        return True
    # CALCULATES ASCENDING/DESCENDING FACTOR
    factor = -1 if report[0] < report[1] else 1
    # FOR EACH LEVEL AFTER THE FIRST
    for i in range(1, len(report)):
        # CALCULATES THE CHANGE AND CHECKS IF VALID
        change = (report[i-1] - report[i]) * factor
        if change < 1 or change > 3:
            return False
    return True


# SOLUTION
total = 0

for report in reports:
    if is_safe(report):
        total += 1
    else:
        # TRY REMOVING ONE PROBLEM LEVEL
        for i in range(len(report)):
            # CREATE DAMPENED REPORT
            dampened = report.copy()
            dampened.pop(i)
            # CHECK IF IT'S SAFE NOW
            if is_safe(dampened):
                total += 1
                break

print(total) # 612
