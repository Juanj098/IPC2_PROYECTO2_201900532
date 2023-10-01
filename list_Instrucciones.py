class Nodo:
    def __init__(self,dato) -> None:
        self.dato = dato
        self.next = None

class list_Instrucciones:
    def __init__(self) -> None:
        self.first = None
        self.len = 0

    def new_Instruccion(self,dato):
        nNodo = Nodo(dato)
        if self.first is None:
            self.first = nNodo
        else:
            aux = self.first
            while aux.next:
                aux = aux.next
            aux.next = nNodo
        self.len+=1

    def enlistIns(self):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                print(f'{aux.dato.no}:{aux.dato.Dron} -> {aux.dato.sistema}')
                aux = aux.next
    
    def clear(self):
        self.first = None

    def searchIn(self,name,i):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                if (name == aux.dato.name) and (i == aux.dato.no):
                    return aux.dato
                aux = aux.next
        return None
    
    def searchInSyM(self,sistema,msn,no):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                if (sistema == aux.dato.sistema) and (msn == aux.dato.name) and (no == aux.dato.no):
                    return aux.dato
                aux = aux.next
        return None    
    
