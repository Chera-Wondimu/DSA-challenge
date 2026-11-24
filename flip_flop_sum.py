t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    ans = -10**9
    for i in range(n - 1):
        if a[i] == -1 and a[i + 1] == -1:
            ans = max(ans, s + 4)
        elif a[i] == 1 and a[i + 1] == 1:
            ans = max(ans, s - 4)
        else:
            ans = max(ans, s)
    print(ans)
