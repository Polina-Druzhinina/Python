N = int(input())
dict_1 = {row[0]: row[1:] for row in [input().split() for _ in range(N)]}
M = int(input())
lst_M = input().split()
for city in lst_M: [print(country) for country in dict_1 if city in dict_1[country]]
