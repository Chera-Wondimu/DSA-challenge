from math import lcm
q = int(input())
for _ in range(q):
  s = input().strip()
  t = input().strip()
  chera = lcm(len(s), len(t))
  a = s*(chera // len(s))
  b = t*(chera // len(t))
  if a == b:
    print(s)
  else:
    print(-1)