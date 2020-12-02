import tkinter as tk
from UIPhotogrammes import PhotogrammesUI
from Photogramme import Photogramme

class ScrollbarPhotogrammesUI(tk.LabelFrame):
    # Comme nous ne pouvons utiliser de scrollbar directement sur une Frame avec Tkinter, nous passons par un canvas qui recouvre notre frame et auquel nous attachons la scrollbar
    # Nous ajoutons ensuite via une autre classe, la grille de thumbnails de photogrammes
    def __init__(self, fenetre, listePhotogrammes, **kwargs):
        tk.LabelFrame.__init__(self, fenetre, text="Photogrammes", padx=10, pady=10, **kwargs) 
        self.pack()
        self._monCanvas = tk.Canvas(self, height=400, width=630)            # gère par extension la taille du cadre
        self._monCadre = tk.Frame(self._monCanvas)
        self._monCadre.bind("<Configure>", self.reset_scrollregion)         # pour que la scrollbar soit actualisée en fonction des photogrammes dedans   
        self._yscrollbar = tk.Scrollbar(self, orient="vertical", command=self._monCanvas.yview)
        self._monCanvas.pack(side=tk.LEFT, fill="both", expand="yes")       
        self._yscrollbar.pack(side=tk.RIGHT, fill="y")
        self._monCanvas.configure(yscrollcommand=self._yscrollbar.set)
        self._monCanvas.create_window((0,0), window=self._monCadre, anchor="nw")
        self._monCanvas.bind('<Configure>', lambda e: self._monCanvas.configure(scrollregion = self._monCanvas.bbox('all')))
        self.pack(fill="both", expand="yes", padx=10, pady=10)
        self.thumbnailsDePhotogrammes = PhotogrammesUI(self._monCadre, listePhotogrammes)
        self.thumbnailsDePhotogrammes.pack()

    def reset_scrollregion(self, event):
        self._monCanvas.configure(scrollregion=self._monCanvas.bbox("all"))