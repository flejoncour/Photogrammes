import tkinter as tk
from PIL import ImageTk, Image
from Photogramme import Photogramme

class PhotogrammesUI(tk.Frame):
    # Grille de thumbnails de Photogrammes  
    def __init__(self, fenetre, listePhotogrammes):
        tk.Frame.__init__(self, fenetre) 
        self.grid()
        self.afficherPhotogrammes(listePhotogrammes)
    
    def afficherPhotogrammes(self, listePhotogrammes):
        ligne = 0
        colonne = 0
        self.listeImages = []
        self.listeLabels = []
        for elt in listePhotogrammes:
            thumbnail = elt.creerThumbnail()
            self.listeImages.append(ImageTk.PhotoImage(thumbnail))
            self.listeLabels.append(tk.Label(self, image=self.listeImages[len(self.listeImages)-1]))      
        for elt in self.listeLabels:
            elt.grid(row=ligne, column=colonne)          
            colonne += 1
            if colonne==3:
                ligne += 1
                colonne = 0
        return self.listeLabels