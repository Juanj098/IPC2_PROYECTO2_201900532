class Sistemas_Dron:

    def __init__(self, name,xMax,yMax) -> None:
        self.name = name
        self.xMax = xMax
        self.yMax = yMax

class Sistema_Char(Sistemas_Dron):

    def __init__(self, name, xMax, yMax,x,y,char) -> None:
        super().__init__(name, xMax, yMax)
        self.x = x
        self.y = y
        self.char = char

    def __str__(self) -> str:
        return f'{self.name},{self.char},{self.x}:{self.y}'
    

