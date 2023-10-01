class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class List_Char:
    def __init__(self) -> None:
        self.first = None
        self.len = 0

    def newChar(self,dato):
        nNodo = Nodo(dato)
        if self.first is None:
            self.first = nNodo
        else:
            aux = self.first
            while aux.next:
                aux = aux.next
            aux.next = nNodo
        self.len += 1

    def enlistChar(self):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                print(aux.dato)
                aux = aux.next

    def clear(Self):
        Self.first = None

    def charXY(self,x,y,sist):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if (int(x) == aux.dato.x) and (str(y) == aux.dato.y) and (sist == aux.dato.name):
                    return aux.dato.char
                aux = aux.next
        return None
    