import math
y, w = map(int, input().split())
x = max(y, w)
a = 7 - x
g = math.gcd(a, 6)
print(f"{a // g}/{6 // g}")