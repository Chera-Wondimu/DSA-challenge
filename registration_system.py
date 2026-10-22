t = int(input())
dict = {}
for _ in range(t):
  name = input().lower()
  if name not in dict:
    print("OK")
    dict[name] = 1
  else:
    print(name + str(dict[name]))
    dict[name] += 1
    