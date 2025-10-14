n = int(input())
count = 0
current = 1

while count < n:
    for i in range(current):
        if count >= n:
            break
        print(current, end="")
        count += 1
    current += 1
