t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  r = s.count('R')
  b = s.count('B')
  clr = 'R'
  chera = 0
  for ch in s:
    if ch != clr:
      chera += 1
    elif ch == 'R':
      clr = 'B'
    else:
      clr = 'R'
  print(chera)
    