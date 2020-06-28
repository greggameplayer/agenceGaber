import tkinter
import agenceGaber.main as agm
from agenceGaber.widget.frameConnexion import *

def menuFrame():
    if user.getRole == 1 :
        menuClient()
    else :
        menuAdministrateur() 

def menuAdministrateur():
    global menuAdministrateur
    menuAdministrateur = tkinter.Frame(agm.window)
    #création de la frame
    menuAdministrateur = tkinter.Frame(agm.window)
    menuAdministrateur.configure(bg='grey15')
    menuAdministrateur.pack(pady=10)
    #widgetLabel
    welcomeLabel=tkinter.Label(menuAdministrateur, text = 'Panel Administratif', bg='grey15',fg='snow')
    welcomeLabel.grid(row=0,column=0,columnspan=2,pady=10)
    voidLabel=tkinter.Label(menuAdministrateur, text ='               ', bg='grey15')
    voidLabel.grid(row = 1, column = 1)
    #Find trip
    trip1 = tkinter.Button(menuAdministrateur, text = 'Trouver un voyage',width=20,overrelief='groove',command=  ,bg='grey40',fg="snow")
    trip1.grid(row = 1, column=0)
    #find user 
    trip1 = tkinter.Button(menuAdministrateur, text = 'Trouver un client',width=20,overrelief='groove',command=  ,bg='grey40',fg="snow")
    trip1.grid(row = 2, column=0)
    #creat a new trip
    trip1 = tkinter.Button(menuAdministrateur, text = 'Ajouter un voyage',width=20,overrelief='groove',command=  ,bg='grey40',fg="snow")
    trip1.grid(row = 2, column=0)
    #voidLabel 2
    voidLabel2= tkinter.Label(menuAdministrateur,bg='grey15')
    voidLabel2.grid(row = 3)
    #disconnect
    disconnect = tkinter.Button(menuAdministrateur, text = 'Déconnexion', width=10, overrelief='groove', command=  , bg='grey40', fg="snow")
    disconnect.grid(row = 4, column = 0)
    #close app 
    closeApp = tkinter.Button(menuAdministrateur, text = 'Quitter', width=10, overrelief='groove', command=  , bg='grey40', fg="snow")
    closeApp.grid(row = 5, column = 0)




def menuClient():
    #variables
    global menuClient
    #création de la frame
    menuClient = tkinter.Frame(agm.window)
    menuClient.configure(bg='grey15')
    menuClient.pack(pady=10)
    #widgetLabel
    welcomeLabel=tkinter.Label(menuClient, text = 'Bienvenue '+user.name, bg='grey15',fg='snow')


