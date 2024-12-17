import sys
from collections import defaultdict

def log(*args):
  if TEST:
    print(*args)

def rules(current):
  updated_stones = defaultdict(int)
  for stone, count in current.items():
    stoneString = str(stone)
    stoneLength = len(stoneString)
    if stone == 0:
      updated_stones[1] += count
    elif stoneLength % 2 == 0:
      first = int(stoneString[:stoneLength//2])
      last = int(stoneString[stoneLength//2:])
      updated_stones[first] += count
      updated_stones[last] += count
    else:
      updated_stones[stone * 2024] += count
  return updated_stones

def solve(filename, steps):
  with open(filename) as f:
    stones = defaultdict(int)
    for stone in map(int, f.read().split()):
      stones[stone] += 1
    for _ in range(steps):
      stones = rules(stones)
    total_stones = sum(stones.values())  
    print(f'There are {total_stones} stones')

if __name__ == '__main__':
  filename = sys.argv[1]
  steps = int(sys.argv[2]) if len(sys.argv) > 2 else 1
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename  
  solve(filename, steps)
