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
file = open('input.txt', 'r', encoding='utf-8')
input = file.readlines()
file.close()
assert len(input) == 1000

# NORMALIZES THE INPUT TO A list[list[int]]
input = [[int(y) for y in x.split(' ')] for x in input]
assert len(input) == 1000


def report_is_safe(report:list[int]):
    if len(report) <= 1:
        return True
    if len(report) == 2:
        return (report[0] != report[1])
    
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
safe_reports = 0

for report in input:
    if report_is_safe(report):
        # EVERYTHING OK
        safe_reports += 1
    else:
        # TRY USING PROBLEM DAMPENER
        for i in range(0, len(report)):
            # CREATE DAMPENED REPORT
            dampened = list(report)
            dampened.pop(i)
            
            # CHECK IF IT'S SAFE NOW
            if report_is_safe(dampened):
                safe_reports += 1
                break

print(safe_reports) # 612
