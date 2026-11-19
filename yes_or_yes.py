t = int(input())
for _ in range(t):
  s = input()
  y = s.count('Y')
  n = s.count('N')
  if y <= 1:
    print("YES")
  else:
    print("NO")