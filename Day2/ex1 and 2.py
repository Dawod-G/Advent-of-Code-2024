print("Day 2 - Exercise 1 and 2")

def red_nosed_reports(report):
    levels = list(map(int, report.split()))

    def is_valid(levels):
        increase = True
        decrease = True
        valid_level_difference = True

        for i in range(len(levels) - 1):
            if levels[i] >= levels[i + 1]:
                increase = False
            if levels[i] <= levels[i + 1]:
                decrease = False
            if not (1 <= abs(levels[i] - levels[i + 1]) <= 3):
                valid_level_difference = False

        return (increase or decrease) and valid_level_difference

    if is_valid(levels):
        return True

    for i in range(len(levels)):
        if is_valid(levels[:i] + levels[i + 1:]):
            return True
    return False

with open('input.txt', 'r') as file:
    reports = file.readlines()

safe_reports = 0

for line in reports:
    if red_nosed_reports(line):
        safe_reports = safe_reports + 1

print(safe_reports, "report(s) are safe")