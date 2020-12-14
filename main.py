from os import system
from libs.labyrinthe import Labyrinthe
from libs.personnage import Personnage
from libs.rang import rng_lab
from libs.console import Console
from libs.gui import Gui

# test
# initialisation  des variables globales
joueur = Personnage()
continuer = True
print("Bonjour bienvenue dans le labyrinthe !\nVotre but est d'atteindre la sortie en vous dirigeant à l'aide de q,d,z,s (gauche,droite,haut,bas)\n"
    "Mais attention aux murs qui ne seront visible que lorsque vous vous y cognerez!")

type_gui = input("1. console / 2. GUI ?")
if type_gui == "1" or type_gui == "console":
    gui = Console()
else:
    print("GUI pas encore construit")
    gui = Gui(400, 300)
    continuer = False

type_lab = gui.input('voulez-vous jouer des labyrinthes random ? o/n')
if type_lab == "o":
    taille = int(gui.input("quelle taille ?21/31/41/51"))
    lab1 = Labyrinthe([], taille, [], [])
    rng_lab(lab1)
else:
    lb = ["##########",
          "#        #",
          "# #####  #",
          "# #   ####",
          "# # #     ",
          "# # ######",
          "# #      #",
          "# ###### #",
          "#        #",
          "##########"]
    depart = [2, 8]
    arrivee = [4, 9]
    lab1 = Labyrinthe(lb, len(lb), depart, arrivee)

coord = list(lab1.depart)
lab_visible = Labyrinthe.creation_lab.__get__(lab1)
while continuer:
    # place le joueur aux coordonnées actuelles
    lab_visible[coord[0]] = lab1.remplacer(lab_visible[coord[0]], coord[1], lab1.personnage)
    gui.affichage(lab_visible)  # on affiche le labyrinthe
    ancienneC = list(coord)  # on stock l'ancienne coordonnée
    direction = gui.input("direction : ")  # choix de la direction
    # on change les nouvelles coordonnées du joueur et on vérifie les cas exceptionnels
    coord = joueur.deplacement(lab1, direction, coord, lab_visible,gui)
    if coord == lab1.arrivee:
        gui.print_texte("VOUS AVEZ GAGNÉ !!")
        continuer = False
    # supprime le "x" de l'ancienne position du joueur
    lab_visible[ancienneC[0]] = lab1.remplacer(lab_visible[ancienneC[0]], ancienneC[1], lab1.vide)
system("pause")
