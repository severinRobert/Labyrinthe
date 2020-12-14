# Création des classes, methodes et fonctions

# test n2
class Labyrinthe:

    def __init__(self, lab, taille, depart, arrivee, personnage="x", mur="#", vide="-", mort=0):
        self.lab = lab
        self.taille = taille
        self.personnage = personnage
        self.mur = mur
        self.vide = vide
        self.mort = mort
        self.depart = depart
        self.arrivee = arrivee

    @property
    def creation_lab(self):

        murEntier = self.mur * self.taille
        ligneVide = self.mur + self.vide * (self.taille - 2) + self.mur
        lab_visible = []
        for i in range(self.taille):
            if i == 0 or i == self.taille-1:
                lab_visible.append(murEntier)
            else:
                lab_visible.append(ligneVide)
        lab_visible[self.arrivee[0]] = self.remplacer(lab_visible[self.arrivee[0]],self.arrivee[1],self.vide)
        return lab_visible

    def remplacer(self, str, index, r):
        if index < 0:  # ajout au début
            return r + str
        if index > len(str):  # ajout à la fin
            return str + r
        return str[:index] + r + str[index + 1:]

    def affichage(self, lab):  # imprime le lab
        for ligne in lab:  # verifier si je dois mettre self ?
            print(ligne)
