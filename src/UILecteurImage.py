from tkinter import *
from PIL import ImageTk, Image
from Photogramme import Photogramme

class LecteurImage():
    def __init__(self, listePhotogrammes, index):
        self.lecteur = Toplevel()
        self._listeImages = []
        for elt in listePhotogrammes:
            self._listeImages.append(ImageTk.PhotoImage(elt.creerImageLecteur()))
        self.mon_label = Label(self.lecteur, image=self._listeImages[index])
        self.mon_label.grid(row=0, column=0, columnspan=3)   
        if index==0 and index==(len(self._listeImages)-1):
            self.boutonPrecedent = Button(self.lecteur, text="<<", state=DISABLED)
            self.boutonSuivant = Button(self.lecteur, text=">>", state=DISABLED)
        elif index==0:  
            self.boutonPrecedent = Button(self.lecteur, text="<<", state=DISABLED)
            self.boutonSuivant = Button(self.lecteur, text=">>", command=lambda: self.suivant(index+1))
        elif index==(len(self._listeImages)-1):
            self.boutonPrecedent = Button(self.lecteur, text="<<", command=lambda: self.precedent(index-1))
            self.boutonSuivant = Button(self.lecteur, text=">>", state=DISABLED)
        else:
            self.boutonPrecedent = Button(self.lecteur, text="<<", command=lambda: self.precedent(index-1))
            self.boutonSuivant = Button(self.lecteur, text=">>", command=lambda: self.suivant(index+1))
        self.boutonPrecedent.grid(row=1, column=0)
        self.boutonSuivant.grid(row=1, column=2)

    def suivant(self, imageNumero):
        self.mon_label.grid_forget()
        self.mon_label = Label(self.lecteur, image=self._listeImages[imageNumero])
        self.boutonSuivant = Button(self.lecteur, text=">>", command=lambda: self.suivant(imageNumero+1))
        self.boutonPrecedent = Button(self.lecteur, text="<<", command=lambda: self.precedent(imageNumero-1))
        if imageNumero== len(self._listeImages)-1:
            self.boutonSuivant = Button(self.lecteur, text=">>", state=DISABLED)    
        self.mon_label.grid(row=0, column=0, columnspan=3)
        self.boutonPrecedent.grid(row=1, column=0)
        self.boutonSuivant.grid(row=1, column=2)

    def precedent(self, imageNumero):
        self.mon_label.grid_forget()
        self.mon_label = Label(self.lecteur, image=self._listeImages[imageNumero])
        self.boutonSuivant = Button(self.lecteur, text=">>", command=lambda: self.suivant(imageNumero+1))
        self.boutonPrecedent = Button(self.lecteur, text="<<", command=lambda: self.precedent(imageNumero-1))
        if imageNumero == 0:
            self.boutonPrecedent = Button(self.lecteur, text="<<", state=DISABLED)    
        self.mon_label.grid(row=0, column=0, columnspan=3)
        self.boutonPrecedent.grid(row=1, column=0)
        self.boutonSuivant.grid(row=1, column=2)