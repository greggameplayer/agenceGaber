import tkinter
import agenceGaber.main as agm
import agenceGaber.widget.moduleHomepage as agwmh
import agenceGaber.classDB.database as agcdb


def frameSeeAllTrips():
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
    nb = agcdb.allTrip()
    indiceVoyage = 1
    for i in nb:
        buttonVoyage = tkinter.Button(frameSeeAllTrips, text='Voyage' + indiceVoyage,
                                      command=lambda id=i[0]: seeMore(id), bg='grey15', fg='snow')
        buttonVoyage.pack()
        indiceVoyage += 1

    # return button
    returnButton = tkinter.Button(frameSeeAllTrips, command=retour, text='Retour', bg='grey15', fg='snow')
    returnButton.pack()


def retour():
    frameSeeAllTrips.destroy()
    agwmh.menuAdministrateur()


def seeMore(id):
    frameSeeAllTrips.destroy()
    frameSeeMoreAboutTrip(id)


def frameSeeMoreAboutTrip(id):
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
    info = agcdb.featureTrip(id)
    label1 = tkinter.Label(frameSeeAllTrips, text='Ville de départ : {}'.format(info[8]), bg='grey15', fg='snow')
    label1.pack()
    label2 = tkinter.Label(frameSeeAllTrips, text='Ville d\'arrivé : {}'.format(info[9]), bg='grey15', fg='snow')
    label2.pack()
    label3 = tkinter.Label(frameSeeAllTrips, text='Date de départ : {}'.format(info[1]), bg='grey15', fg='snow')
    label3.pack()
    label4 = tkinter.Label(frameSeeAllTrips, text='Description : {}'.format(info[5]), bg='grey15', fg='snow')
    label4.pack()
    label5 = tkinter.Label(frameSeeAllTrips, text='Nombre de places totales : {}'.format(info[2]), bg='grey15',
                           fg='snow')
    label5.pack()
    label6 = tkinter.Label(frameSeeAllTrips, text='Nombre de jours : {}'.format(info[3]), bg='grey15', fg='snow')
    label6.pack()
    label7 = tkinter.Label(frameSeeAllTrips, text='Prix : {}'.format(info[3]), bg='grey15', fg='snow')
    label7.pack()

    # nombre de place restantes
    place = agcdb.numberPlacesLeft(id)
    label8 = tkinter.Label(frameSeeAllTrips, text='Place(s) réservée(s) : {}'.format(place), bg='grey15', fg='snow')
    label8.pack()
    label9 = tkinter.Label(frameSeeAllTrips, text='Place(s) restante(s): {}'.format(info[2] - place), bg='grey15',
                           fg='snow')
    label9.pack()

    # liste des étapes
    indice = 1
    indicelabel = 10
    """for détail in agcdb.etapesTrip(id):
        label.indicelabel= tkinter.Label(frameSeeAllTrips, text = 'L\'Etapes '+indice+' se déroule en {}'.format(détail[0])' à {}'.format(détail[2])' à {}'.format(détail[1])), bg='grey15',fg='snow')
        label.indicelabel.pack()
        indice += 1
        indicelabel += 1"""

    # retour
    returnButton = tkinter.Button(frameSeeMoreAboutTrip, command=retour2, text='Retour', bg='grey15', fg='snow')
    returnButton.pack()


def retour2():
    frameSeeMoreAboutTrip.destroy()
    frameSeeAllTrips()
