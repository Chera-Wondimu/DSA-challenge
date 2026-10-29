t = int(input())
for _ in range(t):
  n, x = map(int, input().split())
  a = list(map(int, input().split()))
  ans = 0
  prev = 0
  for i in a:
    ans = max(ans, i - prev)
    prev = i
  ans = max(ans, 2 * ( x - prev))
  print(ans)