import math

def summ(a,b):
    if isinstance(a,(int, float)) and isinstance(b,(int, float)):
        return a+b
    if isinstance(a,str) and isinstance(b,(int, float)):
        return a + str(b)

def summ_other(x, y):
    try:
        d = x+y
        return d
    except Exception as e:
        print("Ты дурак?")

def sin_deg(x):
    return math.sin(x)**0.5

def minus(x, y):
    return y-x

def f(*my_list): #собирается в кортеж
    print(my_list)

l = [3,4,5]
f(*l, *[4,5], *":ythfthyf")

#sebe = [int(i) for i in input().split()]
#cost = [int(i) for i in input().split()]
#print(*map(minus, sebe, cost))


#l = [34,56,23,56,78,89]
#res = map(sin_deg, l)
#res = [sin_deg(i) for i in l] #одинаковые действия
#print(*res)

#print(summ(3,4))
#print(summ("df", "rt"))
#print(summ_other("5", 2.5))
#other = summ
#print(summ.__name__) #просто имя функции


