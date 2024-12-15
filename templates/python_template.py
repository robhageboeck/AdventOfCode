import sys

def log(*args):
  if TEST:
    print(*args)

def solve(filename):
  with open(filename) as f:
    print(f'{f.read()}')
  
if __name__ == '__main__':
  filename = sys.argv[1]
  if not filename:
    print('No file provided')
    sys.exit(1)
  TEST = 'test' in filename
  solve(filename)