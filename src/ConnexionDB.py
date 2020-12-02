import mysql.connector
import tkinter as tk
from Photogramme import Photogramme
import re

class ConnexionBD():
    def __init__(self):
        try:
            self._connexionDB = mysql.connector.connect(
                host = "",
                user = "",
                passwd = "",
            )
            self.curseur = self._connexionDB.cursor()
            print("Identifiants corrects.")

            try:
                self._connexionDB = mysql.connector.connect(
                    host = "",
                    user = "",
                    passwd = "",
                    database = "photogrammes"
                )
                self.curseur = self._connexionDB.cursor()
                print("Connexion réussie.")
            except:
                self.creationDB()
                try:
                    self._connexionDB = mysql.connector.connect(
                    host = "",
                    user = "",
                    passwd = "",
                    database = "photogrammes"
                    )
                    self.curseur = self._connexionDB.cursor()
                    print("Connexion réussie.")
                except:
                    print("Problème de connexion à la base, veuillez voir le code.")

        except:
            print("Problème de connexion à la base de données, veuillez vérifier vos identifiants dans la classe ConnexionDB.")
            return        

    def creationDB(self):
        # si n'existe pas, créer la BD avec la table et la remplit avec les premières images de base
        self.curseur.execute("CREATE DATABASE photogrammes ;")
        self.curseur.execute("CREATE TABLE photogrammes.photogramme (idPhotogramme INT(4) NOT NULL PRIMARY KEY auto_increment, nom_fichier VARCHAR(255) UNIQUE, source VARCHAR(255), annee VARCHAR(4), pays VARCHAR(255), operateur VARCHAR(255), cineaste VARCHAR(255), genre VARCHAR(255), acteur1 VARCHAR(255), acteur2 VARCHAR(255), acteur3 VARCHAR(255), couleur1 VARCHAR(255), couleur2 VARCHAR(255), couleur3 VARCHAR(255), valeur VARCHAR(255), ambiance VARCHAR(255), lieux VARCHAR(255), format VARCHAR(255), focale VARCHAR(255), emulsion VARCHAR(255), natureDesSources VARCHAR(255), contraste VARCHAR(255), commentaire VARCHAR(255));")
        listeDebut = [["Adieu ma concubine", "1993", "Chine", "Gu Changwei", "Chen Kaige", "Drame", "", "", "", "Jaune", "", "", "Rapproché taille", "Soir", "Intérieur", "1.85", "Moyenne", "35mm", "?", "Fort", "", "1.png"], \
            ["Blade Runner", "1982", "Etats-unis", "Jordan Cronenweth", "Ridley Scott", "Science-fiction", "Harrison Ford", "Joe Turkel", "Sean Young", "Orange", "Marron", "", "Ensemble", "Soir", "Intérieur", "2.39", "Moyenne", "35mm", "", "Fort", "Soleil couchant", "2.png"], \
            ["Caravaggio", "1986", "Angleterre", "Gabriel Beristain", "Derek Jarman", "Biopic", "Nigel Terry", "", "", "Carnation", "Cyan", "", "Rapproché poitrine", "Jour", "Extérieur", "1.85", "Longue", "35mm", "", "Moyen", "", "3.png"], \
            ["Edvard Munch, la danse de la vie", "1974", "Norvège", "Odd Geir Sæther", "Peter Watkins", "Biopic", "Gro Fraas", "", "", "Bleu", "", "", "Gros plan", "Jour", "Intérieur", "1.37", "Longue", "35mm", "", "Fort", "", "4.png"], \
            ["In Cold Blood", "1967", "Etats-unis", "Conrad Hall", "Richard Brooks", "Policier", "Robert Blake", "Scott Wilson", "John McLiam", "Noir", "Blanc", "", "Demi-ensemble", "Nuit", "Intérieur", "2.35", "Courte", "35mm", "", "Fort", "", "5.png"], \
            ["Inland Empire", "2006", "Etats-unis", "David Lynch", "David Lynch", "Horreur", "Karolina Gruszka", "", "", "Rouge", "", "", "Gros plan", "Nuit", "Intérieur", "1.85", "Longue", "DV", "", "Low-key", "", "6.png"], \
            ["La double vie de veronique", "1991", "France-Pologne", "Slawomir Idziak", "Krzysztof Kieslowski", "Drame", "Irene Jacob", "", "", "Rouge", "Vert", "Marron", "Gros plan", "Soir", "Intérieur", "1.66", "Moyenne", "35mm", "", "Fort", "", "7.png"], \
            ["Le Conformiste", "1970", "Italie", "Vittorio Storaro", "Bernardo Bertolucci", "Drame", "", "", "", "Bleu", "Marron", "", "Large", "Soir", "Intérieur", "1.66", "Courte", "35mm", "", "Faible/Flat", "", "8.png"], \
            ["Stalker", "1979", "Russie", "Alexander Knyazhinsky", "Andrei Tarkovsky", "science fiction", "Aleksandr Kaydanovskiy", "", "", "Vert", "Noir", "Terre", "Moyen", "Jour", "Extérieur", "1.37", "Courte", "35mm", "", "Fort", "", "9.png"], \
            ["Stalker", "1979", "Russie", "Alexander Knyazhinsky", "Andrei Tarkovsky", "science fiction", "Anatoliy Solonitsyn", "", "", "Noir", "rouille", "Vert", "Moyen", "Jour", "Intérieur", "1.37", "Courte", "35mm", "", "Fort", "", "10.png"]]
        for photogramme in listeDebut:
            self.insertionDansTable(photogramme)
            self._connexionDB.commit()

    def fermerConnexion(self):
        self._connexionDB.close()

    def insertionDansTable(self, listeCaracteristiques):
        requeteInsert = "INSERT INTO photogrammes.photogramme (source, annee, pays, operateur, cineaste, genre, acteur1, acteur2, acteur3, couleur1, couleur2, couleur3, valeur, ambiance, lieux, format, focale, emulsion, natureDesSources, contraste, commentaire, nom_fichier) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        #insertion sécurisée contre l'injection sql via la méthode execute :
        self.curseur.execute(requeteInsert, listeCaracteristiques)
        self._connexionDB.commit()

    def creerNomNouvelleImage(self):
        requeteNumero = "SELECT MAX(idPhotogramme) FROM photogrammes.photogramme"
        self.curseur.execute(requeteNumero)
        resultat = str((self.curseur.fetchone()[0])+1) + ".png"
        return resultat

    def selectionDansTable(self, mot):
        resultats = []
        plusieursMotsClefs = False
        if mot != "":
            if mot.find(',') != -1:
                plusieursMotsClefs = True
                listeMots = mot.split(',')
                mot = listeMots[0]
            mot = mot.lower()
            requeteSelect = "SELECT * FROM photogrammes.photogramme WHERE source LIKE \"%" + mot + "%\" \
                OR annee LIKE \"%" + mot + "%\" \
                OR pays LIKE \"%" + mot + "%\" \
                OR operateur LIKE \"%" + mot + "%\" \
                OR cineaste LIKE \"%" + mot + "%\" \
                OR genre LIKE \"%" + mot + "%\" \
                OR acteur1 LIKE \"%" + mot + "%\" \
                OR acteur2 LIKE \"%" + mot + "%\" \
                OR acteur3 LIKE \"%" + mot + "%\" \
                OR couleur1 LIKE \"%" + mot + "%\" \
                OR couleur2 LIKE \"%" + mot + "%\" \
                OR couleur3 LIKE \"%" + mot + "%\" \
                OR valeur LIKE \"%" + mot + "%\" \
                OR ambiance LIKE \"%" + mot + "%\" \
                OR lieux LIKE \"%" + mot + "%\" \
                OR format LIKE \"%" + mot + "%\" \
                OR focale LIKE \"%" + mot + "%\" \
                OR emulsion LIKE \"%" + mot + "%\" \
                OR natureDesSources LIKE \"%" + mot + "%\" \
                OR contraste LIKE \"%" + mot + "%\" \
                OR commentaire LIKE \"%" + mot + "%\" ;"
            self.curseur.execute(requeteSelect)	  # renvoit une liste de tuples
            resultatsTuples=self.curseur.fetchall()
            for elt in resultatsTuples :
                photogramme = Photogramme(elt[1], elt[2], elt[3], elt[4], elt[5], elt[6], elt[7], elt[8], elt[9], elt[10], elt[11], elt[12], elt[13], elt[14], elt[15], elt[16], elt[17], elt[18], elt[19], elt[20], elt[21], elt[22])
                resultats.append(photogramme)
            if plusieursMotsClefs:
                # si plusieurs mots-clefs, on effectue la recherche (via le module re) dans la liste de resultats obtenus et on actualise cette liste à chaque mot
                index = 1
                resultatsLarge = resultats.copy()
                while index<len(listeMots):
                    resultats = []
                    mot = listeMots[index].strip().lower()
                    for photogramme in resultatsLarge:
                        for element in photogramme:
                            if type(element) is str:
                                if re.search(mot, element.lower()):
                                    resultats.append(photogramme)
                                    break
                    index += 1
        return resultats