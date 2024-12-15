import sys

def log(*args):
  if TEST:
    print(*args)

def rules(current):
  stones = []
  for stone in current:
    stoneString = str(stone)
    stoneLength = len(stoneString)
    if stone == 0:
      stones.append(1)
    elif stoneLength % 2 == 0:
      stones += [int(stoneString[:stoneLength//2]), int(stoneString[stoneLength//2:])]
    else:
      stones.append(stone * 2024)
  return stones

def solve(filename, steps):
  with open(filename) as f:
    stones = [int(x) for x in f.read().split()]
    for _ in range(steps):
        stones = rules(stones)
    print(f'There are {len(stones)} stones')
  
if __name__ == '__main__':
  filename = sys.argv[1]
  steps = int(sys.argv[2]) if len(sys.argv) > 2 else 1
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename
  solve(filename, steps)