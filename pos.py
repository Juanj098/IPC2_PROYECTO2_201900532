class Posiciones:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

class Nodo:
    def __init__(self,dato) -> None:
        self.next = None
        self.dato = dato

class List_Pos:
    def __init__(self) -> None:
        self.first = None
        self.len = 0

    def new_Pos(self,dato):
        node = Nodo(dato)
        if self.first is None:
            self.first = node
        else:
            aux = self.first
            while aux.next:
                aux = aux.next
            aux.next = node
        self.len+=1
    
    def delPos(self,Dato):
        if self.first.dato.x == Dato.x:
            aux = self.first.next
            self.first = aux
        else:
            aux = self.first
            while aux.next:
                if aux.next.dato.x == Dato.x:
                    aux.next = aux.next.next
                aux = aux.next
        
    def enlist(self):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                print (f'{aux.dato.x},{aux.dato.y}')
                aux = aux.next


    def SearchP(self,x,y):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if (x == aux.dato.x):
                    return aux.dato
                aux = aux.next
        return None
        