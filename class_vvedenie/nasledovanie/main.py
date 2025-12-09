import random


class Transport:
    def __init__(self, max_velociti, power, type_energy):
        self.max_velociti = max_velociti
        self.power = power
        self.type_energy = type_energy
    
    def set_type_energy(self, new_type):
        self.type_energy = new_type
        
    def __str__(self):
        return f"Transport:\n\
            max_velociti={self.max_velociti}\n\
            power={self.power}\n\
            type_energy={self.type_energy}"
    
class Car(Transport): #наследуется от класса(родителя)
    def __init__(self, max_velociti, power, type_energy, volume):
        super().__init__(max_velociti, power, type_energy)
        self.volume = volume
    def __str__(self):
        s = super().__str__()
        return s + f"\n\t\t volume ={self.volume}"

car = Car(120, 100, "Gas", 70) # сработал str class Transport
print(car)
tr_list = []
for i in range(10):
    k = random.randint(1,100)
    if k >  50:
        tr_list.append(Transport(120, 200, "Gasoline"))
    else:
        tr_list.append(Car(160, 150, "Gas", 70))
for c in tr_list:
    print(c)