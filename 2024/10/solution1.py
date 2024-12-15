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

def scoreTrailhead(topology, startingTrailhead):
  row, col = startingTrailhead
  score = 0
  visited = set()
  stack = [(row, col)]
  while stack:
    row, col = stack.pop()
    if topology[row][col] == 9:
      score += 1
    visited.add((row, col))
    for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
      if r >= 0 and r < len(topology) and c >= 0 and c < len(topology[0]) and (r, c) not in visited:
        if topology[r][c] == topology[row][col] + 1:
          stack.append((r, c))
  return score

def solve(filename):
  with open(filename) as f:
    topology = []
    trailheads = []
    for index, line in enumerate(f.readlines()):
      topoLine = line.strip()
      trailheads += getTrailheads(index, topoLine)
      topology.append(list(map(int, list(topoLine))))
    scores = [scoreTrailhead(topology, trailhead) for trailhead in trailheads]
    log(f'There are {len(trailheads)} trailheads')
    print(f'The sum of all trailhead scores is {sum(scores)}')
  
if __name__ == '__main__':
  filename = sys.argv[1]
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename
  solve(filename)