import tkinter
from tkinter import messagebox
import datetime
import re
import agenceGaber.widget.frameConnexion as mfc
import agenceGaber.main as agm

def subcribeFrame():
    #Variable Globale 
    global subscribeFrame
    global fnEntry
    global lnEntry
    global emailEntry
    global confirmEmailEntry
    global pwEntry
    global confirmPwEntry
    global birthEntry
    #Creation de la frame inscription 
    subscribeFrame=tkinter.Frame(agm.window)
    subscribeFrame.configure(bg='grey15')
    subscribeFrame.pack(pady=10)
    
    #widget
    subLabel=tkinter.Label(subscribeFrame,text='Inscription',bg='grey15',fg='snow')
    subLabel.grid(row=0,column=0,columnspan=2,pady=10)
    
    fnLabel=tkinter.Label(subscribeFrame, text='Prénom :',bg='grey15',fg='snow')
    fnLabel.grid(row=1,column=0,sticky='w') 
    
    fnEntry=tkinter.Entry(subscribeFrame,width=30,bg='grey40',fg='snow')
    fnEntry.grid(row=1,column=1)

    lnLabel=tkinter.Label(subscribeFrame,text="Nom :",bg='grey15',fg='snow')
    lnLabel.grid(row=2,column=0,sticky='w')
    
    lnEntry=tkinter.Entry(subscribeFrame,width=30,bg='grey40',fg='snow')
    lnEntry.grid(row=2,column=1)

    emailLabel=tkinter.Label(subscribeFrame,text="Email : ",bg='grey15',fg='snow')
    emailLabel.grid(row=4,column=0,sticky='w')
    
    emailEntry=tkinter.Entry(subscribeFrame,width=30,bg='grey40',fg='snow')
    emailEntry.grid(row=4,column=1)

    confirmEmailLabel=tkinter.Label(subscribeFrame,text="Confirmer Email : ",bg='grey15',fg='snow')
    confirmEmailLabel.grid(row=5,column=0,sticky='w')
    confirmEmailEntry=tkinter.Entry(subscribeFrame,width=30,bg='grey40',fg='snow')
    confirmEmailEntry.grid(row=5,column=1)

    pwLabel=tkinter.Label(subscribeFrame,text='Mot de Passe : ',bg='grey15',fg='snow')
    pwLabel.grid(row=6,column=0,sticky='w')
    
    pwEntry=tkinter.Entry(subscribeFrame,show='*',width=30,bg='grey40',fg='snow')
    pwEntry.grid(row=6,column=1)

    confirmPwLabel=tkinter.Label(subscribeFrame,text="Confirmer Mot de Passe : ",bg='grey15',fg='snow')
    confirmPwLabel.grid(row=7,column=0,sticky='w')
    
    confirmPwEntry=tkinter.Entry(subscribeFrame,show='*',width=30,bg='grey40',fg='snow')
    confirmPwEntry.grid(row=7,column=1)

    birthLabel=tkinter.Label(subscribeFrame,text="Date de naissance (jour-mois-année)",bg='grey15',fg='snow')
    birthLabel.grid(row=9,column=0, columnspan=2)
    birthEntry=tkinter.Entry(subscribeFrame,width=30,bg='grey40',fg='snow')
    birthEntry.grid(row=10,column=0 ,columnspan=2)

    voidLabel1= tkinter.Label(subscribeFrame,bg='grey15')
    voidLabel1.grid(row=8)

    voidLabel2= tkinter.Label(subscribeFrame,bg='grey15')
    voidLabel2.grid(row=11)

    btSub=tkinter.Button(subscribeFrame,text='Confirmer',width=10,overrelief='groove',bg='grey40',fg='snow',command=subscribeFunction)
    btSub.grid(row=12,column=0,columnspan=2,pady=5)
    
    btReturn=tkinter.Button(subscribeFrame,text='Annuler',width=10,overrelief='groove',command=returnSub,bg='grey40',fg='snow')
    btReturn.grid(row=13,column=0,columnspan=2)




def returnSub():
    subscribeFrame.destroy()
    mfc.connexion()

def subscribeFunction():
    if not fnEntry.get() and not lnEntry.get() and not emailEntry.get() and not confirmEmailEntry.get() and not pwEntry.get() and not confirmPwEntry.get() and not birthEntry.get() :
        messagebox.showwarning("Attention","Veuillez remplir tous les champs")
    elif not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', emailEntry.get()):
        messagebox.showwarning("Attention",'Veuillez saisir un email valide')
    elif emailEntry.get() != confirmEmailEntry.get() :
        messagebox.showwarning("Attention","Vos adresses email ne sont pas identique")
    elif pwEntry.get() != confirmPwEntry.get() :
        messagebox.showwarning("Attention","Les mots de passe saisient ne sont pas identiques")
    else:
        try :
            universalDate = (datetime.datetime.strptime(birthEntry.get(), '%d/%m/%Y')).strftime('%Y-%m-%d')
            print(universalDate)
        except:
            messagebox.showwarning("Attention","Votre date de naissance ne respecte pas le format nécessaire\n Veuillez la saisir de nouveau")
            return
        