a,b,c,d = map(int, input().split())
for x in range(1000, -1, -1):
    if (a*x**3 + b*x**2 + c*x + d) == 0:
        print(x)
