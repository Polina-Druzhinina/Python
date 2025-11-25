class Myclass:
    a = 2 #всеобщее поле класса

ob = Myclass()
ob.a = 23 #находится в объексте , не изменяет в классе
print(ob.a)
ob1 = Myclass()
print(ob1.a) #у объекта нет такой переменной => берет из класса
ob2 = Myclass()
Myclass.a = 45
print(ob1.a, ob2.a)

class NDrob:
    counter = 0 
    #конструктор
