import sys

def log(*args):
  if TEST:
    print(*args)

def getTrailheads(index, topoLine):
  heads = []
  for i, char in enumerate(topoLine):
    if char == '0':
      heads.append((index, i))
  return heads

def rateTrailhead(topology, startingTrailhead):
  row, col = startingTrailhead
  paths = 0
  stack = [(row, col, set())]
  while stack:
    row, col, visited = stack.pop()
    if (row, col) in visited:
      continue
    visited.add((row, col))
    if topology[row][col] == 9:
      paths += 1
      continue
    for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
      if r >= 0 and r < len(topology) and c >= 0 and c < len(topology[0]) and (r, c) not in visited:
        if topology[r][c] == topology[row][col] + 1:
          stack.append((r, c, visited.copy()))
  return paths

def solve(filename):
  with open(filename) as f:
    topology = []
    trailheads = []
    for index, line in enumerate(f.readlines()):
      topoLine = line.strip()
      trailheads += getTrailheads(index, topoLine)
      topology.append(list(map(int, list(topoLine))))
    ratings = [rateTrailhead(topology, trailhead) for trailhead in trailheads]
    print(f'The sum of all trailhead ratings is {sum(ratings)}')
  
if __name__ == '__main__':
  filename = sys.argv[1]
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename
  solve(filename)