class NDrob:
    counter = 0 #поля самого класса
    #констурктор
    def __init__(self, num, den): #self ссылка на объект
        self.num = num #поля создаваемых объектов
        if den != 0:
            self.den = den #поля создаваемых объектов
            NDrob.counter += 1 
        else:
            raise ValueError() #искусственная генерация ошибки
        
    def setNum(self, num): #сеттер, изменить числитель если надо
        self.num = num
        
    def getNum(self): #геттер, вернуть числитель
        return self.num
    
    def __str__(self): #из объекта в строку
        return f"{self.num}/{self.den}"
    
    def sum(self, otherFrac):
        res = NDrob(1,1)
        res.num = self.num * otherFrac.num
        res.den = self.den * otherFrac.den
        return res

frac1 = NDrob(3, 4) #без self
print(frac1)

frac2 = NDrob(-1, 6)
print(frac2)

print(NDrob.counter)

frac1.setNum(11) #способ 1
print(frac1)

NDrob.setNum(frac1, 25)
print(frac1)

print(frac1)