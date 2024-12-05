from common import isIncreasing, isDecreasing, safeChanges

with open("input.txt") as f:
  reports = []
  for line in f.readlines():
    reports.append(list(map(int, line.split())))
  safe = 0
  for report in reports:
    if (isIncreasing(report) or isDecreasing(report)) and safeChanges(report):
      safe += 1
  print(f'The number of safe reports is {safe}')
