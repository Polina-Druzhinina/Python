class Negator:
    @staticmethod
    def neg(arg):
        if isinstance(arg, bool):
            return not arg
        elif isinstance(arg, (int, float)):
            return  -arg
        else:
            raise TypeError("Аргумент переданного типа не поддерживается")
    
print(Negator.neg(8))
print(Negator.neg(6.4))
print(Negator.neg(False))
Negator.neg([1,2,3])
