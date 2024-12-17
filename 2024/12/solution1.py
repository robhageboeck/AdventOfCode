import sys

def log(*args):
  if TEST:
    print(*args)

def getFencingCost(garden, region, y, x):
  cost = 0
  if x == 0 or garden[y][x - 1] != region:
    cost += 1
  if x == len(garden[0]) - 1 or garden[y][x + 1] != region:
    cost += 1
  if y == 0 or garden[y - 1][x] != region:
    cost += 1
  if y == len(garden) - 1 or garden[y + 1][x] != region:
    cost += 1
  return cost

def getCostOfRegion(garden, j, i):
  visited = []
  region = garden[j][i]
  print(f'Evaluating New Region: {region}', j, i)
  stack = [(j, i)]
  regionFencing = 0
  while stack:
    y, x = stack.pop()
    if (y, x) in visited:
      continue
    visited.append((y, x))
    if x > 0 and garden[y][x - 1] == region:
      stack.append((y, x - 1))
    if x < len(garden[0]) - 1 and garden[y][x + 1] == region:
      stack.append((y, x + 1))
    if y < len(garden) - 1 and garden[y + 1][x] == region:
      stack.append((y + 1, x))
    if y > 0 and garden[y - 1][x] == region:
      stack.append((y - 1, x))
    regionFencing += getFencingCost(garden, region, y, x)
  return len(visited) * regionFencing, visited

def fenceCost(garden):
  cost = 0
  visited = []
  for y in range(len(garden)):
    for x in range(len(garden[0])):
      if (y, x) not in visited:
        regionCost, visitedNodes = getCostOfRegion(garden, y, x)
        cost += regionCost
        visited += visitedNodes
  return cost

def solve(filename):
  with open(filename) as f:
    garden = []
    for line in [l.strip() for l in f.readlines()]:
      garden.append(list(line))
    cost = fenceCost(garden)
    print(f'Cost of fencing: {cost}')
  
if __name__ == '__main__':
  filename = sys.argv[1]
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename
  solve(filename)