from dron import Dron

class Nodo:
    def __init__(self,dato,indice) -> None:
        self.dato = dato
        self.indice = indice
        self.next = None

class listDron:
    def __init__(self) -> None:
        self.first = None
        self.i = 0
        self.lenght = 0
    
    def Clear(self):
        self.first = None

    def new_Dron(self,dato):
        self.i += 1
        new_nodo = Nodo(dato,0)
        if self.first is None:
            self.first = new_nodo
        else:
            aux = self.first
            prev = None
            while aux and dato.name > aux.dato.name:
                prev = aux
                aux = aux.next
            if prev:
                prev.next = new_nodo
            else:
                self.first = new_nodo
            new_nodo.next = aux
        
    def Actualizar_i(self):
        aux = self.first
        cont = 1
        while aux:
            aux.indice = cont
            cont+=1
            aux = aux.next

    def enlist(self):
        if self.first == None:
            print('lista vacia')
        else:
            aux = self.first
            while aux:
                print(f'{aux.indice}:{aux.dato.name}')
                aux=aux.next
    
    def enlistRt(self):
        list = ''
        if self.first == None:
            return None
        else:
            aux = self.first
            while aux:
                list+=(f' - {aux.indice}:{aux.dato.name}\n')
                aux=aux.next
        return list

    def Search_i(self,dron):
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                if dron == aux.dato.name:
                    return aux.indice
                aux = aux.next

    def verificarE(self,dron):
        aux = self.first
        while aux:
            if dron == aux.dato.name:
                return False
            aux = aux.next
        return True