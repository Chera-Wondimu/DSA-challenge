t = int(input())
for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  if a[0] == a[1] == a[2] == n:
    print(0)
  else:
    print(n - a[0])
    