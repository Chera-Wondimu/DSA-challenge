t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    r = n - 1
    while l < n and a[l] == a[0]:
        l += 1
    while r >= 0 and a[r] == a[n - 1]:
        r -= 1
    if a[0] == a[n - 1]:
        print(max(0, r - l + 1))
    else:
        print(min(n - l, r + 1))

