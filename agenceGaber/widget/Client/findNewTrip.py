import tkinter
import agenceGaber.main as agm
import agenceGaber.widget.moduleHomepage as agwmh
import agenceGaber.main as agcdb
from tkinter import messagebox

def findNewTripFunc():
    # variables globales
    global findNewTrip

    # creation de la frame
    findNewTrip = tkinter.Frame(agm.window)
    findNewTrip.configure(bg='grey15')
    findNewTrip.pack(pady=10)
    # widget
    welcomeLabel = tkinter.Label(findNewTrip, text='Tous les voyages', bg='grey15', fg='snow')
    welcomeLabel.pack()
    voidLabel = tkinter.Label(findNewTrip, text='               ', bg='grey15')
    voidLabel.pack()

    # boutons voyages
    nb = agcdb.database.allTrip()
    for idx, i in enumerate(list(nb)):
        buttonVoyage = tkinter.Button(findNewTrip, text=f'Voyage {idx+1}',
                                      command=lambda id=i[0]: seeMore(id), overrelief='groove', bg='grey40', fg='snow')
        buttonVoyage.pack()

    # return button
    returnButton = tkinter.Button(findNewTrip, command=retour, text='Retour', overrelief='groove', bg='grey40', fg='snow')
    returnButton.pack()


    #réserver


def retour():
    findNewTrip.destroy()
    agwmh.menuClientFunc()




def seeMore(id):
    findNewTrip.destroy()
    frameSeeMoreAboutTripClientFunc(id)


def frameSeeMoreAboutTripClientFunc(id):
    # variables globales
    global frameSeeMoreAboutTripClient
    global nbReservation 
    global idTrip
    idTrip=id
    # creation de la frame
    frameSeeMoreAboutTripClient = tkinter.Frame(agm.window)
    frameSeeMoreAboutTripClient.configure(bg='grey15')
    frameSeeMoreAboutTripClient.pack(pady=10)
    # widget
    detailLabel = tkinter.Label(frameSeeMoreAboutTripClient, text='Détail du voyage', bg='grey15', fg='snow')
    detailLabel.pack()

    # find informations
    info = agcdb.database.featureTrip(id)
    label1 = tkinter.Label(frameSeeMoreAboutTripClient, text=f'Ville de départ : {info[8]}', bg='grey15', fg='snow')
    label1.pack()
    label2 = tkinter.Label(frameSeeMoreAboutTripClient, text='Ville d\'arrivé : {}'.format(info[9]), bg='grey15', fg='snow')
    label2.pack()
    label3 = tkinter.Label(frameSeeMoreAboutTripClient, text='Date de départ : {}'.format(info[1]), bg='grey15', fg='snow')
    label3.pack()
    label4 = tkinter.Label(frameSeeMoreAboutTripClient, text='Description : {}'.format(info[5]), bg='grey15', fg='snow')
    label4.pack()
    label5 = tkinter.Label(frameSeeMoreAboutTripClient, text='Nombre de places totales : {}'.format(info[2]), bg='grey15',
                           fg='snow')
    label5.pack()
    label6 = tkinter.Label(frameSeeMoreAboutTripClient, text='Nombre de jours : {}'.format(info[3]), bg='grey15', fg='snow')
    label6.pack()
    label7 = tkinter.Label(frameSeeMoreAboutTripClient, text=f'Prix : {info[4]} €', bg='grey15', fg='snow')
    label7.pack()

    # nombre de place restantes
    place = agcdb.database.numberPlacesLeft(id)
    label8 = tkinter.Label(frameSeeMoreAboutTripClient, text='Place(s) réservée(s) : {}'.format(place), bg='grey15', fg='snow')
    label8.pack()
    label9 = tkinter.Label(frameSeeMoreAboutTripClient, text=f'Place(s) restante(s): {str(int(info[2]) - int(place))}', bg='grey15',
                           fg='snow')
    label9.pack()

    # liste des étapes
    labels = []
    for idx, detail in enumerate(agcdb.database.etapesTrip(id)):
        labels.append(tkinter.Label(frameSeeMoreAboutTripClient, text=f'L\'étape {idx+1} se déroule en {detail[0]} à {detail[2]} à {detail[1]}', bg='grey15',fg='snow'))
        labels[idx].pack()

    void = tkinter.Label(frameSeeMoreAboutTripClient, bg ='grey15', fg ='snow',text = ' ')
    void.pack()
    
    #Widget Réservation : 
    reservation = tkinter.Label(frameSeeMoreAboutTripClient, bg ='grey15', fg ='snow',text = 'Réserver (indiquer le nombre de voyageurs)')
    reservation.pack()

    nbReservation = tkinter.Entry(frameSeeMoreAboutTripClient, bg ='grey15', fg ='snow')
    nbReservation.pack()

    validerBouton = tkinter.Button(frameSeeMoreAboutTripClient,bg ='grey40', fg ='snow', overrelief='groove', text= 'Valider Réservation', command = fonctionReserver)
    validerBouton.pack()
    
    # retour
    returnButton = tkinter.Button(frameSeeMoreAboutTripClient, command=retour2, text='Retour', overrelief='groove', bg='grey40', fg='snow')
    returnButton.pack()


