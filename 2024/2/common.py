def isIncreasing(report):
  for i in range(1, len(report)):
    if report[i] < report[i - 1]:
      return False
  return True

def isDecreasing(report):
  for i in range(1, len(report)):
    if report[i] > report[i - 1]:
      return False
  return True

def safeChanges(report):
  for i in range(1, len(report)):
    if abs(report[i] - report[i - 1]) not in range(1, 4):
      return False
  return True
