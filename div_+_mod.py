t = int(input())
for _ in range(t):
  l, r, a = map(int, input().split())
  ans = r//a + r%a
  x = (r//a)*a-1
  if x >= l:
    ans = max(ans, x//a + x%a)
  print(ans)