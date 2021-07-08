from libs.labyrinthe import Labyrinthe


def jeu_console(joueur, lab):
    continuer = True
    coord = list(lab.depart)
    lab_visible = Labyrinthe.creation_lab.__get__(lab)
    while continuer:
        # place le joueur aux coordonnées actuelles
        lab_visible[coord[0]] = lab.remplacer(lab_visible[coord[0]], coord[1], lab.personnage)
        lab.affichage(lab_visible)  # on affiche le labyrinthe
        ancienne_c = list(coord)  # on stock l'ancienne coordonnée
        direction = input("direction : ")  # choix de la direction
        # on change les nouvelles coordonnées du joueur et on vérifie les cas exceptionnels
        coord = joueur.deplacement(lab, direction, coord, lab_visible)
        if coord == lab.arrivee:
            print("VOUS AVEZ GAGNÉ !!")
            continuer = False
        # supprime le "x" de l'ancienne position du joueur
        lab_visible[ancienne_c[0]] = lab.remplacer(lab_visible[ancienne_c[0]], ancienne_c[1], lab.vide)
