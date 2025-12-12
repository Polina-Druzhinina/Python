from datetime import date, datetime
from functools import singledispatchmethod
class BirthInfo:
    def __init__(self, birth_date):
        self.birth_date = birth_date
        self.check(birth_date)
    @singledispatchmethod
    def check(self, arg):
        raise TypeError("Аргумент переданного типа не поддерживается")
    @check.register(date)
    def date_check(self, arg):
        self.birth_date = arg
    @check.register(str)
    def str_check(self, arg):
        self.birth_date = datetime.strptime(arg, '%Y-%m-%d').date()
    @check.register(list)
    @check.register(tuple)
    def lst_check(self, arg):
        self.birth_date = date(*arg)
    
    @property
    def age(self, ):
        today = date.today()
        years = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            years -= 1
        return years
b1 = BirthInfo(date(2007, 1, 11))
print(b1.age)