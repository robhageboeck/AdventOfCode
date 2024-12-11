def isRule(s):
  return '|' in s

def parseRule(s):
  return s.split('|')

def isUpdate(s):
  return ',' in s

def parseUpdate(s):
  return s.split(',')

def matchesRules(update, rules):
  for r in range(len(rules)):
    first, second = rules[r]
    if first in update and second in update and update.index(first) > update.index(second):
      return False
  return True

with open('input.txt') as f:
  rules = []
  updates = []
  for line in [l.strip() for l in f.readlines()]:
    if len(line) != 0:
      if isRule(line):
        rules.append(parseRule(line))
      if isUpdate(line):
        updates.append(parseUpdate(line))
  count = 0
  sumOfMiddlePages = 0
  for update in updates:
    if matchesRules(update, rules):
      print(f'Update {update} matched all rules')
      count += 1
      sumOfMiddlePages += int(update[len(update) // 2])
  print(f'{count} updates matched all rules')
  print(f'Sum of middle pages: {sumOfMiddlePages}')