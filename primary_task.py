t = int(input())
for _ in range(t):
    s = input()
    if s[:2] == "10" and len(s) >= 3 and s[2] != "0" and int(s[2:]) >= 2:
        print("YES")
    else:
        print("NO")
