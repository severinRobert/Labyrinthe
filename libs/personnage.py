from time import sleep


class Personnage:

    def deplacement(self, lab, direction, coord, lab_visible):
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
            lab_visible[coord[0]] = lab.remplacer(lab_visible[coord[0]], coord[1], lab.mur)
            coord = list(lab.depart)
            print("VOUS ÊTES MORT, RETOUR AU POINT DE DÉPART")
            sleep(0.5)
        return coord
