a,b,c,d = map(int, input().split())

l = [[i*j for j in range(c, d+1)]for i in range(a, b+1)]
for item in l:
    print(item)
