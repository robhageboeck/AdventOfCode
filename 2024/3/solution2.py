import re

def compute(instruction):
  a = int(instruction.split('(')[1].split(',')[0])
  b = int(instruction.split(',')[1].split(')')[0])
  return a * b

with open("input.txt") as f:
  searchableInput = ''
  for line in f.readlines():
    searchableInput += line
  do = True
  instructions = []
  for matchingInstruction in re.finditer(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', searchableInput):
    if matchingInstruction.group()[0:4] == 'do()':
      do = True
    elif matchingInstruction.group()[0:5] == 'don\'t':
      do = False
    elif do and matchingInstruction.group()[0:3] == 'mul':
      instructions.append(matchingInstruction.group())
  multiplications = [compute(instruction) for instruction in instructions]
  print(f'The sum of all multiplications is {sum(multiplications)}')