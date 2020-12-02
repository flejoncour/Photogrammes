import tkinter as tk
from UIScrollbarPhotogrammes import ScrollbarPhotogrammesUI
from Photogramme import Photogramme

class CadrePhotogrammesUI(tk.Frame):
    # Comme il est impossible d'utiliser pack() et grid() pour le même master, nous choisissons de mettre dans un conteneur grid notre cadre avec scrollbar 
    def __init__(self, fenetre, listePhotogrammes, **kwargs):
        tk.Frame.__init__(self, fenetre, borderwidth=0, **kwargs)
        self.grid()
        self.scrollbar = ScrollbarPhotogrammesUI(self, listePhotogrammes)
        self.scrollbar.grid()