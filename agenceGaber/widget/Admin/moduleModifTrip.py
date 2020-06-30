import tkinter
from tkinter import ttk
from tkinter import messagebox
import agenceGaber.main as agm
import agenceGaber.widget.moduleHomepage as agwmh
import agenceGaber.main as agcdb
from functools import partial
import random

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
        buttonVoyage = tkinter.Button(frameSeeAllTrips, text=f'Voyage {idx + 1}',
                                      command=lambda id=i[0]: seeMore(id), overrelief='groove', bg='grey40', fg='snow')
        buttonVoyage.pack()

    # ajouter un voyage
    plusButton = tkinter.Button(frameSeeAllTrips, command=ajoutervoyage, text='+', overrelief='groove', bg='grey40',
                                fg='snow')
    plusButton.pack()

    # return button
    returnButton = tkinter.Button(frameSeeAllTrips, command=retour, text='Retour', overrelief='groove', bg='grey40',
                                  fg='snow')
    returnButton.pack()


def ajoutervoyage():
    frameSeeAllTrips.destroy()
    ajoutervoyageFunc()


def ajoutervoyageFunc():
    # variables globales
    global frameAjouterVoyage, validationButton, returnButtonajoutervoyage, Espace2, LabelAV3
    # creation de la frame
    frameAjouterVoyage = tkinter.Frame(agm.window)
    frameAjouterVoyage.configure(bg='grey15')
    frameAjouterVoyage.pack(pady=10)
    # widget
    LabelAV1 = tkinter.Label(frameAjouterVoyage, text='Créer un voyage :', bg='grey15', fg='snow')
    LabelAV1.grid(row=0, column=0)

    Espace1 = tkinter.Label(frameAjouterVoyage, text='                         ', bg='grey15', fg='snow')
    Espace1.grid(row=2, column=0)

    LabelAV3 = tkinter.Label(frameAjouterVoyage, text='Entrez le nombre d\'Etape(s): ', bg='grey15', fg='snow')
    LabelAV3.grid(row=3, column=0)

    EntryAV1 = tkinter.Entry(frameAjouterVoyage, width=5, bg='grey40', fg='snow')
    EntryAV1.grid(row=3, column=1)

    validationButton = tkinter.Button(frameAjouterVoyage, command=partial(creationEtapes, EntryAV1), text='Valider la génération',
                                      overrelief='groove', bg='grey40', fg='snow')
    validationButton.grid(row=4, column=0)

    Espace2 = tkinter.Label(frameAjouterVoyage, text='                         ', bg='grey15', fg='snow')
    Espace2.grid(row=5, column=1)

    returnButtonajoutervoyage = tkinter.Button(frameAjouterVoyage, command=retour3, text='Retour', overrelief='groove',
                                               bg='grey40', fg='snow')
    returnButtonajoutervoyage.grid(row=6, column=0)


