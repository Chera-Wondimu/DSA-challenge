t = int(input())
for _ in range(t):
  n = int(input())
  s, t = input().split()
  if sorted(s) == sorted(t):
    print("YES")
  else:
    print("NO")