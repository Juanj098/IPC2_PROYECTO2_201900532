class Movimientos:
    
    def __init__(self,char,time,nameMensaje,dron,y) -> None:
        self.char = char
        self.time = time
        self.name = nameMensaje
        self.dron = dron
        self.Alt = y

class Nodo:

    def __init__(self,dato,i) -> None:
        self.next = None
        self.dato = dato
        self.i = int(i)

class List_Movimientos:

    def __init__(self) -> None:
        self.first = None
        self.len = 0

    def newMov(self,dato):
        nodo = Nodo(dato,self.len)
        if self.first is None:
            self.first = nodo
        else:
            aux = self.first
            while aux.next:
                aux = aux.next
            aux.next = nodo
        self.len+=1
    
    def enlistMov(self):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                print(f'{aux.i} -> {aux.dato.char}')
                aux = aux.next

    def clear(self):
        self.first = None

    def searchtime(self,dron,y,name):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if (dron == aux.dato.dron) and (y == aux.dato.Alt) and (name == aux.dato.name):
                    return aux.dato.time
                aux = aux.next