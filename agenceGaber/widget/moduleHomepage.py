import tkinter
import agenceGaber.main as agm
import agenceGaber.widget.frameConnexion as agconn
import agenceGaber.widget.frameConnexion as agwfc

import agenceGaber.widget.Admin.moduleFindTrip as awamft


def menuFrame():
    if agconn.user.getRole() == 0:
        menuClientFunc()
    else:
        menuAdministrateurFunc()


def menuAdministrateurFunc():
    global menuAdministrateur
    menuAdministrateur = tkinter.Frame(agm.window)
    # création de la frame
    menuAdministrateur = tkinter.Frame(agm.window)
    menuAdministrateur.configure(bg='grey15')
    menuAdministrateur.pack(pady=10)
    # widgetLabel
    welcomeLabel = tkinter.Label(menuAdministrateur, text='Panel Administratif', bg='grey15', fg='snow')
    welcomeLabel.grid(row=0, column=0, columnspan=2, pady=10)
    voidLabel = tkinter.Label(menuAdministrateur, text='               ', bg='grey15')
    voidLabel.grid(row=1, column=1)
    # Find trip
    trip1 = tkinter.Button(menuAdministrateur, text='Trouver un voyage', width=20, overrelief='groove',
                           command=toFrameSeeAllTrips, bg='grey40', fg="snow")
    trip1.grid(row=1, column=0)
    # find user
    findUser = tkinter.Button(menuAdministrateur, text='Trouver un client', width=20, overrelief='groove',
                              command=toFrameSeeAllUsers, bg='grey40', fg="snow")
    findUser.grid(row=2, column=0)
    # creat a new trip
    creatTrip = tkinter.Button(menuAdministrateur, text='Ajouter un voyage', width=20, overrelief='groove',
                               command=toFrameAddTrip, bg='grey40', fg="snow")
    creatTrip.grid(row=3, column=0)
    # update trip
    updateTrip = tkinter.Button(menuAdministrateur, text='Modifier un voyage', width=20, overrelief='groove',
                                command=toFrameModifTrip, bg='grey40', fg="snow")
    updateTrip.grid(row=4, column=0)
    # voidLabel 2
    voidLabel2 = tkinter.Label(menuAdministrateur, bg='grey15')
    voidLabel2.grid(row=5)
    # disconnect
    disconnect = tkinter.Button(menuAdministrateur, text='Déconnexion', width=10, overrelief='groove',
                                command=disconn, bg='grey40', fg="snow")
    disconnect.grid(row=6, column=0)
    # close app
    closeApp = tkinter.Button(menuAdministrateur, text='Quitter', width=10, overrelief='groove', command=quit,
                              bg='grey40', fg="snow")
    closeApp.grid(row=7, column=0)


def toFrameSeeAllTrips():
    menuAdministrateur.destroy()
    awamft.frameSeeAllTripsFunc()


def toFrameSeeAllUsers():
    menuAdministrateur.destroy()
    awamft.frameSeeAllUsersFunc()


def toFrameModifTrip():
    menuAdministrateur.destroy()
    awamft.frameSeeModifTripsFunc()


def toFrameAddTrip():
    menuAdministrateur.destroy()
    awamft.frameAddTripFunc()


def quit():
    agm.window.destroy()


def menuClientFunc():
    # variables
    global menuClient
    # création de la frame
    menuClient = tkinter.Frame(agm.window)
    menuClient.configure(bg='grey15')
    menuClient.pack(pady=10)
    # widgetLabel
    welcomeLabel = tkinter.Label(menuClient, text='Bienvenue ' + agconn.user.name, bg='grey15', fg='snow')
    welcomeLabel.grid(row=0, column=0, columnspan=2, pady=10)
    voidLabel = tkinter.Label(menuClient, text='               ', bg='grey15')
    voidLabel.grid(row=1, column=1)
    # Voir réservation
    seeReservation = tkinter.Button(menuClient, text='Voir Mes Réservations', width=50, overrelief='groove',
                                    command=toFrameSeeAllReservations, bg='grey40', fg="snow")
    seeReservation.grid(row=1, pady=1)
    # Voir les voyages
    findTrip = tkinter.Button(menuClient, text='Voir Les Voyages', width=50, overrelief='groove',
                              command=toFrameSeeAllTrips, bg='grey40', fg="snow")
    findTrip.grid(row=2, pady=1)
    # paiement en attente
    seePaiement = tkinter.Button(menuClient, text='Voir Mes Paiements', width=50, overrelief='groove',
                                 command=toFrameSeeAllPayments, bg='grey40', fg="snow")
    seePaiement.grid(row=3, pady=1)
    # disconnect
    disconnect = tkinter.Button(menuClient, text='Déconnexion', width=10, overrelief='groove',
                                command=disconn, bg='grey40', fg="snow")
    disconnect.grid(row=4, column=0)
    # close app
    closeApp = tkinter.Button(menuClient, text='Quitter', width=10, overrelief='groove', command=quit,
                              bg='grey40', fg="snow")
    closeApp.grid(row=5, column=0)


# fonction client
def toFrameSeeAllReservations():
    menuClient.destroy()
    awamft.seeAllReservations()


def toFrameSeeAllTripsUser():
    menuClient.destroy()
    awamft.SeeAllTripsUser()


def toFrameSeeAllPayments():
    menuClient.destroy()
    awamft.SeeAllPayments()


def disconn():
    # TODO: to be redone
    if agconn.user.getRole() == 1:
        menuAdministrateur.destroy()
    else:
        menuClient.destroy()
    agwfc.connexion()
