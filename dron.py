
class Dron:

    def __init__(self, name) -> None:
        self.name = name
        # self.no = no
    
    def __str__(self) -> str:
        return f'{self.name}'