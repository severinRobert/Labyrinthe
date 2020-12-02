from time import sleep

class Personnage:

    def __init__(self, depart = [2, 8], arrivee = [4, 9]):
        self.depart = depart
        self.arrivee = arrivee


def deplacement(self, lab, direction, coord, labVisible):
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
        coord[0] = self.depart[0]
        coord[1] = self.depart[1]
        print("VOUS ÊTES MORT, RETOUR AU POINT DE DÉPART")
        sleep(1)
    if coord == self.arrivee:  # SI ON EST ARRIVÉ À LA SORTIE
        return True

    labVisible[self.arrivee[0]] = lab.remplacer(labVisible[self.arrivee[0]], self.arrivee[1], lab.vide)