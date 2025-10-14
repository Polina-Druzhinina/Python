import random
n, m = map(int, input().split())

table = [[random.randint(10, 150) for i in range(m)] for j in range(n)]

res = list(map(sum, table))
print(list(res).index(max(res)))
