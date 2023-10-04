import threading
import concurrent.futures
import time
from pos import List_Pos,Posiciones

l_pos = List_Pos()
class NodoM:
    def __init__(self,x,y,posicion) -> None:
        self.up = None
        self.down = None
        self.right = None
        self.left = None
        self.posY = y
        self.posX = x
        self.pos = posicion
        self.st = False

class Matriz:
    def __init__(self) -> None:
        self.principal = NodoM(-1,-1,'raiz')

    def searchF(self,y):
        aux = self.principal
        while aux:
            if aux.posY == y:
                return aux
            aux = aux.down

    def searchC(self,x):
        aux = self.principal
        while aux:
            if aux.posX == x:
                return aux
            aux = aux.right

    def insertCol(self,pos,txt):
        new_nodo = NodoM(pos,-1,txt)
        piv = self.principal
        pivA = self.principal
        while piv.right:
            if new_nodo.posX > piv.posX:
                pivA = piv
                piv = piv.right
            else:
                new_nodo.right = piv
                new_nodo.left =pivA
                pivA.right = new_nodo
                piv.left = new_nodo
                return
        new_nodo.left = piv
        piv.right = new_nodo

    def insertFil(self,pos,txt):
        new_Nodo = NodoM(-1,pos,txt)
        piv = self.principal
        pivA = self.principal
        while piv.down:
            if new_Nodo.posY > piv.posY:
                pivA = piv
                piv = piv.down
            else:
                new_Nodo.down = piv
                new_Nodo.up = pivA
                pivA.down = new_Nodo
                piv.up = new_Nodo
                return
        new_Nodo.up = piv
        piv.down = new_Nodo
    
    def newNodo(self,x,y,txt):
        new_Nodo = NodoM(x,y,txt)
        tempx = self.principal
        tempy = self.principal
        #add column
        while tempx.right:
            if tempx.posX == new_Nodo.posX:
                break
            tempx = tempx.right
        while True:
            if tempx.posY == new_Nodo.posY:
                break
            elif tempx.down != None and tempx.down.posY > new_Nodo.posY:
                new_Nodo.down = tempx.down
                new_Nodo.up = tempx
                tempx.down = new_Nodo
                break
            elif tempx.down is None:
                new_Nodo.up = tempx
                new_Nodo.down = tempx.down
                tempx.down = new_Nodo
                break
            else:
                tempx = tempx.down
        #add row
        while tempy.down:
            if tempy.posY == new_Nodo.posY:
                break
            tempy = tempy.down
        while True:
            if tempy.posX == new_Nodo.posX:
                break
            elif tempy.right != None and tempy.right.posX > new_Nodo.posX:
                new_Nodo.right = tempy.right
                new_Nodo.left = tempy
                tempy.right = new_Nodo
            elif tempy.right is None:
                new_Nodo.left = tempy
                new_Nodo.right = tempy.right
                tempy.right = new_Nodo
            else:
                tempy = tempy.right

    def insertElm(self,x,y,txt):
        # text = f'{x},{y}'
        nFila = self.searchF(y)
        nCol = self.searchC(x)
        if (nFila  is None) and (nCol is None): #fila y columna no existen
            self.insertCol(x,f'{txt}')
            self.insertFil(y,f'{y}')
            self.newNodo(x,y,txt)
        elif (nFila is None) and (nCol != None): #fila no existe / columna si existe
            self.insertFil(y,f'{y}')
            self.newNodo(x,y,txt)
        elif (nFila != None) and (nCol is None): #fila si existe / columna no existe
            self.insertCol(x,f'{txt}')
            self.newNodo(x,y,txt)
        elif (nFila != None) and (nCol != None): # fila y columna si existen
            self.newNodo(x,y,txt)
        else:
            print('sale en vacas :c')

    def reporte(self):
        grp = 'digraph MatrizCapa{ \n node[shape=box,style = filled] \n rankdir = UD; \n {rank = min; \n'
        aux1 = self.principal
        aux2 = self.principal
        aux3 = self.principal
        if aux1 is not None:
            #creacion de nodos actuales
            while aux1:
                grp += f'nodo{int(aux1.posX)+1}{int(aux1.posY)+1}[label="{aux1.pos}", rankdir=LR, group="{int(aux1.posX)+1}"];\n'
                aux1 = aux1.right
            grp += '}\n'
            while aux2:
                aux1 = aux2
                grp += '{rank=same;\n'
                while aux1:
                    if aux1.st is False:
                        grp += f'nodo{int(aux1.posX)+1}{int(aux1.posY)+1}[label="{aux1.pos}",group="{int(aux1.posX)+1}"];\n'
                    elif aux1.st is True:
                        grp += f'nodo{int(aux1.posX)+1}{int(aux1.posY)+1}[label="{aux1.pos}",group="{int(aux1.posX)+1}",fillcolor="yellow"];\n'
                    aux1 = aux1.right
                grp += '}\n'
                aux2 = aux2.down
            #conexiones entre nodos
            aux2 = aux3
            while aux2:
                aux1 = aux2
                while aux1.right:
                    grp += f'nodo{int(aux1.posX)+1}{int(aux1.posY)+1} -> nodo{int(aux1.right.posX)+1}{int(aux1.right.posY)+1} [dir = both]; \n'
                    aux1 = aux1.right
                aux2 = aux2.down
            aux2 = aux3
            while aux2:
                aux1 = aux2
                while aux1.down:
                    grp += f'nodo{int(aux1.posX)+1}{int(aux1.posY)+1} -> nodo{int(aux1.down.posX)+1}{int(aux1.down.posY)+1} [dir = both]; \n'
                    aux1 = aux1.down
                aux2 = aux2.right
            grp += '}'
        else:
            grp += 'Sin elementos en matriz'
        return grp

    def clearM(self):
        self.principal.down = None
        self.principal.left = None
        self.principal.right = None
        self.principal.up = None


    def recorrerXY(self,x,y):
        tempX = self.principal
        t = 1
        while tempX:
            if tempX.posX == x:
                tempY = tempX
                while tempY:
                    if tempY.posY == y:
                        tempY.st = True
                        return tempY,t
                    t+=1
                    tempY = tempY.down
            tempX = tempX.right 

    # EjecutarInst -> recibe pos x,y, verifica si la posicion existe en la lista si retorna el dato eso quiere decir que ya se tiene 
    # registro de un dato en esa columna y retorna la posicion del dato anterior ingresado, si la nueva posicion es mayor a la anterior 
    # el dron sube y si es menor el dron baja a la posicion; si retorna none busca el dato desde cero y agrega la posicion a la lista
    # requerida desde la posicion pasada
    def EjecutarInst(self,x,y):
        # print(f'x -> {type(x)}: y -> {type(y)}')
        posA = l_pos.SearchP(str(x),str(y))
        if posA is None: #no hay registro de anterior
            pos = Posiciones(x,y)
            l_pos.new_Pos(pos)
            m,t = self.recorrerXY(x,y)
            return m.pos,t
        else: #hay registro de anterior
            posDron,p = self.recorrerXY(x,y)
            t = 1
            if int(posA.y) > y: # el dron baja
                dif = int(posA.y) - int(y)
                cont = 0
                aux = posDron
                while (cont < dif) and aux:
                    if aux.up:
                        aux = aux.up
                        t+=1
                        cont+=1
                    else:
                        break

                l_pos.delPos(posA)
                nPos = Posiciones(x,y)
                l_pos.new_Pos(nPos)

                if y == int(aux.posY):
                    return aux.pos,t
                else:
                    return None
                
            elif int(posA).y < y: # el dron sube
                dif = int(y) - int(posA.y)
                cont = 0
                aux = posDron
                while aux and (cont < dif):
                    if aux.down:
                        aux = aux.down
                        t+=1
                        cont+=1
                    else:
                        break
                l_pos.delPos(posA)
                nPos = Posiciones(x,y)
                l_pos.new_Pos(nPos)

                if y == int(aux.posY):
                    return aux.pos,t
                else:
                    return None

            elif int(posA.y) == y: # el dron se mantiene en esa altura
                return posDron.pos,0
            else:
                return None  

            
            
# matt = Matriz()

# matt.insertElm(1,1,'a')
# matt.insertElm(1,2,'z')
# matt.insertElm(2,1,'r')
# matt.insertElm(2,2,'j')
# l_pos.enlist()
# print('-----------------')
# z = matt.EjecutarInst(2,2)
# l_pos.enlist()
# print('-----------------')
# z = matt.EjecutarInst(2,1)
# l_pos.enlist()
# print('------------')
# print(z)

