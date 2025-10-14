a = int(input())
b = int(input())
lst = []

for i in range(a, b+1):
    if abs(i) % 3 == 0:
        lst.append(i)
print(sum(lst)/len(lst))
