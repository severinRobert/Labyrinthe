# Création des classes, methodes et fonctions


class Labyrinthe:

    def __init__(self, lab = [], taille=10, personnage="x", mur="#", vide="-", mort=0):
        self.lab = lab
        self.taille = taille
        self.personnage = personnage
        self.mur = mur
        self.vide = vide
        self.mort = mort

    @property
    def creation_lab(self):

        murEntier = self.mur * self.taille
        ligneVide = self.mur + self.vide * (self.taille - 2) + self.mur
        labVisible = []
        for i in range(self.taille):
            if i == 0 or i == 9:
                labVisible.append(murEntier)
            else:
                labVisible.append(ligneVide)
        return labVisible

    def remplacer(self, str, index, r):
        if index < 0:  # ajout au début
            return r + str
        if index > len(str):  # ajout à la fin
            return str + r
        return str[:index] + r + str[index + 1:]

    def affichage(self, lab):  # imprime le lab
        for ligne in lab:  # verifier si je dois mettre self ?
            print(ligne)
