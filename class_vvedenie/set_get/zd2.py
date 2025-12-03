class User:
    def __init__(self, name, age):
        self.__name = name
        self._age = age
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        if new_name == "" or (not new_name.isalpha()):
            raise ValueError("Некорректное имя")
        self.__name = new_name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        if 0 > new_age or new_age > 110 or (not isinstance(new_age, int)):
            raise ValueError("Некорректный возвраст")
        self._age = new_age

user1 = User("Polina", 18)
user2 = User("Clara", 25)

print(user1.name, user1.age) 
print(user2.name, user2.age) 

user1.name = "Sonya"
user1.age = 35
print(user1.name, user1.age)

try:
    user2.name = "123"
except ValueError as e:
    print(e)