def retour2():
    frameSeeMoreAboutTripClient.destroy()
    findNewTripFunc()

def fonctionReserver():
    if (int(agcdb.database.featureTrip(idTrip)[2]) - int(agcdb.database.numberPlacesLeft(idTrip))) >= int(nbReservation.get()):
        test = messagebox.askquestion('Valider Réservation', 'Êtes vous sur de vouloir réserver pour {} personne(s)'.format(nbReservation.get()))
        if test:
            nombre = int(nbReservation.get())
            frameSeeMoreAboutTripClient.destroy()
            ajoutMembreTrip(nombre, idTrip) 
    else: 
         alert1 = messagebox.showwarning('Attention', 'Il ne reste plus assez de place pour ce voyage')
        
def ajoutMembreTrip(nb, id):
     # variables globales
    global ajoutMembre
    # creation de la frame
    frameAjouterVoyage = tkinter.Frame(agm.window, bg="grey15")
    frameAjouterVoyage.grid(row=0,column=0)
    voidRow= tkinter.Label(frameAjouterVoyage, text= '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg='grey15')
    voidRow.grid(column=1, row=2)
    voidRow2= tkinter.Label(frameAjouterVoyage, text= '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg='grey15')
    voidRow2.grid(column=0, row=2)
    
    frameAddContent2 = tkinter.Frame(frameAjouterVoyage, bg="grey15")
    canvas = tkinter.Canvas(frameAddContent2,bg='grey15', highlightcolor='grey15', highlightthickness=0)
    scrollbar = tkinter.Scrollbar(frameAddContent2, orient="vertical", command=canvas.yview)
    scrollable_frame = tkinter.Frame(canvas, bg= 'grey15',width=500, height = 600)

    scrollable_frame.bind(
    "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)
    # widget
    AjouterMembreTripLabel1 = tkinter.Label(scrollable_frame, text='Option du Voyage', bg='grey15', fg='snow')
    AjouterMembreTripLabel1.grid(row=0, column=0)
    AjouterMembreTripLabel2 = tkinter.Label(scrollable_frame, text='                   ', bg='grey15', fg='snow')
    AjouterMembreTripLabel2.grid(row=1, column=0)
    tkinter.Button(scrollable_frame, text= 'valider', bg='grey15', fg='snow').grid(row=100, column=0)
    nbmembre = int(nb)
    idx = int(0)
    for Indice in range(nbmembre):
        tkinter.Label(scrollable_frame, text=f'Membre n°{Indice + 1} :', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='Nom: ', bg='grey15', fg='snow').grid(row=2 + idx, column=0)
        idx += 1
        tkinter.Entry(scrollable_frame, bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='Prenom: ', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Entry(scrollable_frame, bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='Email: ', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Entry(scrollable_frame, bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='Date de naissance(année-mois-jour): ', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Entry(scrollable_frame, bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='', bg='grey15', fg='snow').grid(row=2+idx, column=0)
        idx += 1

    frameAddContent2.grid(row=1,column=1,pady=10, rowspan=2, sticky='NS')
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tkinter.Button(frameAjouterVoyage, text= 'valider', bg='grey15', fg='snow', command=...).grid(row=3, column=0)