class Person: #сделала класс, иначе у класса Son вылазит ошибка MRO
    def __init__(self, mood):
        self.mood = mood

class Father(Person):
    def __init__(self, mood="neutral"):
        super().__init__(mood)
    def greet(self):
        return "Hello"
    def be_strict(self):
        self.mood = "strict"

class Mother(Person):
    def __init__(self, mood="neutral"):
        super().__init__(mood)
    def greet(self):
        return "Hi, honey!"
    def be_kind(self):
        self.mood = "kind"

class Daughter(Mother, Father):
    def __init__(self, mood="neutral"):
        super().__init__(mood)
    def greet(self):
       return super().greet()
    def be_kind(self):
        super().be_kind()
    def be_strict(self):
        super().be_strict()

class Son(Father, Mother):
    def __init__(self, mood="neutral"):
        super().__init__(mood)
    def greet(self):
       return super().greet()
    def be_kind(self):
        super().be_kind()
    def be_strict(self):
        super().be_strict()
    
f = Father()
print( f.greet()) 
f.be_strict()
print(f.mood)  

m = Mother()
print(m.greet())  
m.be_kind()
print(m.mood)  

d = Daughter()
print(d.greet())
d.be_kind()
print(d.mood)
d.be_strict()
print(d.mood)

s = Son()
print(s.greet())  
s.be_strict()
print(s.mood) 
s.be_kind()
print(s.mood) 