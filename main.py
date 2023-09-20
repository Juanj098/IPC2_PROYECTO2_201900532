from tkinter.filedialog import askopenfile
import xml.etree.ElementTree as ET
import os

from dron import Dron
from list_dron import listDron
from Matriz import Matriz

listDron = listDron()
Mtrz = Matriz()

def lector_Xml(Docx):
    try:
        tree = ET.parse(Docx)
        root = tree.getroot()
        for elm in root.findall("listaDrones"):
            for dron in elm.findall('dron'):
                new_dron = Dron(dron.text)
                listDron.new_Dron(new_dron)
        listDron.Actualizar_i()
        for sistemas in root.findall('listaSistemasDrones'):
            for sistema in sistemas.findall('sistemaDrones'):
                nombre = sistema.get('nombre')
                print(f'N:{nombre}')
                x = sistema.find('cantidadDrones').text
                y = sistema.find('alturaMaxima').text
                print(f'{x}:{y}')
                for contenido in sistema.findall('contenido'):
                    dr = contenido.find('dron').text
                    i = listDron.Search_i(dr)
                    print(f'{i} -> {dr}')
                    for alturas in contenido.findall('alturas'):
                        for altura in alturas.findall('altura'):
                            print(f'{i}:{altura.get("valor")} <-> {altura.text}')
                            Mtrz.insertElm(int(i),int(altura.get('valor')))   
                    
    except:
        print('Error!')

os.system('cls')
print('<--------------------------->')
print('a) Cargar archivo            ')
print('b) Generar archivo           ')
print('C) Gestion drones            ')
print('d) Gestion de sistemas       ')
print('e) Gestion de mensajes       ')
print('f) Ayuda                     ')
print('<--------------------------->')
print('             (x)             ')
print('<--------------------------->')
opc = input('-> ')
os.system('cls')
while opc != 'x':
    if opc == 'a':
        Doc_xml = askopenfile(title='Buscar documento',filetypes=(('archivo.xml','*.xml'),('todos los archivos','*.*')))
        if Doc_xml:
            path = Doc_xml.name
            name_xml = os.path.basename(path)
            listDron.Clear()
            lector_Xml(name_xml)
            print('<------------------>')
            listDron.enlist()
            print('<------------------>')
            print(Mtrz.reporte())
        else:
            print('error!')
    elif opc == 'b':
        pass
    elif opc == 'c':
        pass
    elif opc == 'd':
        pass
    elif opc == 'e':
        pass
    elif opc == 'f':
        pass
    print('<--------------------------->')
    print('a) Cargar archivo            ')
    print('b) Generar archivo           ')
    print('C) Gestion drones            ')
    print('d) Gestion de sistemas       ')
    print('e) Gestion de mensajes       ')
    print('f) Ayuda')
    print('<--------------------------->')
    print('             (x)             ')
    print('<--------------------------->')
    opc = input('-> ')
    os.system('cls')

