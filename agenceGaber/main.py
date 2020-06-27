import os
from tkinter import *
from agenceGaber.widget.frameConnexion import connexion

def MAINMENU(DB):

    global database
    database = DB
    global window
    window = Tk()
    window.title("agenceGaber")
    window.geometry("600x600")
    window.configure(background='grey15')
    window.resizable(False, False)
    connexion()
    window.mainloop()
