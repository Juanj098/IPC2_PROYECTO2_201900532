class Messenger:

    def __init__(self, nameM, sistema, txt, time) -> None:
        self.nameM = nameM
        self.sitem = sistema
        self.txt = txt
        self.time = time

    def __str__(self) -> str:
        return(f'nombre: {self.nameM},Sistema: {self.sitem},mensaje: {self.txt},tiempo: {self.time}')

class Nodo:

    def __init__(self, dato) -> None:
        self.dato = dato
        self.next = None

class List_M:

    def __init__(self) -> None:
        self.first = None
        self.len = 0

    def newM(self,dato):
        node = Nodo(dato)
        if self.first is None:
            self.first = node
        else:
            aux = self.first
            while aux.next:
                aux = aux.next
            aux.next = node
        self.len+=1

    def searchM(self, name):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if name == aux.dato.nameM:
                    return aux.dato
                aux = aux.next
        return None 
    
    def enlist(self):
        if self.first is None:
            return None
        else:
            aux =self.first
            while aux:
                print(aux.dato)
                aux = aux.next