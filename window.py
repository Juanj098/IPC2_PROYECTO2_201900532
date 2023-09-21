import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from PIL import ImageTk, Image
import xml.etree.ElementTree as ET
import os
from Matriz import Matriz
from list_dron import listDron
from dron import Dron

l_Dron = listDron()
name_Doc = None
class Window(Frame):

    
    def __init__(self,master = None) -> None:
        super().__init__(master,width=900,height=500,bg='#6e4478')
        self.master = master
        self.pack()
        self.widgetI()

    def widgetI(self):
        
        tk.Label(
            self,
            text='PROYECTO 2',
            justify=tk.CENTER,
            font=('Jetbrains mono',16),
            foreground='#ff8d03',  
            bg='#6e4478'  
                 ).pack(
                    side=tk.TOP,
                    fill=tk.BOTH,
                    expand= True,
                    padx=22,
                    pady=11
                 )
        frameA = tk.Frame(
            self,
            bg='#6e4478',
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
            bg='#e5be77',
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
            height=1
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
            height=1
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
            height=1
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
            height=1
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
            )
        BtnHelp.pack(
            side=tk.TOP,
            padx=5,
            pady=4
        )

        self.Text1 = tk.Text(
            frameB,
            font=('Jetbrains mono',10),
            width=30,
            height=15,
            bg='#e5be77',
            state=DISABLED
        )
        self.Text1.place(x=5,y=5)

        self.Btn6 =tk.Button(
            frameB,
            text='Nuevo Dron',
            font=('Jetbrains mono',16),
            width=16,
            height=1,
            state='disabled',
            command=self.new_Dron
        )
        self.Btn6.place(x=18,y=275)


    def lector_Xml(self):
        global name_Doc
        Doc_xml=askopenfile(title='Buscar documento',filetypes=(('archivo.xml','*.xml'),('todos los archivos','*.*')))
        if Doc_xml:
            path = Doc_xml.name
            name = os.path.basename(path)
            name_Doc = name
            l_Dron.Clear()
            self.tree_xml(name)
            print('<-------------->')
            l_Dron.enlist()
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
        except:
            print('Error!')

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
                    l_Dron.Actualizar_i
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


    