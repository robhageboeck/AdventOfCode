import re

def compute(instruction):
  a = int(instruction.split('(')[1].split(',')[0])
  b = int(instruction.split(',')[1].split(')')[0])
  return a * b

with open("input.txt") as f:
  rawInput = ''
  for line in f.readlines():
    rawInput += line
  instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', rawInput)
  multiplications = [compute(instruction) for instruction in instructions]
  print(f'The sum of all multiplications is {sum(multiplications)}')