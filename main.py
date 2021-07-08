from os import system
from libs.personnage import Personnage
from libs.console import jeu_console
from libs.gui import jeu_gui
from libs.rang import rng_lab
from libs.labyrinthe import Labyrinthe

# test
# initialisation  des variables globales
joueur = Personnage()

print("Bonjour bienvenue dans le labyrinthe !\nVotre but est d'atteindre la sortie en vous dirigeant à l'aide"
      " de q,d,z,s (gauche,droite,haut,bas)\nMais attention aux murs qui ne seront visible que lorsque vous "
      "vous y cognerez!")
type_lab = input('voulez-vous jouer des labyrinthes random ? o/n')
if type_lab == "o":
    taille = 0
    while taille < 7 and taille % 2 == 0:
        try:
            taille = int(input("Choisissez une taille impaire au dessus de 7 : "))
            break
        except ValueError:
            print("Ceci n'est pas un nombre")
        except Exception as e:
            # Just print(e) is cleaner and more likely what you want,
            # but if you insist on printing message specifically whenever possible...
            print(f"Une erreur s'est produite : {e} {e.message}")

    lab1 = Labyrinthe([], int(taille), [], [])
    rng_lab(lab1)
    lab1.affichage(lab1.lab)
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

type_gui = input("1. console / 2. GUI ?")
if type_gui == "1" or type_gui == "console":
    jeu_console(joueur, lab1)
else:
    print("GUI pas encore construit")
    jeu_gui(800, 600, lab1, joueur)

system("pause")
