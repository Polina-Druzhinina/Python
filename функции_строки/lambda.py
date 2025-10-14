sebe = [int(i) for i in input().split()]
#print(sorted(sebe, key=lambda x: x//10+x%10))
print(*filter(lambda x: x < 0, sebe))
