import tkinter as tk


class FenetrePopUp(tk.Toplevel):
    def __init__(self, fenetre, message):
        tk.Toplevel.__init__(self, fenetre)
        self.cadre = tk.Frame(self, padx=15, pady=12)
        self._labelMessage = tk.Label(self.cadre, text=message, padx=20, pady=20, font="16")
        self._labelLigneVide = tk.Label(self.cadre)
        self._BoutonOK = tk.Button(self.cadre, text="OK", width=10, height=1, command=self.destroy)
        self.cadre.grid()
        self._labelMessage.grid()
        self._labelLigneVide.grid()
        self._BoutonOK.grid()