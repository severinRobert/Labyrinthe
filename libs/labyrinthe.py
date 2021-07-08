
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
        """
        Cette fonction crée le labyrinthe visible par le joueur

        :return: liste de string contenant le labyrinthe visible par le joueur
        """

        mur_entier = self.mur * self.taille  # création des murs du haut et du bas
        ligne_vide = self.mur + self.vide * (self.taille - 2) + self.mur
        lab_visible = []
        for i in range(self.taille):
            if i == 0 or i == self.taille-1:
                lab_visible.append(mur_entier)
            else:
                lab_visible.append(ligne_vide)
        lab_visible[self.arrivee[0]] = self.remplacer(lab_visible[self.arrivee[0]], self.arrivee[1], self.vide)
        return lab_visible

    def remplacer(self, str, index, r):
        """
        Cette fonction permet de remplacer les murs quand ils ont été touché, les faire apparraitre ou quand le joueur
        a bougé de place de remplacer la marque de l'emplacement prècedent
        :param str: chaine de caractere dans laquelle on veut remplacer le dit caractere
        :param index: index du caractere a remplacer
        :param r: caractere qui va remplacer
        :return: return le caractere changer à l'endroit voulue
        """

        if index < 0:  # ajout au début
            return r + str
        if index > len(str):  # ajout à la fin
            return str + r
        return str[:index] + r + str[index + 1:]

    def affichage(self, lab):
        for ligne in lab:
            print(ligne)
