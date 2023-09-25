class Mensaje():

    def __init__(self,nombre,sistema) -> None:
        self.name = nombre
        self.sistema = sistema


class Instruccion(Mensaje):

    def __init__(self, nombre, sistema, Alt,Dron,no) -> None:
        super().__init__(nombre, sistema)
        self.Dron = Dron
        self.Alt = Alt
        self.no = no

    def __str__(self) -> str:
        return f'Dron: {self.Dron}; Altura: {self.Alt}'