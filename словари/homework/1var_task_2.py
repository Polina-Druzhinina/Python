n = int(input())
dict_N = {row[0]:row[1] for row in [input().split() for _ in range(n)]}
word = input()
for key, value in dict_N.items():
    if word in (key, value):
        print(value if word == key else key)
        break
