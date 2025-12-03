class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
    
    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"
    
    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                    self.proteins + other.proteins,
                    self.fats + other.fats,
                    self.carbohydrates + other.carbohydrates)
        return NotImplemented
    
    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                    self.proteins * n,
                    self.fats * n,
                    self.carbohydrates * n)
        return NotImplemented
    
    def __truediv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                    self.proteins / n,
                    self.fats / n,
                    self.carbohydrates / n)
        return NotImplemented
    
    def __floordiv__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                    self.proteins //n,
                    self.fats // n,
                    self.carbohydrates // n)
        return NotImplemented
    
apple = FoodInfo(0.4, 0.4, 9.8) 
banana = FoodInfo(1.5, 0.2, 21.8)
print("Яблоко:", apple)
print("Банан:", banana)
plus = apple + banana
print(plus)

um = banana * 2
print(um)

delen = apple / 2
print(delen)

delen_in = banana // 2
print(delen_in)
