import tkinter as tk
from PIL import ImageTk
from shutil import copyfile
from ConnexionDB import ConnexionBD
from Photogramme import Photogramme
from UIFenetrePrincipale import FenetrePrincipaleUI
from UILecteurImage import LecteurImage
from UIFenetreAjouterImage import FenetreAjouter
from UIFenetrePopUp import FenetrePopUp

class Controleur():
	def __init__(self):
		self._connexion = ConnexionBD()
		self._listePhotogrammes = []		
		self._root = tk.Tk()
		self._root.iconbitmap("..\\images\\Icon_8-512.ico") 	# si autre OS que Windows : self._root.iconbitmap("../images/Icon_8-512.ico") 
		self._root.title("Photogrammes")
		self._root.resizable(False, False)
		self._fenetrePrincipale = FenetrePrincipaleUI(self._root, self._listePhotogrammes)
		self.activerBoutonRecherche()
		self.activerRechecheParEntree()
		self.activerBoutonAjouter()
		self._fenetrePrincipale.mainloop()
	
	def activerBoutonRecherche(self):
		self._fenetrePrincipale.menu.boutonRecherche.configure(command=self.faireRecheche)

	def activerRechecheParEntree(self):
		self._fenetrePrincipale.menu.inputRecherche.bind('<Return>', self.validerRechercheParEntree)

	def validerRechercheParEntree(self, event):
		self.faireRecheche()

	def activerBoutonAjouter(self):
		self._fenetrePrincipale.menu.boutonAjouter.configure(command=self.ouvrirFenetreAjouterImage)

	def faireRecheche(self):
		mot = self._fenetrePrincipale.menu.inputRecherche.get()
		listePhotogrammes = self._connexion.selectionDansTable(mot)
		listeNouveauxLabels = self._fenetrePrincipale.photogrammes.scrollbar.thumbnailsDePhotogrammes.afficherPhotogrammes(listePhotogrammes)
		for i in range(len(listeNouveauxLabels)):
			# difficultés avec les fonctions lambda et l'espace de nommage de variable, devons declarer explicitement la variable index pour que celui-ci soit bien pris en compte
			listeNouveauxLabels[i].bind('<ButtonPress-1>', lambda e, index=i : self.actualiserInfos(listePhotogrammes[index]))
			listeNouveauxLabels[i].bind('<Double-1>', lambda e, index=i : self.ouvrirLecteur(listePhotogrammes, index))

	def actualiserInfos(self, photogramme):
		self._fenetrePrincipale.infos.labelSourceReponse.configure(text=photogramme.source)
		self._fenetrePrincipale.infos.labelAnneeReponse.configure(text=photogramme.annee)
		self._fenetrePrincipale.infos.labelRealisateurReponse.configure(text=photogramme.cineaste)
		self._fenetrePrincipale.infos.labelOperateurReponse.configure(text=photogramme.operateur)
		self._fenetrePrincipale.infos.labelActeursReponse.configure(text=photogramme.acteur1)
		self._fenetrePrincipale.infos.labelActeurs2Reponse.configure(text=photogramme.acteur2)
		self._fenetrePrincipale.infos.labelActeurs3Reponse.configure(text=photogramme.acteur3)
		self._fenetrePrincipale.infos.labelEmulsionReponse.configure(text=photogramme.emulsion)
		self._fenetrePrincipale.infos.labelFormatReponse.configure(text=photogramme.formatCadre)
		self._fenetrePrincipale.infos.labelFocaleReponse.configure(text=photogramme.focale)
		self._fenetrePrincipale.infos.labelAmbianceReponse.configure(text=(photogramme.lieux + "/" + photogramme.ambiance))
		self._fenetrePrincipale.infos.labelCommentaireReponse.configure(text=photogramme.commentaire)
		self._fenetrePrincipale.infos.labelPaysReponse.configure(text=photogramme.pays)

	def ouvrirLecteur(self, listePhotogrammes, index):
		# va ouvrir un lecteur avec l'image en grand
		lecteur = LecteurImage(listePhotogrammes, index)

	def ouvrirFenetreAjouterImage(self):
		# ouvre une fenetre pour ajouter une image à la bdd
		fenetre = FenetreAjouter(self._root)
		fenetre.boutonEnvoyer.configure(command=lambda:self.envoyerBDD(fenetre, [fenetre.labelSourceReponse.get(),\
			fenetre.labelAnneeReponse.get(),\
			fenetre.labelPaysReponse.get(),\
			fenetre.labelOperateurReponse.get(),\
			fenetre.labelRealisateurReponse.get(),\
			fenetre.labelGenreReponse.get(),\
			fenetre.labelActeurs1Reponse.get(),\
			fenetre.labelActeurs2Reponse.get(),\
			fenetre.labelActeurs3Reponse.get(),\
			fenetre.labelCouleur1Reponse.get(),\
			fenetre.labelCouleur2Reponse.get(),\
			fenetre.labelCouleur3Reponse.get(),\
			fenetre.labelValeurReponse.get(),\
			fenetre.labelAmbianceReponse.get(),\
			fenetre.labelLieuxReponse.get(),\
			fenetre.labelFormatReponse.get(),\
			fenetre.labelFocaleReponse.get(),\
			fenetre.labelEmulsionReponse.get(),\
			fenetre.labelNatureDesSourcesReponse.get(),\
			fenetre.labelContrasteReponse.get(),\
			fenetre.labelCommentaireReponse.get(),\
			fenetre.labelPathImageReponse.get()
		]))
		
	def envoyerBDD(self, fenetre, listeCaracteristiques):
		nomFichier = self._connexion.creerNomNouvelleImage()
		pathImage = listeCaracteristiques[len(listeCaracteristiques)-1]
		listeCaracteristiques[len(listeCaracteristiques)-1] = nomFichier
		copyfile(pathImage, "..\\images\\"+nomFichier)			# si autre OS que Windows : copyfile(pathImage, "../images/"+nomFichier)
		self._connexion.insertionDansTable(listeCaracteristiques)
		fenetre.destroy()
		popUp = FenetrePopUp(self._root, "Image bien ajoutée dans la base de données.")
	
if __name__=="__main__":
	app = Controleur()