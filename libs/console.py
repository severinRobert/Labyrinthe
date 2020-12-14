class Console():
    def affichage(self, lab):  # imprime le lab
        for ligne in lab:
            print(ligne)

    def print_texte(self,texte):
        print(texte)

    def input(self,texte):
        return input(texte)