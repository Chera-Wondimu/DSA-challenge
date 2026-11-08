t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  if list(s) == sorted(s):
    print("YES")
  else:
    print("NO")
