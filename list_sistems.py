from sistemas import Sistemas_Dron
import os

class Nodo:

    def __init__(self, dato, indice) -> None:
        self.next = None
        self.dato = dato
        self.i = indice

class List_Sistemas:

    def __init__(self) -> None:
        self.first = None
        self.i = 0
        self.len = 0

    def clear(self):
        self.first = None
    
    def New_sistema(self,dato):
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
        self.len+=1

    def Actualizar_i(self):
        aux = self.first
        cont = 1
        while aux:
            aux.i = cont
            cont+=1
            aux = aux.next
    
    def enlist(self):
        if self.first is None:
            return f'Lista vacia'
        else:
            aux = self.first
            while aux:
                print (f'{aux.i}:{aux.dato.name}:{aux.dato.xMax}:{aux.dato.yMax}')
                aux = aux.next

    def GraficarL(self):
        cont = 0
        grp = '''digraph G {
    rankdir=TB
    node[shape=circle,color=grey]
    Nodo0[label="Sistema \n de Drones"]
'''
        node = ''
        ramas = ''
        if self.first is None:
            return 'Lista vacia'
        else:
            aux = self.first
            while aux:
                cont+=1
                node+=f'\tNodo{cont}[label="{aux.dato.name}"]\n'
                ramas+=f'\tNodo0 -> Nodo{cont}\n'
                aux = aux.next
            grp+=f'{node}\n'
            grp+=f'{ramas}\n'
            grp+='}'
        
        # with open('gsist.dot','w',encoding='UTF-8') as Doc:
        #     Doc.write(grp)
        #     Doc.close()
        # os.system("dot -Tpng gsist.dot -o gsist.png")

    def ObtenerX(self,name):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if name == aux.dato.name:
                    return aux.dato.xMax
                aux = aux.next
        return None
    
    def ObtenerY(self,name):
        if self.first is None:
            return None
        else:
            aux = self.first
            while aux:
                if name == aux.dato.name:
                    return aux.dato.yMax
                aux = aux.next
        return None
    
    def searchI(self,i):
        if self.first is None:
            return 'lISTA VACIA'
        else:
            aux = self.first
            while aux:
                if i == aux.i:
                    return aux.dato
                aux = aux.next
        return None