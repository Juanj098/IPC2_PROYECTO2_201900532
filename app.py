from tkinter import *
from window import Window 

root = Tk()
app = Window(root)
root.title('IPC2')
root.iconbitmap('src\dron-alternativo.ico')
root.resizable(False,False)
root.config(bg='#6e4478')
root.mainloop()     
