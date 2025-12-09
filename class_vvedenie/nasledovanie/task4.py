class Shapes:
    def __init__(self, name):
        self.name = name
    def square(self):
        pass
    def volume(self):
        pass
    def __str__(self):
        return f"{self.name}:{self.volume()}"

class Cube(Shapes):
    def __init__(self, name, a):
        super().__init__(name)
        self.a =a
    def square(self):
        return 6*self.a**2
    def volume(self):
        return self.a**3

class Sphere(Shapes):
    def __init__(self, name,r):
        super().__init__(name)
        self.r = r
    def square(self):
        return 4*3.14*self.r**2
    def volume(self):
        return (4/3)*3.14*self.r**3
    
class Cylinder(Shapes):
    def __init__(self, name, r,h):
        super().__init__(name)
        self.r = r
        self.h = h
    def square(self):
        return 2*3.14*self.r*(self.h + self.r)
    def volume(self):
        return 3.14*self.r**2*self.h
    
class Parallelepiped(Shapes):
    def __init__(self,name,a,b,c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
    def square(self):
        return 2*(self.a*self.b + self.b*self.c + self.c*self.a)
    def volume(self):
        return  self.a*self.b*self.c

class Ellipsoid(Shapes):
    def __init__(self, name, a,b,c):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c
    def square(self):
        return 4*3.14*((self.a**1.6*self.b**1.6 + self.a**1.6*self.c**1.6 + self.b**1.6*self.c**1.6)/3)**(1/1.6)
    def volume(self):
        return  (4/3)*3.14*self.a*self.b*self.c
def rez(cube,sphere,cylinder,parallelepiped,ellipsoid):
    lst = [cube,sphere,cylinder,parallelepiped,ellipsoid]
    total_volume = sum(f.volume() for f in lst)
    for f in lst:
        if (f.volume() >= total_volume-f.volume()):
            print(f)
    if not any(f.volume() >= total_volume - f.volume() for f in lst):
        print("Нет доминирующих фигур")
        
rez(cube = Cube("Куб", 7),
sphere = Sphere("Сфера", 2),
cylinder = Cylinder("Цилиндр", 2, 5),
parallelepiped = Parallelepiped("Параллелепипед", 2,3,4),
ellipsoid = Ellipsoid("Эллипсоид", 2,1.5,1))
