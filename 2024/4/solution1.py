def found(x, y):
  pass

def isForward(matrix, x, y):
  return ''.join(matrix[y][x:x+4]) == 'XMAS'

def isReversed(matrix, x, y):
  return ''.join(matrix[y][x-3:x+1]) == 'SAMX'

def isDown(matrix, x, y, maxY):
  if y > maxY - 4:
    return False
  return ''.join([matrix[y][x], matrix[y+1][x], matrix[y+2][x], matrix[y+3][x]]) == 'XMAS'

def isUp(matrix, x, y):
  if y < 3:
    return False
  return ''.join([matrix[y][x], matrix[y-1][x], matrix[y-2][x], matrix[y-3][x]]) == 'XMAS'

def isRightDiagonalDown(matrix, x, y, xMax, yMax):
  if x > xMax - 4 or y > yMax - 4:
    return False
  return ''.join([matrix[y][x], matrix[y+1][x+1], matrix[y+2][x+2], matrix[y+3][x+3]]) == 'XMAS'

def isRightDiagonalUp(matrix, x, y, xMax):
  if x > xMax - 4 or y < 3:
    return False
  return ''.join([matrix[y][x], matrix[y-1][x+1], matrix[y-2][x+2], matrix[y-3][x+3]]) == 'XMAS'

def isLeftDiagonalDown(matrix, x, y, xMax, yMax):
  if x < 3 or y > yMax - 4:
    return False
  return ''.join([matrix[y][x], matrix[y+1][x-1], matrix[y+2][x-2], matrix[y+3][x-3]]) == 'XMAS'

def isLeftDiagonalUp(matrix, x, y):
  if x < 3 or y < 3:
    return False
  return ''.join([matrix[y][x], matrix[y-1][x-1], matrix[y-2][x-2], matrix[y-3][x-3]]) == 'XMAS'

def countXmas(matrix, x, y, xMax, yMax):
  count = 0
  if isForward(matrix, x, y):
    found(x,y)
    count += 1
  if isReversed(matrix, x, y):
    found(x,y)
    count += 1 
  if isDown(matrix, x, y, yMax):
    found(x,y)
    count += 1
  if isUp(matrix, x, y):
    found(x,y)
    count += 1 
  if isRightDiagonalDown(matrix, x, y, xMax, yMax):
    found(x,y)
    count += 1
  if isRightDiagonalUp(matrix, x, y, xMax):
    found(x,y)
    count += 1
  if isLeftDiagonalDown(matrix, x, y, xMax, yMax):
    found(x,y)
    count += 1
  if isLeftDiagonalUp(matrix, x, y):
    found(x,y)
    count += 1
  return count

with open('input.txt') as f:
    matrix = [list(line.strip()) for line in f.readlines()]
    xMax = len(matrix[0])
    yMax = len(matrix)
    XMAS_COUNT = 0
    print(f'xMax: {xMax}, yMax: {yMax}')
    for y in range(yMax):
      for x in range(xMax):
        if matrix[y][x] == 'X':
          XMAS_COUNT += countXmas(matrix, x, y, xMax, yMax)
    print(f'XMAS_COUNT: {XMAS_COUNT}')