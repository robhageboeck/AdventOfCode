def calcScore(a, count):
  multiplier = count.get(a, 0)
  return int(a) * multiplier

with open("input.txt") as f:
  l1 = []
  l2 = []
  count = {}
  for line in f.readlines():
    (a, b) = line.split()
    l1.append(a)
    l2.append(b)
  for a in l1:
    if count.get(a):
      pass
    else:
      count[a] = l2.count(a)
  similarityScores = [calcScore(a, count) for a in l1]
  print(f'The similarity score is {sum(similarityScores)}')