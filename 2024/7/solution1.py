def possibleCombinations(n):
  operations = ['+', '*']
  combinations = []
  for i in range(2**n):
    combination = []
    for j in range(n):
      combination.append(operations[(i >> j) & 1])
    combinations.append(combination)
  return combinations

def solvable(total, operands):
  totalPossibleCombinations = len(operands) - 1
  combinations = possibleCombinations(totalPossibleCombinations)
  for combination in combinations:
    currentTotal = operands[0]
    for i in range(len(operands) - 1):
      if combination[i] == '+':
        currentTotal += operands[i+1]
      else:
        currentTotal *= operands[i+1]
    if currentTotal == total:
      return True
  return False

with open('input.txt') as f:
  solvableSum = 0
  for t,ops in [map(lambda i: i.strip(), l.split(':')) for l in f.readlines()]:
    total = int(t)
    operands = list(map(int, ops.split(' ')))
    if solvable(total, operands):
      solvableSum += total
  print(f'The sum of all solvable test cases is {solvableSum}')