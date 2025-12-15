from abc import ABC,abstractmethod
class ChessPiece(ABC):
    def __init__(self, horizontal ,vertical):
        self.horizontal = horizontal
        self.vertical  = vertical
    @abstractmethod
    def can_move(self,other_h, other_v):
        pass
    @property
    def horizontal(self):
        return self._horizontal
    @horizontal.setter
    def horizontal(self, new_horizontal):
        if not('a' <= new_horizontal <= 'h'):
            raise ValueError("координата фигуры по горизонтали, представленная латинской буквой от a до h")
        else:
            self._horizontal = new_horizontal
    @property
    def vertical(self):
        return self._vertical
    @vertical.setter
    def vertical(self,new_vertical):
        if not(1<=new_vertical<=8):
            raise ValueError("координата фигуры по вертикали, представленная целым числом от 1 до 8 включительно")
        else:
            self._vertical = new_vertical
class King(ChessPiece):
    def __init__(self, horizontal ,vertical):
        super().__init__(horizontal ,vertical)
    def can_move(self, other_h, other_v):
        lst = "abcdefgh"
        dx = abs(lst.index(other_h) - lst.index(self.horizontal))
        dy = abs(other_v - self.vertical)
        return max(dx,dy) == 1



class Knight(ChessPiece):
    def __init__(self, horizontal ,vertical):
        super().__init__(horizontal ,vertical)
    
    def can_move(self, other_h, other_v):
        lst = "abcdefgh"
        dx = abs(lst.index(other_h) - lst.index(self.horizontal))
        dy = abs(other_v - self.vertical)
        return (dx == 2 and dy==1) or (dx==1 and dy==2)
lst = [King('b', 5), Knight('c', 4)]

for i in lst:
    print(i.can_move('c', 5))
    print(i.can_move('d', 2))
    print(i.can_move('e', 5))
    print(i.can_move('d', 4))
