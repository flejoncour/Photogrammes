import mysql.connector
import re
from PIL import Image, ImageTk
# import tkinter as tk

class Photogramme():
	def __init__(self, nom_fichier, source, annee, pays, operateur, cineaste, genre, acteur1, acteur2, acteur3, couleur1, couleur2, couleur3, valeur, ambiance, lieux, formatCadre, focale, emulsion ,natureDesSources, contraste, commentaire):
		self.nom_fichier = nom_fichier
		self.source = source
		self.annee = annee
		self.pays = pays
		self.operateur = operateur
		self.cineaste = cineaste
		self.genre = genre
		self.acteur1 = acteur1
		self.acteur2 = acteur2
		self.acteur3 = acteur3
		self.couleur1 = couleur1
		self.couleur2 = couleur2
		self.couleur3 = couleur3
		self.valeur = valeur
		self.ambiance = ambiance
		self.lieux = lieux
		self.formatCadre = formatCadre
		self.focale = focale
		self.emulsion = emulsion
		self.natureDesSources = natureDesSources
		self.contraste = contraste
		self.commentaire = commentaire
		self.listeElements = [self.nom_fichier, self.source, self.annee, self.pays, self.operateur, self.cineaste, self.genre, self.acteur1, self.acteur2, self.acteur3, self.couleur1, self.couleur2, self.couleur3, self.valeur, self.ambiance, self.lieux, self.formatCadre, self.focale, self.emulsion, self.natureDesSources, self.contraste, self.commentaire]

	def __repr__(self):
		return "Fichier : " + str(self.nom_fichier)
	
	def creerThumbnail(self):
        # on veut créer des thumbnails pour l'affichage dans la grille de Labels (largeur 200px)
		image = Image.open("..\\images\\" + self.nom_fichier)		# si autre OS que Windows : image = Image.open("../images/" + self.nom_fichier)
		largeur = image.size[0]
		hauteur = image.size[1]
		hauteurReduite = (int)(((20000/largeur)*hauteur)/100)
		return image.resize((200, hauteurReduite))

	def creerImageLecteur(self):
		# on veut créer des images de taille adéquate pour pouvoir être lue dans le lecteur
		image = Image.open("..\\images\\" + self.nom_fichier)		# si autre OS que Windows : image = Image.open("../images/" + self.nom_fichier)
		largeur = image.size[0]
		hauteur = image.size[1]
		hauteurLecteur = (int)(((90000/largeur)*hauteur)/100)
		return image.resize((900, hauteurLecteur))

	def __iter__(self):
		return IteratorPhotogramme(self, self.listeElements)

class IteratorPhotogramme:
	def __init__(self, photogramme, listeElements):
		self._photogramme = photogramme
		self._liste = listeElements
		self._index = -1

	def __next__(self):
		if self._index == len(self._liste)-1:
			raise StopIteration
		self._index += 1
		return self._liste[self._index]