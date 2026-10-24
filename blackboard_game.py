t = int(input())
for _ in range(t):
  n = int(input())
  if (n + 4) % 4 != 0:
    print("Alice")
  else:
    print("Bob")