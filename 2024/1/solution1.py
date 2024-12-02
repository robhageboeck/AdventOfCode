with open("input.txt") as f:
  l1, l2 = [], []
  for line in f.readlines():
    (a, b) = line.split()
    l1.append(a)
    l2.append(b)
  l1.sort()
  l2.sort()
  diff = [abs(int(b) - int(a)) for a, b in zip(l1, l2)]
  print(f'The total difference is {sum(diff)}')