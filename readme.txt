Photogrammes :

Application destinée aux chefs opérateur, photographes, réalisateurs voir dessinateurs, peintres ou chacun travaillant avec l'image.
Propose de créer une base de données composée de photogrammes issus de films/créations personnelles. Ceux-ci sont référencés via leurs caractéristiques (voir liste ci-dessous) et apparaissent à l'écran via un système de recherche par mot(s)-clé(s).
L'intéret est de pouvoir accéder rapidement à des références visuelles choisies selon l'inspiration que nous souhaitons trouver pour composer (par exemple taper "bleu" pour avoir des références de plans où la couleur apparait, ceci étant possible avec chacun des paramètres cités ci-dessous). A chacun ensuite de composer sa base de données d'images qui l'auront marqué !

Possible de taper plusieurs mots-clés dans la barre de recherche pour plus de précision : il faudra séparer ces mots-clés par des virgules.
Un clic sur l'image dans le cadre "Photogrammes" fera apparaitre ses caractéristiques dans le cadre "Infos" sur le côté droit.
Un double-clic sur l'image ouvrira un lecteur dans une nouvelle fenêtre permettant d'observer celle-ci en grand. Il est ensuite possible de naviguer dans la selection via les boutons "<<" et ">>" dans la fenêtre sous l'image.
L'ajout d'image se fait via le bouton en haut à droite de la fenêtre principale, les références de l'image (qui permettront ensuite la recherche dans la base de données) sont : 
	- titre du film ("source")
	- année
	- pays
	- chef opérateur
	- réalisateur
	- genre
	- acteur(s) présent(s) dans le cadre
	- valeur de cadre
	- format de l'image
	- emulsion
	- focale
	- couleur(s)
	- ambiance (jour/soir/nuit)
	- lieux (intérieur/extérieur)
	- nature des sources de lumière utilisées
	- contraste
	- commentaire sur l'image
Il est tout à fait possible de laisser un ou plusieurs de ces champs vides.

Réalisée en Python avec les modules Tkinter/PIL et une base de données MySql.
Nécessite l'installation d'une base de données MySql puis de rentrer ses identifiants aux espaces prévus dans le fichier ConnexionDB.py (l'ouverture de l'application se charge ensuite de la création de la base et de la table ainsi que de l'insertion de 10 images prévues de base).

![](https://github.com/flejoncour/Photogrammes/blob/master/images/fenetrePrincipale.png?raw=True)
![](https://github.com/flejoncour/Photogrammes/blob/master/images/lecteurImage.png)
![](https://github.com/flejoncour/Photogrammes/blob/master/images/fenetreAjoutBDD.png)




