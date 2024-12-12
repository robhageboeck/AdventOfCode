def move(orientation, startPosition, room):
  steps = []
  done = False
  if orientation == '^':
    newOrientation = '>'
    for i in range(startPosition[0]-1, -1, -1):
      if room[i][startPosition[1]] == '#':
        break
      if i == 0:
        done = True
      steps.append((i, startPosition[1]))
  elif orientation == '>':
    newOrientation = 'v'
    for i in range(startPosition[1]+1, len(room[0])):
      if room[startPosition[0]][i] == '#':
        break
      steps.append((startPosition[0], i))
      if i == len(room[0]) - 1:
        done = True
  elif orientation == 'v':
    newOrientation = '<'
    for i in range(startPosition[0]+1, len(room)):
      if room[i][startPosition[1]] == '#':
        break
      if i == len(room) - 1:
        done = True
      steps.append((i, startPosition[1]))
  elif orientation == '<':
    newOrientation = '^'
    for i in range(startPosition[1]-1, -1, -1):
      if room[startPosition[0]][i] == '#':
        break
      if i == 0:
        done = True
      steps.append((startPosition[0], i))
  return steps, newOrientation, done

def traverseRoom(room, startingPosition):
  orientation = '^'
  positions = [startingPosition]
  while True:
    stepsToAdd, orientation, done = move(orientation, positions[-1], room)
    positions += stepsToAdd
    if done:
      break
  return positions

with open('input.txt') as f:
  room = []
  startingPosition = None
  for line in [list(l.strip()) for l in f.readlines()]:
    room.append(line)
    if not startingPosition and '^' in line:
      startingPosition = (len(room) - 1, line.index('^'))
  steps = traverseRoom(room, startingPosition)
  print(f'There are {len(steps)} steps to get out of the room.')
  uniqueSteps = set(steps)
  print(f'There are {len(uniqueSteps)} unique steps to get out of the room.')