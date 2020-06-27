import tkinter
import agenceGaber.main as agm

def menuFrame(user):
    if user.getRole == 1 :
        menuClient(user)
    else :
        menuAdministrateur() 

def menuAdministrateur(user):
    global menuAdministrateur
    menuAdministrateur = tkinter.Frame(agm.window)

def menuClient(user):
    global menuClient
    menuClient = tkinter.Frame(agm.window)


