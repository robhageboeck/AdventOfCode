def isMas(mas):
  return mas == 'MAS' or mas == 'SAM'

def LRMasDiagonal(matrix, x, y):
  mas = ''.join([matrix[y-1][x-1], matrix[y][x], matrix[y+1][x+1]])
  return isMas(mas)

def RLMasDiagonal(matrix, x, y):
  mas = ''.join([matrix[y+1][x-1], matrix[y][x], matrix[y-1][x+1]])
  return isMas(mas)

def countXmas(matrix, x, y):
  if LRMasDiagonal(matrix, x, y) and RLMasDiagonal(matrix, x, y):
    return 1
  return 0

with open('input.txt') as f:
    matrix = [list(line.strip()) for line in f.readlines()]
    xMax = len(matrix[0])
    yMax = len(matrix)
    XMAS_COUNT = 0
    for y in range(1, yMax-1):
      for x in range(1, yMax-1):
        if matrix[y][x] == 'A':
          XMAS_COUNT += countXmas(matrix, x, y)
    print(f'XMAS_COUNT: {XMAS_COUNT}')