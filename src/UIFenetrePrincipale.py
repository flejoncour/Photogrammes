import tkinter as tk
from UICadreMenu import MenuUI
from UICadrePhotogrammes import CadrePhotogrammesUI
from UICadreInfos import InfosUI
from Photogramme import Photogramme


class FenetrePrincipaleUI(tk.Frame):
    def __init__(self, fenetre, listePhotogrammes, **kwargs):
        tk.Frame.__init__(self, fenetre, padx=10, pady=10, **kwargs)
        self.grid()        
        self.menu = MenuUI(self)
        self.photogrammes = CadrePhotogrammesUI(self, listePhotogrammes)
        self.infos = InfosUI(self)
        self.menu.grid(row=0, column=0, columnspan=2)
        self.photogrammes.grid(row=1, column=0)
        self.infos.grid(row=1, column=1)