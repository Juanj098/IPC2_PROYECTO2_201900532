class Nodo:

    def __init__(self,dato,i) -> None:
        self.next = None
        self.dato = dato
        self.i = i

class List_Msn:
    
    def __init__(self) -> None:
        self.first = None
        self.i = 0 
    
    def NewMenssage(self,dato):
        newNodo = Nodo(dato,self.i)
        if self.first is None:
            self.first = newNodo
        else:
            aux = self.first
            prev = None
            while aux and dato.name > aux.dato.name:
                prev = aux
                aux = aux.next
            if prev:
                prev.next = newNodo
            else:
                self.first = newNodo
            newNodo.next = aux

    def ActualizarI(self):
        cont = 0
        Aux = self.first
        while Aux:
            cont+=1
            Aux.i = cont
            Aux = Aux.next

    def enlistMsn(self):
        if self.first is None:
            return 'lista Vacia'
        else:
            aux = self.first
            while aux:
                print(f'{aux.dato.name}')
                aux = aux.next

    def clear(self):
        self.first = None

    def SearchI(self,i):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                if aux.i == i:
                    return aux.dato.name
                aux = aux.next
        return None
    
    def searchMsn(self,nombre):
        if self.first is None:
            return 'Lista Vacia'
        else:
            aux = self.first
            while aux:
                if nombre == aux.dato.name:
                    return aux.dato.sistema
                aux = aux.next
        return None