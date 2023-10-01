from tkinter import *
from window import Window 

root = Tk()
app = Window(root)
root.title('IPC2')
root.iconbitmap('src\dron-alternativo.ico')
root.resizable(False,False)
root.geometry('850x450')
root.config(bg='#A0A0A0')
root.mainloop()     
# 