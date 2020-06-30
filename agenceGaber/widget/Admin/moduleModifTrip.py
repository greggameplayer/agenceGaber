import tkinter
import agenceGaber.main as agm
import agenceGaber.widget.moduleHomepage as agwmh
import agenceGaber.main as agcdb


def frameSeeAllTripsFunc():
    # variables globales
    global frameSeeAllTrips

    # creation de la frame
    frameSeeAllTrips = tkinter.Frame(agm.window)
    frameSeeAllTrips.configure(bg='grey15')
    frameSeeAllTrips.pack(pady=10)
    # widget
    welcomeLabel = tkinter.Label(frameSeeAllTrips, text='Tous les voyages', bg='grey15', fg='snow')
    welcomeLabel.pack()
    voidLabel = tkinter.Label(frameSeeAllTrips, text='               ', bg='grey15')
    voidLabel.pack()

    # boutons voyages
    nb = agcdb.database.allTrip()
    for idx, i in enumerate(list(nb)):
        buttonVoyage = tkinter.Button(frameSeeAllTrips, text=f'Voyage {idx+1}',
                                      command=lambda id=i[0]: seeMore(id), overrelief='groove', bg='grey40', fg='snow')
        buttonVoyage.pack()


    #ajouter un voyage
    plusButton = tkinter.Button(frameSeeAllTrips, command= ajoutervoyage, text='+', overrelief='groove', bg='grey40', fg='snow')
    plusButton.pack()


    # return button
    returnButton = tkinter.Button(frameSeeAllTrips, command=retour, text='Retour', overrelief='groove', bg='grey40', fg='snow')
    returnButton.pack()


def ajoutervoyage():
    frameSeeAllTrips.destroy()
    ajoutervoyageFunc()

def ajoutervoyageFunc():
    # variables globales
    global frameAjouterVoyage
    # creation de la frame
    frameAjouterVoyage = tkinter.Frame(agm.window)
    frameAjouterVoyage.configure(bg='grey15')
    frameAjouterVoyage.pack(pady=10)
    # widget
    LabelAV1 = tkinter.Label(frameAjouterVoyage, text='Créer un voyage :', bg='grey15', fg='snow')
    LabelAV1.grid(row=1, column=0)

    Espace1 = tkinter.Label(frameAjouterVoyage, text='                         ', bg='grey15', fg='snow')
    Espace1.grid(row=2, column=0)

    LabelAV3 = tkinter.Label(frameAjouterVoyage, text='Entrez le nombre d\'Etape(s): ', bg='grey15', fg='snow')
    LabelAV3.grid(row=3, column=0)

    EntryAV1 = tkinter.Entry(frameAjouterVoyage, width=5, bg='grey40', fg='snow')
    EntryAV1.grid(row=3, column=1)

    validationButton = tkinter.Button(frameAjouterVoyage, command=creationEtapes, text='Valider la génération', overrelief='groove', bg='grey40', fg='snow')
    validationButton.grid(row=4, column=0)

    Espace2= tkinter.Label(frameAjouterVoyage, text='                         ', bg='grey15', fg='snow')
    Espace2.grid(row=5, column=1)

    returnButtonajoutervoyage = tkinter.Button(frameAjouterVoyage, command=retour3, text='Retour', overrelief='groove', bg='grey40', fg='snow')
    returnButtonajoutervoyage.grid(row=6, column=0)


    def creationEtapes():
        Labels = []
        Entries = []
        validationButton.destroy()
        returnButtonajoutervoyage.destroy()
        Espace2.destroy()
        for Indice in range(int(EntryAV1.get())):
            Labels.append(tkinter.Label(frameAjouterVoyage, text ='Etape n°'+Indice+':', bg='grey15', fg='snow'))
            Labels[int(Indice)].grid(row=4+int(Indice), comlum=0)

            Labels.append(tkinter.Label(frameAjouterVoyage, text ='... :', bg='grey15', fg='snow'))
            Labels[1+int(Indice)].grid(row=6+int(Indice), comlum=0)

            Entries.append(tkinter.Entry(frameAjouterVoyage, width=30, bg='grey40', fg='snow'))
            Entries[int(Indice)].grid(row=6+int(Indice), comlum=1)

            Labels.append(tkinter.Label(frameAjouterVoyage, text ='...', bg='grey15', fg='snow'))
            Labels[2+int(Indice)].grid(row=7+int(Indice), comlum=0)

            Entries.append(tkinter.Entry(frameAjouterVoyage, width=30, bg='grey40', fg='snow'))
            Entries[1+int(Indice)].grid(row=7+int(Indice), comlum=1)

        returnButtonajoutervoyage2 = tkinter.Button(frameAjouterVoyage, command=retour3, text='Retour', overrelief='groove', bg='grey40', fg='snow')
        returnButtonajoutervoyage2.grid(row=8+int(Indice), column=0)


