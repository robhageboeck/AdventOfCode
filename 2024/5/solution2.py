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

def fixWithRules(update, rules):
  for rule in rules:
    first, second = rule
    if first in update and second in update and update.index(first) > update.index(second):
      update[update.index(first)], update[update.index(second)] = update[update.index(second)], update[update.index(first)]
  if not matchesRules(update, rules):
    return fixWithRules(update, rules)
  return update

with open('input.txt') as f:
  rules = []
  updates = []
  for line in [l.strip() for l in f.readlines()]:
    if len(line) != 0:
      if isRule(line):
        rules.append(parseRule(line))
      if isUpdate(line):
        updates.append(parseUpdate(line))
  notMatchCount = 0
  sumOfMiddlePages = 0
  for update in updates:
    if not matchesRules(update, rules):
      notMatchCount += 1
      updatedUpdate = fixWithRules(update, rules)
      sumOfMiddlePages += int(updatedUpdate[len(updatedUpdate) // 2])
  print(f'{notMatchCount} updates matched all rules')
  print(f'Sum of middle pages: {sumOfMiddlePages}')
