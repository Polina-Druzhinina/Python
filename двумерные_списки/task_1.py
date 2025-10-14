#l_double = [[j for j in range(5)]for i in range(6)]
#l_double = [[int(j) for j in input().split()]for i in range(6)]
#print(l_double)
#for row in l_double:
#    print(*row)
l = [1]*10
print(l)
l[3] = 12
print(l)

l2 = [[1]*10 for i in range(5)]#[[1]*10]*5
l2[1][5] = -15
print(l2)
for row in l2:
    print(*row)

