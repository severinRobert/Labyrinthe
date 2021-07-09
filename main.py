import sys
from libs.personnage import Personnage
from libs.console import jeu_console
from libs.gui import jeu_gui
from libs.rang import rng_lab
from libs.labyrinthe import Labyrinthe

def menu():
    # initialisation  des variables globales

    print("\nBonjour bienvenue dans le labyrinthe !\nVotre but est d'atteindre la sortie en vous dirigeant à l'aide"
          " de q,d,z,s (gauche,droite,haut,bas)\nMais attention aux murs qui ne seront visible que lorsque vous "
          "vous y cognerez!\nÀ tous moment tapez '0' dans le menu pour revenir en arrière.")
    type_lab = input('Choisissez le type de labyrinthe : 0. Quitter / 1. Labyrinthe random / 2. Labyrinthe Prédéfini\n')

    while type_lab.upper() not in ["0","1","2"]:
        type_lab = input("La valeur entrée est incorrecte, veuillez entrer '0' ou '1' ou '2' : ")

    if type_lab == "1":
        menu_random()
    elif type_lab == "2":
        menu_labyrinthe()


def menu_random():
    taille = 0
    while taille < 7 and taille % 2 == 0:
        try:
            taille = int(input("Choisissez une taille impaire au dessus de 7 (0 pour revenir en arrière dans le menu) : "))
            break
        except ValueError:
            print("Ceci n'est pas un nombre")
        except:
            print(f"Une erreur s'est produite")
    # retour en arrière
    if taille == 0:
        menu()

    labyrinthe = Labyrinthe([], int(taille), [], [])
    rng_lab(labyrinthe)

    labyrinthe.affichage(labyrinthe.lab)

    menu_graphique(labyrinthe)

def menu_labyrinthe():
    choix_lab = input("Choisissez un labyrinthe : 0 (retour) / 1. facile / 2. moyen / 3. difficile\n")
    while choix_lab not in ["0","1","2","3"]:
        choix_lab = input("La valeur entrée est incorrecte, veuillez entrer '0' ou '1' ou '2' ou '3' : ")

    if choix_lab == "0":
        menu()
    elif choix_lab == "1":
        lb = ["##### #",
              "#     #",
              "# #####",
              "#   # #",
              "### # #",
              "#     #",
              "#######"]
        depart = [3, 5]
        arrivee = [0, 5]
        labyrinthe = Labyrinthe(lb, len(lb), depart, arrivee)
    elif choix_lab == "2":
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
        labyrinthe = Labyrinthe(lb, len(lb), depart, arrivee)
    elif choix_lab == "3":
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
        labyrinthe = Labyrinthe(lb, len(lb), depart, arrivee)
    menu_graphique(labyrinthe)

def menu_graphique(labyrinthe):
    joueur = Personnage()
    type_gui = input("Choisissez l'interface graphique : 0. retour / 1. console / 2. GUI\n")
    if type_gui == "1" or type_gui.upper() == "CONSOLE":
        jeu_console(joueur, labyrinthe)
    elif type_gui == "2" or type_gui.upper() == "GUI":
        jeu_gui(800, 600, labyrinthe, joueur)

    # retour
    elif type_gui == "0" and labyrinthe.random:
        menu_random()
    elif type_gui == "0" and not labyrinthe.random:
        menu_labyrinthe()
    fin()

def fin():
    print("Bravo vous avez vaincu ce labyrinthe !")
    choix_continuer = input("Voulez-vous continuer de jouer ? 1. Continuer à jouer / 2. Quitter le jeu\n")
    while choix_continuer.upper() not in ["1","2"]:
        choix_continuer = input("La valeur entrée est incorrecte, veuillez entrer '1' ou '2' : ")
    if choix_continuer == "1":
        menu()
    elif choix_continuer == "2":
        sys.exit

if __name__ == "__main__":
    menu()