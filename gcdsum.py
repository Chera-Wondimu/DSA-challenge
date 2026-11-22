import math
t = int(input())
for _ in range(t):
  n = int(input())
  while math.gcd(n, sum(map(int, str(n)))) == 1:
    n += 1
  print(n)