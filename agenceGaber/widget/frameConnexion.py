import tkinter
import agenceGaber.main as agm
from agenceGaber.widget.moduleInscription import *
from agenceGaber.classDB.User import User
import agenceGaber.widget.moduleHomepage as homepage

def connexion():
    #variable globale
    global frameConnexion, entryID, entryMP
    #Creation de la frame
    frameConnexion=tkinter.Frame(agm.window)
    frameConnexion.configure(background='grey15' )
    frameConnexion.pack(pady=10)
    #widgets
    messageAcceuil=tkinter.Label(frameConnexion,text="Bienvenue dans agenceGaber",bg='grey15',fg='snow')
    messageAcceuil.grid(row=0,column=0,columnspan=2,pady=10)
    
    labelID=tkinter.Label(frameConnexion,text='Identifiant : ',bg='grey15',fg='snow')
    labelID.grid(row=1,column=0,sticky='w')
    
    labelMP=tkinter.Label(frameConnexion,text='Mot de Passe : ',bg='grey15',fg='snow')
    labelMP.grid(row=2,column=0,sticky='w')
    
    entryID=tkinter.Entry(frameConnexion,width=20,bg='grey40',fg="snow")
    entryID.grid(row=1,column=1)
    
    entryMP=tkinter.Entry(frameConnexion,show='*',width=20,bg='grey40',fg="snow")
    entryMP.grid(row=2,column=1)
    
    btConnexion=tkinter.Button(frameConnexion,text='Connexion',width=10,overrelief='groove',command=traitement,bg='grey40',fg="snow")
    btConnexion.grid(row=3,column=0,pady=2,columnspan=2)
    
    btInscription=tkinter.Button(frameConnexion,text='Inscription',width=10,overrelief='groove',command=subscribeButton,bg='grey40',fg="snow")
    btInscription.grid(row=4,column=0,pady=2,columnspan=2)

def traitement():
    global user
    log=(entryID.get(),entryMP.get())
    if log[0] !='' and log[1] !='':
        user=User(log)
        user.findUserOnDB()
        if user.auth:
            tkinter.messagebox.showinfo('Connexion','Connexion Réussie')
            frameConnexion.destroy()
            homepage.menuFrame(user)
        else: 
            tkinter.messagebox.showinfo('Alert','Echec de la connexion, vérifiez les informations saisies')
    else :
        if not log[0]:
            tkinter.messagebox.showinfo('Alert','Veuillez saisir un email')
        else:
            tkinter.messagebox.showinfo('Alert','Veuillez saisir votre mot de passe')



def subscribeButton():
    frameConnexion.destroy()
    subcribeFrame()

    