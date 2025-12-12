from abc import ABC, abstractmethod
class Main(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @abstractmethod
    def format(self):
        pass
    @abstractmethod
    def iso_format(self):
        pass
    def check(self):
        if 1<=self.month<=9:
            self.month = '0'+str(self.month)
        if 1<=self.day<=9:
            self.day = '0'+str(self.day)
    def iso_format(self):
        return f'{self.year}-{self.month}-{self.day}'

class USADate(Main):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)
        self.check()
    def format(self):
        return f'{self.month}-{self.day}-{self.year}'
    def iso_format(self):
        return super().iso_format()
class ItalianDate(Main):
    def __init__(self, year, month, day):
        super().__init__(year, month, day)
        self.check()
    def format(self):
        return f'{self.day}/{self.month}/{self.year}'
    def iso_format(self):
        return super().iso_format()

usa_date = USADate(2025, 3, 7)
print(usa_date.iso_format())
ita_date = ItalianDate(2025, 3, 7)
print(ita_date.format())