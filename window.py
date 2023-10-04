import tkinter as tk
from tkinter import ttk
import subprocess
import timeit
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PIL import ImageTk, Image
from tkPDFViewer import tkPDFViewer as PDFviewer
import xml.etree.ElementTree as ET
import os
from Matriz import Matriz
from list_dron import listDron
from dron import Dron
from list_sistems import List_Sistemas
from sistemas import Sistemas_Dron
from list_Msn import List_Msn
from Mensajes import Mensaje
from Mensajes import Instruccion
from list_Instrucciones import list_Instrucciones
from sistemas import Sistema_Char
from sistChar import List_Char
from M import List_M,Messenger
from  movs import List_Movimientos,Movimientos

mtz = Matriz()
l_sist = List_Sistemas()
l_char = List_Char()
l_msn = List_Msn()
l_Dron = listDron()
l_instru = list_Instrucciones()
l_M = List_M()
l_movs = List_Movimientos()

name_Doc = None
class Window(Frame):

    
    def __init__(self,master = None) -> None:
        super().__init__(master,width=600,height=200,bg='#A0A0A0')
        self.master = master
        self.pack()
        self.widgetI()

    def widgetI(self):
        
        tk.Label(
            self,
            text='PROYECTO 2',
            justify=tk.CENTER,
            font=('Jetbrains mono',18),
            foreground='#A01028',  
            bg='#A0A0A0'  
                 ).pack(
                    side=tk.TOP,
                    fill=tk.BOTH,
                    expand= True,
                    padx=18,
                    pady=9
                 )
        frameA = tk.Frame(
            self,
            bg='#A0A0A0',
            width=10,
            height=500
        )
        frameA.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=TRUE,
            padx=5,
            pady=5 
        )
        frameB = tk.Frame(
            self,
            bg='#B08078',
            width=600,
            height=500,
        )
        frameB.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=TRUE,
            padx=5,
            pady=5
        )

        Btn0 = tk.Button(
            frameA,
            text='Inicializar',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.inicializar
        )
        Btn0.pack(side=tk.TOP,
                  padx=5,
                  pady=4)

        Btn1 = tk.Button(
            frameA,
            text='Abrir XML',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.lector_Xml
        )
        Btn1.pack(
            side=tk.TOP,
            padx=5,
            pady=4
            )
        
        Btn2 = tk.Button(
            frameA,
            text='Generar XML',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.outfileXml
        )
        Btn2.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        Btn3 = tk.Button(
            frameA,
            text='Gestion Dron',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command= self.Enlist_Drons
        )
        Btn3.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        Btn4 =tk.Button(
            frameA,
            text='Sistemas Dron',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.Gest_Sistemas
        )
        Btn4.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        Btn5 = tk.Button(
            frameA,
            text='Gestion Mensajes',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.Gest_Msn
        )
        Btn5.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        BtnHelp = tk.Button(
            frameA,
            text='Ayuda',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            command=self.visorPDF
            )
        BtnHelp.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        self.Text1 = tk.Text(
            frameB,
            font=('Jetbrains mono',12),
            width=55,
            height=15,
            bg='#B08078',
            state=DISABLED
        )
        self.Text1.place(x=25,y=10)

        self.Btn6 =tk.Button(
            frameB,
            text='Nuevo Dron',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            state='disabled',
            command=self.new_Dron
        )
        self.Btn6.place(x=190,y=311)


    def lector_Xml(self):
        global name_Doc
        Doc_xml=askopenfile(title='Buscar documento',filetypes=(('archivo.xml','*.xml'),('todos los archivos','*.*')))
        if Doc_xml:
            path = Doc_xml.name
            name = os.path.basename(path)
            name_Doc = name
            l_Dron.Clear()
            l_msn.clear()
            l_sist.clear()
            l_instru.clear()
            self.tree_xml(name)
            print('<-------------->')
        else:
            messagebox.showerror('Error','Error al leer documento!')

    def tree_xml(self,Dxml):
        try:
            os.system('cls')
            tree = ET.parse(Dxml)
            root = tree.getroot()
            for elm in root.findall('listaDrones'):
                for dron in elm.findall('dron'):
                    new_dron = Dron(dron.text)
                    l_Dron.new_Dron(new_dron)
            l_Dron.Actualizar_i()
            for elm in root.findall('listaSistemasDrones'):
                for sistemaD in elm.findall('sistemaDrones'):
                    nombreS = sistemaD.get('nombre')
                    x = sistemaD.find('cantidadDrones').text
                    y = sistemaD.find('alturaMaxima').text
                    sistem = Sistemas_Dron(nombreS,x,y)
                    l_sist.New_sistema(sistem)
                    for cont in sistemaD.findall('contenido'):
                        Sdron = cont.find('dron').text
                        iDron = l_Dron.Search_i(Sdron)
                        nChar = Sistema_Char(nombreS,x,y,iDron,'0',Sdron)
                        l_char.newChar(nChar)
                        for alts in cont.findall('alturas'):
                            for alt in alts.findall('altura'):
                                h = alt.get('valor')
                                c = alt.text
                                nChar = Sistema_Char(nombreS,x,y,iDron,h,c)
                                l_char.newChar(nChar)
            l_sist.Actualizar_i()
            for elm in root.findall('listaMensajes'):
                for mensaje in elm.findall('Mensaje'):
                    nameMsn = mensaje.get('nombre')
                    siste = mensaje.find('sistemaDrones').text
                    new_msn = Mensaje(nameMsn,siste)
                    l_msn.NewMenssage(new_msn)
                    for inss in mensaje.findall('instrucciones'):
                        no = 0
                        for ins in inss.findall('instruccion'):
                            no+=1
                            nDron = ins.get('dron')
                            alt = ins.text
                            newInstruccion = Instruccion(nameMsn,siste,alt,nDron,no)
                            l_instru.new_Instruccion(newInstruccion)
            l_msn.ActualizarI()
        except Exception as e:
            print(e)

    def Gest_dron(self):
        global name_Doc
        if name_Doc != None:
            print(name_Doc)
        else:
            messagebox.showerror('Error','Ingrese Documento xml')

    def Enlist_Drons(self):
        list = l_Dron.enlistRt()
        if list:
            txt ='Lista Dron:\n'
            txt += list
            self.Text1.configure(state='normal')
            self.Text1.delete(1.0,tk.END)
            self.Text1.insert(1.0,txt)
            self.Text1.configure(state='disabled')
            self.Btn6.configure(state='normal')
        else:
            messagebox.showerror('Error','Lista Vacia')


    def new_Dron(self):
        root2 = tk.Tk()
        root2.title('Nuevo Dron')
        root2.geometry('425x200')
        root2.resizable(False,False)
        root2.iconbitmap('src/aplicaciones-anadir.ico')
        root2.config(bg='#1a6b81')
        LabelT = tk.Label(root2,text='Nuevo Dron',justify='center',font=('Jetbrains mono',16),bg='#1a6b81')
        LabelT.pack(
            padx=5,
            pady=8
        )

        # nameD = StringVar()

        def saveDron():
            nDron = nameDron.get()
            if nDron != '':
                if l_Dron.verificarE(nDron):
                    n_Dron = Dron(nDron)
                    l_Dron.new_Dron(n_Dron)
                    l_Dron.Actualizar_i()
                    list = l_Dron.enlistRt()
                    txt = 'Lista de Drones:\n'
                    txt+=list
                    self.Text1.configure(state='normal')
                    self.Text1.delete(1.0,tk.END)
                    self.Text1.insert(1.0,txt)
                    self.Text1.configure(state='disabled')
                    root2.destroy()
                else:
                    messagebox.showinfo('Dron Existente','Elija otro Nombre')
            else:
                messagebox.showwarning('Cuidado','Ingrese nombre de Dron')

        LnameD = tk.Label(root2,text='Nombre Dron:',font=('Jetbrains mono',16),bg='#1a6b81')
        LnameD.place(x=5,y=50)
        nameDron = Entry(root2,font=('Jetbrain mono',16))
        nameDron.place(x=175,y=50)
        
        def cerrar_root2():
            root2.destroy()

        Fbotones=tk.Frame(root2,bg='#1a6b81')
        Fbotones.pack(padx=5,pady=5,side=tk.BOTTOM)
        save = tk.Button(Fbotones,text='Guardar',font=('Jetbrains mono',14),width=10,height=1,command=saveDron)
        save.pack(padx=5,pady=5,side=tk.LEFT)
        salir = tk.Button(Fbotones,text='Salir',font=('Jetbrains mono',14),width=10,height=1,command=cerrar_root2)
        salir.pack(padx=5,pady=5,side=tk.RIGHT)
        root2.mainloop()

    def Gest_Sistemas(self):
        global name_Doc
        if name_Doc != None:
            self.Text1.configure(state='normal')
            self.Text1.delete(1.0,tk.END)
            self.Text1.configure(state='disabled')
            self.Btn6.configure(state='disabled')
            grap = self.graficarSistema()
            with open('gsist.dot','w',encoding='UTF-8') as Doc:
                Doc.write(grap)
                Doc.close()
            os.system("dot -Tpng -Gdpi=70 gsist.dot -o gsist.png")
            dot_file="gsist.dot"
            output_file="gsist.png"
            subprocess.run(["dot","-Tpng","-Gdpi=70",dot_file,"-o",output_file])
            ventana = tk.Toplevel()
            ventana.iconbitmap('src\estadisticas.ico')
            ventana.title(".dot")
        
            # Carga la imagen en un widget Label
            imagen = tk.PhotoImage(file=output_file)
            label = ttk.Label(ventana, image=imagen)
            label.pack()
        
            ventana.mainloop()
        else:
            messagebox.showerror('Error','Ingrese Documento Xml')

    def graficarSistema(self):
       
        grp = '''digraph G {
    rankdir=LR
    node[shape=circle,style=filled]
    Nodo0[label="Sistema \\n de Drones"]
'''

        nodos = ''
        ramas = ''
        for i in range(0,int(l_sist.len)):
            nodo = l_sist.searchI(i+1)
            if nodo != None:
                
                nodos += f'\tNodo{i+1}[label="{nodo.name}"]\n'
                ramas += f'\tNodo0 -> Nodo{i+1}\n'

                for m in range(int(l_Dron.lenght)+1):
                    for n in range(int(nodo.yMax)+1):
                        char = l_char.charXY(m,n,nodo.name)
                        if char != None:
                            nodos += f'\tNodo{i+1}{m}{n}[label="{char}"]\n'
                            if (m > 0) and (n == 0):
                                ramas+=f'\tNodo{i+1} -> Nodo{i+1}{m}{n} -> '
                            elif (m > 0) and (n < int(nodo.yMax)):
                                ramas+=f'Nodo{i+1}{m}{n} -> '
                            elif (m > 0) and (n == int(nodo.yMax)):
                                ramas+=f'Nodo{i+1}{m}{n}\n'        
        grp+=nodos
        grp+=ramas
        grp+='\n}'
        return grp

    def Gest_Msn(self):
        listado = 'Listado Mensajes:\n'
        global name_Doc
        
        self.Text1.configure(state='normal')
        self.Text1.delete(1.0,tk.END)
        self.Text1.configure(state='disabled')
        self.Btn6.configure(state='disabled')


        if name_Doc != None:
            gSistema = tk.Tk()
            gSistema.title('Gestion de Sistema de Drones')
            gSistema.geometry('425x500')
            gSistema.resizable(False,False)
            gSistema.iconbitmap('src/locador.ico')
            gSistema.config(bg='#884088')
            Ltitle = tk.Label(gSistema,text='Gestion de sistemas',justify='center',font=('Jetbrains mono',16),bg='#884088')
            Ltitle.pack(
                padx=15,
                pady=5,
                side=tk.TOP
            )
            txt2 = tk.Text(
                gSistema,
                state=DISABLED,
                bg='#D0C8D0',
                font=('Jetbrains mono',14),
                width=35,
                height=10
                )
            txt2.place(
                x=17,
                y= 50
            )
            Sislabel = tk.Label(
                gSistema,
                text='Nombre de sistema',
                font=('Jetbrains mono',14),
                bg='#884088'
            )

            def genMrtz():
                mtz.clearM()
                os.system('cls')
                mtrz = nameM.get()
                if (mtrz != None) and (mtrz != ''):
                    searchS = l_msn.searchMsn(mtrz)
                    if searchS != None:
                        x = l_Dron.lenght
                        y = l_sist.ObtenerY(searchS)
                        if (x != None) and (y != None):
                            print(f'{x}:{y} - {searchS}')
                            for m in range(0,x+1): #x
                                for n in range(0,int(y)+1): #y
                                    ch= l_char.charXY(m,n,searchS)
                                    if (m > 0) and (n == 0) and (ch != None):
                                        mtz.insertCol(m,ch)
                                    elif (m > 0) and (n > 0) and (ch != None):
                                        mtz.insertElm(m,n,ch)
                        self.Threads(searchS,mtrz) #sistema, name mensaje ej. msg
                        datoMM = l_M.searchM(mtrz)
                        with open('matriz.dot','w',encoding='UTF-8') as Doc:
                            Doc.write(mtz.reporte())
                            Doc.close()
                        os.system("dot -Tpng -Gdpi=50 matriz.dot -o matriz.png")
                        dot_file = "matriz.dot"
                        outputM_file = "matriz.png"
                        subprocess.run(["dot","-Tpng","-Gdpi=50",dot_file,"-o",outputM_file])
                        MatDrons = tk.Toplevel()
                        MatDrons.iconbitmap('src/almuerzo-cohete.ico')
                        MatDrons.title("Mensaje")
                        daa = f'Nombre: {datoMM.nameM}, Sistema: {datoMM.sitem}, Mensaje: {datoMM.txt}, Tiempo: {datoMM.time}'
                        laberData = tk.Label(MatDrons,text=daa,font=('Jetbrains mono',10))
                        laberData.pack(padx=5,pady=5)
                        imag = tk.PhotoImage(file=outputM_file)
                        Label = ttk.Label(MatDrons,image=imag)
                        Label.pack()

                        MatDrons.mainloop()

                    else:
                        print('dato no encontrado')
                else:
                    print('Ingrese mensaje a buscar')

            Sislabel.place(x=10,y=325)
            nameM = tk.Entry(gSistema, font=('Jetbrains mono',14),width=15)
            nameM.place(x=205,y=325)
            BtonMtrz = tk.Button(gSistema,text='Generar Grafica',font=('Jetbrains Mono',16),command=genMrtz)
            BtonMtrz.place(x=100,y=375)
            state = True
            cont = 1
            while state != False:
                resp = l_msn.SearchI(cont)
                if resp != None:
                    listado+=f'-> {resp}\n'
                    state2 = True
                    n = 1
                    while state2 != False:
                        re = l_instru.searchIn(resp,n)
                        if re != None:
                            listado+=f' -{re}\n'
                            n+=1
                        else:
                            n = 1
                            state2 = False
                    cont+=1
                else:
                    state = False
            # <-------------------------------->
            txt2.configure(state='normal')
            txt2.delete(1.0,tk.END)
            txt2.insert(1.0,listado)
            txt2.configure(state='disabled')



        elif name_Doc is None:
            messagebox.showerror('Error','Ingrese Documento Xml')

    def Threads(self,sistema,msg):
        cont = 1
        mess = ''
        # time = 0
        searchI = l_instru.searchInSyM(sistema,msg,cont)
        while searchI != None:
            cont+=1
            if searchI != None:
                x = l_Dron.Search_i(searchI.Dron)
                char, time = mtz.EjecutarInst(int(x),int(searchI.Alt))
                # print(f'char -> {char}, t -> {time}')
                nmov = Movimientos(char,time,msg,searchI.Dron,searchI.Alt)
                l_movs.newMov(nmov)
                mess += char
            searchI = l_instru.searchInSyM(sistema,msg,cont)
        # print(f'Mensaje -> {mess}')
        objM = Messenger(msg,sistema,mess,"--")
        l_M.newM(objM)

    def Mtrz(self):
        global name_Doc
        if name_Doc != None:
            l_char.enlistChar()
        else:
            messagebox.showerror('Error','Ingrese Documento Xml')


    def visorPDF(self):
        visor = tk.Toplevel()
        visor.geometry("635x400")
        visor.iconbitmap('src\\archivo-pdf.ico')
        visor.resizable(False,False)
        filename = 'Propuesta.pdf'
        v1 = PDFviewer.ShowPdf()
        v2 = v1.pdf_view(
            visor,
            pdf_location=open(filename,"r"),
            height=200,
            width=110
        )
        v2.pack()

        visor.mainloop()

    def inicializar(self):
        global name_Doc
        name_Doc = None
        l_char.clear()
        mtz.clearM()
        l_Dron.Clear()
        l_movs.clear()
        l_instru.clear()
        l_msn.clear()
        l_M.clear()
        l_sist.clear()
        self.Text1.configure(state='normal')
        self.Text1.delete(1.0,tk.END)
        self.Text1.configure(state='disabled')
        self.Btn6.configure(state='disabled')


    def outfileXml(self):
        global name_Doc
        if name_Doc != None:
            ruta ='outXML.xml'
            root = ET.Element('respuesta')
            listMensaje = ET.SubElement(root,"listaMensaje")
            r = int(l_msn.len)
            for i in range(1,r+1):
                mens = l_msn.SearchI(i)
                mensaje = ET.SubElement(listMensaje,"mensaje",nombre = mens)
                sistema= l_msn.searchMsn(mens)
                sistemaD = ET.SubElement(mensaje,"sistemaDrones").text = sistema
                self.genMrtz(mens)
                t = l_M.searchM(mens)
                tiempoOp = ET.SubElement(mensaje,"tiempoOptimo").text=t.time
                mensajeRecibido = ET.SubElement(mensaje,"mensajeRecibido").text=t.txt
                instrucciones = ET.SubElement(mensaje,"instrucciones")
                cont = 1
                busque = l_instru.searchInsis(sistema,cont,mens)
                while busque != None:
                    cont+=1
                    if busque != None:
                        tiem = l_movs.searchtime(busque.Dron,busque.Alt,busque.name)
                        tiempo = ET.SubElement(instrucciones,"tiempo",valor= str(tiem))
                        acciones = ET.SubElement(tiempo,"acciones")
                        dron = ET.SubElement(acciones,"dron",nombre = busque.Dron).text = busque.Alt
                        print(f'dron: {busque.Dron}, mensaje:{busque.name}')  
                    busque = l_instru.searchInsis(sistema,cont,mens)
            
            archivo = ET.ElementTree(root)
            archivo.write(ruta)
            messagebox.showinfo('Listo!','Archivo Creado con exito')
        else:
            messagebox.showerror('Error','Ingrese Documento Xml')

    def genMrtz(self,msnfu):
        mtz.clearM()
        os.system('cls')
        mtrz = msnfu
        if (mtrz != None) and (mtrz != ''):
            searchS = l_msn.searchMsn(mtrz)
            if searchS != None:
                x = l_Dron.lenght
                y = l_sist.ObtenerY(searchS)
                if (x != None) and (y != None):
                    print(f'{x}:{y} - {searchS}')
                    for m in range(0,x+1): #x
                        for n in range(0,int(y)+1): #y
                            ch= l_char.charXY(m,n,searchS)
                            if (m > 0) and (n == 0) and (ch != None):
                                mtz.insertCol(m,ch)
                            elif (m > 0) and (n > 0) and (ch != None):
                                mtz.insertElm(m,n,ch)
                self.Threads(searchS,mtrz) #sistema, name mensaje ej. msg
            else:
                print('dato no encontrado')
        else:
            print('Ingrese mensaje a buscar')