def retour():
    frameSeeAllTrips.destroy()
    agwmh.menuAdministrateurFunc()

def retour3():
    frameAjouterVoyage.destroy()
    agwmh.menuAdministrateurFunc()


def seeMore(id):
    frameSeeAllTrips.destroy()
    frameSeeMoreAboutTripFunc(id)


def frameSeeMoreAboutTripFunc(id):
    # variables globales
    global frameSeeMoreAboutTrip
    # creation de la frame
    frameSeeMoreAboutTrip = tkinter.Frame(agm.window)
    frameSeeMoreAboutTrip.configure(bg='grey15')
    frameSeeMoreAboutTrip.pack(pady=10)
    # widget
    detailLabel = tkinter.Label(frameSeeMoreAboutTrip, text='Détail du voyage', bg='grey15', fg='snow')
    detailLabel.pack()

    # find informations
    info = agcdb.database.featureTrip(id)
    print(info)
    label1 = tkinter.Label(frameSeeMoreAboutTrip, text=f'Ville de départ : {info[8]}', bg='grey15', fg='snow')
    label1.pack()
    label2 = tkinter.Label(frameSeeMoreAboutTrip, text='Ville d\'arrivé : {}'.format(info[9]), bg='grey15', fg='snow')
    label2.pack()
    label3 = tkinter.Label(frameSeeMoreAboutTrip, text='Date de départ : {}'.format(info[1]), bg='grey15', fg='snow')
    label3.pack()
    label4 = tkinter.Label(frameSeeMoreAboutTrip, text='Description : {}'.format(info[5]), bg='grey15', fg='snow')
    label4.pack()
    label5 = tkinter.Label(frameSeeMoreAboutTrip, text='Nombre de places totales : {}'.format(info[2]), bg='grey15',
                           fg='snow')
    label5.pack()
    label6 = tkinter.Label(frameSeeMoreAboutTrip, text='Nombre de jours : {}'.format(info[3]), bg='grey15', fg='snow')
    label6.pack()
    label7 = tkinter.Label(frameSeeMoreAboutTrip, text=f'Prix : {info[4]} €', bg='grey15', fg='snow')
    label7.pack()

    # nombre de place restantes
    place = agcdb.database.numberPlacesLeft(id)
    label8 = tkinter.Label(frameSeeMoreAboutTrip, text='Place(s) réservée(s) : {}'.format(place), bg='grey15', fg='snow')
    label8.pack()
    label9 = tkinter.Label(frameSeeMoreAboutTrip, text=f'Place(s) restante(s): {str(int(info[2]) - int(place))}', bg='grey15',
                           fg='snow')
    label9.pack()

    # liste des étapes
    labels = []
    for idx, detail in enumerate(agcdb.database.etapesTrip(id)):
        labels.append(tkinter.Label(frameSeeMoreAboutTrip, text=f'L\'étape {idx+1} se déroule en {detail[0]} à {detail[2]} à {detail[1]}', bg='grey15',fg='snow'))
        labels[idx].pack()

    # retour
    returnButton = tkinter.Button(frameSeeMoreAboutTrip, command=retour2, text='Retour', overrelief='groove', bg='grey40', fg='snow')
    returnButton.pack()


def retour2():
    frameSeeAllTripsFunc()
    frameSeeMoreAboutTrip.destroy()
