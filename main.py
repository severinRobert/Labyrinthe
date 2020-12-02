''''''
from labyrinthe import Labyrinthe
from os import system

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

def deplacement(lab, direction, coord, labVisible):
    gauche = "q"
    droite = "d"
    haut = "z"
    bas = "s"

    if direction == gauche and coord[1] > 0:  # GAUCHE
        coord[1] = coord[1] - 1
    elif direction == droite and coord[1] < lab.taille - 1:  # DROITE
        coord[1] = coord[1] + 1
    elif direction == haut and coord[0] > 0:  # HAUT
        coord[0] = coord[0] - 1
    elif direction == bas and coord[0] < lab.taille - 1:  # BAS
        coord[0] = coord[0] + 1
    else:
        print("commande non reconnue")
        sleep(1)
    if lab.lab[coord[0]][coord[1]] == "#":  # SI ON RENCONTRE UN MUR
        labVisible[coord[0]] = lab.remplacer(labVisible[coord[0]], coord[1], lab.mur)
        coord[0] = depart[0]
        coord[1] = depart[1]
        print("VOUS ÊTES MORT, RETOUR AU POINT DE DÉPART")
        sleep(1)
    if coord == arrivee:  # SI ON EST ARRIVÉ À LA SORTIE
        return True

    labVisible[arrivee[0]] = lab.remplacer(labVisible[arrivee[0]], arrivee[1], lab.vide)
print("Bonjour bienvenue dans le labyrinthe !\nVotre but est d'atteindre la sortie en vous dirigeant à l'aide de q,d,z,s (gauche,droite,haut,bas)\n"
      "Mais attention aux murs qui ne seront visible que lorsque vous vous y cognerez!")

while continuer:
    # place le joueur aux coordonnées actuelles

    labVisible[coord[0]] = lab1.remplacer(labVisible[coord[0]], coord[1], lab1.personnage)
    lab1.affichage(labVisible)  # on affiche le labyrinthe
    ancienneC = list(coord)  # on stock l'ancienne coordonnée
    direction = input("direction : ")  # choix de la direction
    # on change les nouvelles coordonnées du joueur et on vérifie les cas exceptionnels
    if deplacement(lab1, direction, coord, labVisible):
        print("VOUS AVEZ GAGNÉ !!")
        continuer = False
    # supprime le "x" de l'ancienne position du joueur
    labVisible[ancienneC[0]] = lab1.remplacer(labVisible[ancienneC[0]], ancienneC[1], lab1.vide)
system("pause")
