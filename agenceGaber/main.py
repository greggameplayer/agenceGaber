import os
from tkinter import *
from agenceGaber.functions import Main


class MAINMENU:
    def __init__(self):
        self.window = Tk()
        self.window.title("agenceGaber")
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        Main()
        self.window.mainloop()
