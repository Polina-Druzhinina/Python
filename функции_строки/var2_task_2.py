stroka = "123456789101112131415161718192021"
n = input()
count = 22
while True:
        res = stroka.find(n)
        if res != -1:
            print(res+1)
            break
        stroka+=str(count)
        res = stroka.find(n)
        count+=1

