import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import xml.etree.ElementTree as ET
import os
from Matriz import Matriz
from list_dron import listDron
from dron import Dron

l_Dron = listDron()

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
            width=150,
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
            height=500
        )
        frameB.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=TRUE,
            padx=5,
            pady=5
        )
        Btn1 = tk.Button(
            frameA,
            text='Abrir Xml',
            font=('Jetbrains mono',16),
            width=15,
            height=1,
            command=self.lector_Xml
        )
        Btn1.pack(
            side=tk.TOP,
            padx=5,
            pady=4
            )


    def lector_Xml(self):
        Doc_xml=askopenfile(title='Buscar documento',filetypes=(('archivo.xml','*.xml'),('todos los archivos','*.*')))
        if Doc_xml:
            path = Doc_xml.name
            name = os.path.basename(path)
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