def creationEtapes(EntryAV1):
    listComboValuesLieu = [0 for i in range(100)]
    listComboValuesTown = [0 for i in range(100)]
    listDateArrivee = [0 for i in range(100)]
    listDateDepart= [0 for i in range(100)]
    villes = []
    for i in agm.database.allTown():
        villes.append(i[1])
    Objects = []
    Indice = 0
    validationButton.destroy()
    returnButtonajoutervoyage.destroy()
    Espace2.destroy()
    LabelAV3.destroy()
    val = EntryAV1.get()
    EntryAV1.destroy()

    voidRow= tkinter.Label(frameAjouterVoyage, text= '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg='grey15')
    voidRow.grid(column=1, row=2)
    voidRow2= tkinter.Label(frameAjouterVoyage, text= '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg='grey15')
    voidRow2.grid(column=0, row=2)
    
    frameAddContent2 = tkinter.Frame(frameAjouterVoyage, bg="grey15")
    canvas = tkinter.Canvas(frameAddContent2,bg='grey15', highlightcolor='grey15', highlightthickness=0)
    scrollbar = tkinter.Scrollbar(frameAddContent2, orient="vertical", command=canvas.yview)
    scrollable_frame = tkinter.Frame(canvas, bg= 'grey15',width=400, height = 600)

    scrollable_frame.bind(
    "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    
    idx = 0
    for Etape in range(int(val)):
        cboxCurrentValue = tkinter.StringVar()
        cboxCurrentValueLieu = tkinter.StringVar()
        CurrentDateArrivee = tkinter.StringVar()
        CurrentDateDepart = tkinter.StringVar()
        tkinter.Label(scrollable_frame, text=f'Etape n°{Indice + 1} :', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='                     ', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx += 1
        tkinter.Label(scrollable_frame, text='Nom de la ville :', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx += 1
        cboxlieu = ttk.Combobox(scrollable_frame, state="readonly", textvariable=cboxCurrentValueLieu)
        cbox = ttk.Combobox(scrollable_frame, values = villes, state="readonly", textvariable=cboxCurrentValue)
        cbox.grid(row=3 + Etape + idx, column=0)
        cbox.bind("<<ComboboxSelected>>", partial(cboxselected, cboxCurrentValue, cboxlieu, cboxCurrentValueLieu, Etape, listComboValuesTown))
        idx+=1
        tkinter.Label(scrollable_frame, text='Nom du lieu visité', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx+=1
        cboxlieu.grid(row=3 + Etape + idx, column=0)
        cboxlieu.bind("<<ComboboxSelected>>", partial(cboxselectedLieu, cboxCurrentValueLieu, Etape, listComboValuesLieu))
        idx+=1
        tkinter.Label(scrollable_frame, text='Ajouter un date d\'arrivé : (année-mois-jour)', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx+=1
        tkinter.Entry(scrollable_frame, width=30, bg='grey40', fg='snow', textvariable=CurrentDateArrivee, validate="focusout", validatecommand=partial(datearrivmodified, CurrentDateArrivee, listDateArrivee, Etape)).grid(row=3 + Etape + idx, column=0)
        idx+=1
        tkinter.Label(scrollable_frame, text='Ajouter un date de départ : (année-mois-jour)', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx+=1
        tkinter.Entry(scrollable_frame, width=30, bg='grey40', fg='snow', textvariable=CurrentDateDepart, validate="focusout", validatecommand=partial(datedepartmodified, CurrentDateDepart, listDateDepart, Etape)).grid(row=3 + Etape + idx, column=0)
        idx+=1
        tkinter.Label(scrollable_frame, text='                     ', bg='grey15', fg='snow').grid(row=3 + Etape + idx, column=0)
        idx+=1
        Indice += 1

    frameAddContent2.grid(row=1,column=1,pady=10, rowspan=2, sticky='NS')
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    boutonValider = tkinter.Button(frameAjouterVoyage, text="Valider", command=partial(cmdAddTrip, listComboValuesTown, listComboValuesLieu, listDateArrivee, listDateDepart), bg='grey40', fg='snow', width=15)
    boutonValider.grid(row=3, column=0, columnspan=3, padx=10)
    boutonRetour = tkinter.Button(frameAjouterVoyage, text='Annuler', command=retour3,bg='grey40', fg='snow', width=15)
    boutonRetour.grid(row=4, column=0, columnspan=3)


def cboxselected(cboxCurrentValue, cbox, cboxCurrentValueLieu, Etape, listComboValuesTown, eventObject):
    values = []
    for i in agm.database.getLieuxByVilleName(cboxCurrentValue.get()):
        values.append(i[2])
    cboxCurrentValueLieu.set("")
    cbox.configure(values=values)
    listComboValuesTown[Etape] = cboxCurrentValue.get()


def datedepartmodified(CurrentDateDepart, listDateDepart, Etape):
    listDateDepart[Etape] = CurrentDateDepart.get()


def datearrivmodified(CurrentDateArrivee, listDateArrivee, Etape):
    listDateArrivee[Etape] = CurrentDateArrivee.get()


def cboxselectedLieu(cboxCurrentValueLieu, Etape, listComboValuesLieu, eventObject):
    listComboValuesLieu[Etape] = cboxCurrentValueLieu.get()


def cmdAddTrip(listComboValuesTown, listComboValuesLieu, listDateArrivee, listDateDepart):
    test = messagebox.askquestion('Attention','vous sur de vouloir ajouter ce voyage ?')
    if test :
        result = [[],[],[],[]]

        for i in listComboValuesTown:
            if str(i) == "0":
                break
            result[0].append(i)
        
        for i in listComboValuesLieu:
            if str(i) == "0":
                break
            result[1].append(i)
        
        for i in listDateArrivee:
            if str(i) == "0":
                break
            result[2].append(i)
        
        for i in listDateDepart:
            if str(i) == "0":
                break
            result[3].append(i)
        

        print(result)
        frameAjouterVoyage.destroy()
        frameSeeAllTrips.destroy()
    else:
        tuple1= ()
        
        frameAjouterVoyage.destroy()
        agwmh.menuAdministrateurFunc()

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
    label8 = tkinter.Label(frameSeeMoreAboutTrip, text='Place(s) réservée(s) : {}'.format(place), bg='grey15',
                           fg='snow')
    label8.pack()
    label9 = tkinter.Label(frameSeeMoreAboutTrip, text=f'Place(s) restante(s): {str(int(info[2]) - int(place))}',
                           bg='grey15',
                           fg='snow')
    label9.pack()

    # liste des étapes
    labels = []
    for idx, detail in enumerate(agcdb.database.etapesTrip(id)):
        labels.append(tkinter.Label(frameSeeMoreAboutTrip,
                                    text=f'L\'étape {idx + 1} se déroule en {detail[0]} à {detail[2]} à {detail[1]}',
                                    bg='grey15', fg='snow'))
        labels[idx].pack()

    # retour
    returnButton = tkinter.Button(frameSeeMoreAboutTrip, command=retour2, text='Retour', overrelief='groove',
                                  bg='grey40', fg='snow')
    returnButton.pack()


def retour2():
    frameSeeAllTripsFunc()
    frameSeeMoreAboutTrip.destroy()
