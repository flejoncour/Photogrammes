import tkinter as tk

class MenuUI(tk.Frame):

    def __init__(self, fenetre, **kwargs):
        tk.Frame.__init__(self, fenetre, padx=10, pady=10, width=650, **kwargs) 
        self.grid()
        self._labelRecherche = tk.Label(self, text="Recherche :")
        self.inputRecherche = tk.Entry(self, width=50)
        self.boutonRecherche = tk.Button(self, text="Rechercher")
        self.boutonAjouter = tk.Button(self, text="Ajouter")
        self._labelRemplissage1 = tk.Label(self, width=2)
        self._labelRemplissage2 = tk.Label(self, width=100)        
        self._labelRecherche.grid(row=0, column=0)
        self.inputRecherche.grid(row=0, column=1)
        self._labelRemplissage1.grid(row=0, column=2)
        self.boutonRecherche.grid(row=0, column=3)
        self._labelRemplissage2.grid(row=0, column=4)
        self.boutonAjouter.grid(row=0, column=5)