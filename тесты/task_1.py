summa = []
summa_y = 0
while True:
    n = int(input())
    summa.append(n**2)
    summa_y += n
    if summa_y == 0:
        break

print(sum(summa))
