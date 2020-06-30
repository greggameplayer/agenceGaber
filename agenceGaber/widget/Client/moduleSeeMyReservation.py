import tkinter
import agenceGaber.widget.frameConnexion as agwf
import agenceGaber.main as agm
import agenceGaber.widget.moduleHomepage as agwmh
import agenceGaber.widget.frameConnexion as agconn
from tkinter import messagebox


def seeAllReservationsUser():
    global frameUserReservations
    frameUserReservations = tkinter.Frame(agm.window, bg='grey15')
    frameUserReservations.pack()
    labelacceuil = tkinter.Label(frameUserReservations, text= 'Historique de vos réservations:', bg='grey15', fg ='snow')
    labelacceuil.pack()
    voidLabel = tkinter.Label(frameUserReservations, text= '', bg='grey15', fg ='snow')
    labelacceuil.pack()
    test = agm.database.userTripSub(int(agconn.user.getId()))
    if len(test) == 0:
        historique = tkinter.Label(frameUserReservations, text= 'Pour le moment vous n\'avez effectué aucune réservation', bg='grey15', fg ='snow')
        historique.pack()
    else:
        nb=1
        container = tkinter.Frame(frameUserReservations, bg="grey15")

        canvas = tkinter.Canvas(container,bg='grey15', highlightcolor='grey15', highlightthickness=0)

        scrollbar = tkinter.Scrollbar(container, orient="vertical", command=canvas.yview)

        scrollable_frame = tkinter.Frame(canvas, bg= 'grey15',width=400, height = 600)

        scrollable_frame.bind(
        "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        for i in test :
            historique = tkinter.Label(scrollable_frame, text= f'voyage {nb} : ' , bg='grey15', fg ='snow')

            historique.pack()
            historique2 = tkinter.Label(scrollable_frame, text= f'Nombre de place réservé {i[0]} : ' , bg='grey15', fg ='snow')
            historique2.pack()
            historique3= tkinter.Label(scrollable_frame, text= f'Date de début {i[3]} : ' , bg='grey15', fg ='snow')
            historique3.pack()
            historique4= tkinter.Label(scrollable_frame, text= f'Prix total : {int(i[5])*int(i[0])} euros' , bg='grey15', fg ='snow')
            historique4.pack()
            void2 = tkinter.Label(scrollable_frame, text= ' ' , bg='grey15', fg ='snow')
            void2.pack()
            nb += 1
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    retour1= tkinter.Button(frameUserReservations, text='Retour', command=retour ,bg='grey40', fg='snow', width=15)
    retour1.pack()

def retour():
    frameUserReservations.destroy()
    agwmh.menuFrame()