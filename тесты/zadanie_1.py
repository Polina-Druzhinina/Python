str_1 = list(map(float, input().split()))
str_2 = list(map(float, input().split()))
print(*[i[0]-i[1] for i in zip(str_2, str_1)])
