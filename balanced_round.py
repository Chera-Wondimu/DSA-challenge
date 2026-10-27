t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  a = sorted(map(int, input().split()))
  ans = 1
  chera = 1
  for i in range(1, n):
    if a[i] - a[i-1] <= k:
      ans += 1
    else:
      ans = 1
    chera = max(chera, ans)
  print(n - chera)