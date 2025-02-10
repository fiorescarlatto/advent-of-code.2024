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

# :::::::::::::::::::::::::::::  INPUT  :::::::::::::::::::::::::::::: #
with open('input.txt', 'r', encoding='utf-8') as file:
    # READS THE FILE LINE BY LINE
    lines = file.readlines()

# CREATES A LIST OF REPORTS
reports = []

for report in lines:
    # CREATES A LIST OF LEVELS
    levels = [int(x) for x in report.split(' ')]
    # ADDS IT TO THE LIST OF REPORTS
    reports.append( levels )

# ::::::::::::::::::::::::::::  SOLUTION  :::::::::::::::::::::::::::: #
def is_safe(report:list[int]) -> bool:
    '''
    Checks if a given report is safe.
    '''
    # CALCULATES ASCENDING OR DESCENDING FACTOR
    factor = -1 if report[0] < report[1] else 1
    # FOR EACH LEVEL AFTER THE FIRST
    for i in range(1, len(report)):
        # CALCULATES THE CHANGE
        change = (report[i-1] - report[i]) * factor
        # CHECKS IF CHANGE IS BETWEEN TOLERANCE
        if change < 1 or change > 3:
            return False
    return True

def within_tolerance(report:list[int]) -> bool:
    '''
    Checks if a given report has at most one error.
    '''
    for i in range(len(report)):
        # CREATES A COPY OF THE ORIGINAL REPORT
        cleaned = report.copy()
        # REMOVES ONE (POSSIBLY) PROBLEMATIC LEVEL 
        cleaned.pop(i)
        # CHECK IF THE CLEANED REPORT IS SAFE
        if is_safe(cleaned):
            return True
    return False

# GETS THE NUMBER OF SAFE REPORTS 
total = sum(map(within_tolerance, reports))

print(total) # 612
