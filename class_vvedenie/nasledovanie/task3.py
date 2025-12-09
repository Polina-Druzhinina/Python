class Product:
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_price(self):
        return self.__price
    def set_price(self, new_price):
        self.__name = new_price

    def get_weight(self):
        return self.__weight
    def set_weight(self, new_weight):
        self.__weight = new_weight


class Buy(Product):
    def __init__(self, name, price, weight, quantity):
        super().__init__(name, price, weight)
        self.__quantity = quantity
        self.__total_price = price * quantity
        self.__total_weight = weight * quantity
    
    def get_quantity(self):
        return self.__quantity
    
    def get_total_price(self):
        return self.__total_price

    def get_total_weight(self):
        return self.__total_weight

    def set_quantity(self, value):
        self.__quantity = value
        self.__total_price = self.get_price() * value
        self.__total_weight = self.get_weight() * value
class Check(Buy):
    def print_check(self):
        print("Товар:", self.get_name())
        print("Цена за единицу:", self.get_price())
        print("Вес единицы:", self.get_weight())
        print("Количество:", self.get_quantity())
        print("Общая стоимость:", self.get_total_price())
        print("Общий вес:", self.get_total_weight())
c = Check("Яблоки", 100, 0.2, 10)
c.print_check()