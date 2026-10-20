from math import*
t = int(input())
for _ in range(t):
  a, x, y = map(int, input().split())
  if abs(a-x) > abs(x -y) or abs(a-y) > abs(x-y):
    print("YES")
  else:
    print("NO")