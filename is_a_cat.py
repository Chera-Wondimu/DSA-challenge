t = int(input())
for _ in range(t):
    n = int(input())
    s = input().lower()
    x = s[0]
    for c in s:
        if c != x[-1]:
            x += c
    if x == "meow":
        print("YES")
    else:
        print("NO")