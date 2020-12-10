from time import sleep
from os import system
from labyrinthe import Labyrinthe
from personnage import Personnage
# test
# initialisation  des variables globales
lab1 = Labyrinthe(["##########",
                   "#        #",
                   "# #####  #",
                   "# #   ####",
                   "# # #     ",
                   "# # ######",
                   "# #      #",
                   "# ###### #",
                   "#        #",
                   "##########"])
continuer = True
depart = [2, 8]
arrivee = [4, 9]
coord = list(depart)
labVisible = Labyrinthe.creation_lab.__get__(lab1)
joueur = Personnage()

print("Bonjour bienvenue dans le labyrinthe !\nVotre but est d'atteindre la sortie en vous dirigeant à l'aide de q,d,z,s (gauche,droite,haut,bas)\n"
      "Mais attention aux murs qui ne seront visible que lorsque vous vous y cognerez!")

while continuer:
    # place le joueur aux coordonnées actuelles

    labVisible[coord[0]] = lab1.remplacer(labVisible[coord[0]], coord[1], lab1.personnage)
    lab1.affichage(labVisible)  # on affiche le labyrinthe
    ancienneC = list(coord)  # on stock l'ancienne coordonnée
    direction = input("direction : ")  # choix de la direction
    # on change les nouvelles coordonnées du joueur et on vérifie les cas exceptionnels
    if joueur.deplacement(lab1, direction, coord, labVisible):
        print("VOUS AVEZ GAGNÉ !!")
        continuer = False
    # supprime le "x" de l'ancienne position du joueur
    labVisible[ancienneC[0]] = lab1.remplacer(labVisible[ancienneC[0]], ancienneC[1], lab1.vide)
system("pause")
