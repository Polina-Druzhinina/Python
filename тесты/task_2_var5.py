import math
n = int(input())
root = math.isqrt(n)
if root*root == n:
    print("YES")
else:
    print("NO")
