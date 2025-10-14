a, b, c, d, e = map(int, input().split())
count = 0
for x in range(0, 1000+1):
    if x != e and (a*x**3 + b*x**2 + c*x + d)/(x-e) == 0:
        count += 1
print(count)
        
