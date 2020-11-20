# Création des classes, methodes et fonctions


class Labyrinthe:

    def __init__(self, lab, taille=10, personnage="x", mur="#", vide="-", mort=0):
        self.lab = lab
        self.taille = taille
        self.personnage = personnage
        self.mur = mur
        self.vide = vide
        self.mort = mort

    @property
    def creation_lab(self):
        """
        Cette methode crée le labyrinthe qui sera visible par le joueur

        :return labVisible:
        :rtype: list
        """

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
        """
        Cette methode permet de remplacer un caractere d'une chaine de caracteres par un autre à un emplacement donné

        :param str: chaine de caracteres qui va etre modifiee
        :param index: endroit du caractere à remplacer
        :param r: caractere à ajouter

        :return: la chaine de caracteres changee
        """
        if index < 0:  # ajout au début
            return r + str
        if index > len(str):  # ajout à la fin
            return str + r
        return str[:index] + r + str[index + 1:]

    def affichage(self, lab):  # imprime le lab
        """
        Cette methode permet d'afficher le labyrinthe en console

        :param lab: le labyrinthe à afficher

        :return: none
        """
        for ligne in lab:  # verifier si je dois mettre self ?
            print(ligne)
