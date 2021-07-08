import pygame, sys, math
from libs.rang import rng_lab
from libs.labyrinthe import Labyrinthe

"""
def jeu(lab, lab_visible, coord, joueur):
    ""
    Cette fonction gère l'affichage
    :param lab: instance de classe de Labyrinthe dans laquelle sera stocké le labyrinthe, départ et arrivée
    :param lab_visible: liste représentant le labyrinthe visible par le joueur
    :param coord: liste [x,y] représentant les coordonnées du joueur
    :param joueur: instance de classe de Personnage qui permet le déplacement du joueur
    :return: rien
    ""
    # place le joueur aux coordonnées actuelles
    lab_visible[coord[0]] = lab.remplacer(lab_visible[coord[0]], coord[1], lab.personnage)
    lab.affichage(lab_visible)  # on affiche le labyrinthe
    ancienne_coord = list(coord)  # on stock l'ancienne coordonnée
    direction = input("direction : ")  # choix de la direction
    # on change les nouvelles coordonnées du joueur et on vérifie les cas exceptionnels
    coord = joueur.deplacement(lab, direction, coord, lab_visible)
    if coord == lab.arrivee:
        print("VOUS AVEZ GAGNÉ !!")
        continuer = False
    # supprime le "x" de l'ancienne position du joueur
    lab_visible[ancienne_coord[0]] = lab.remplacer(lab_visible[ancienne_coord[0]], ancienne_coord[1], lab.vide)
"""

def jeu_gui(largeur_fenetre: int, hauteur_fenetre: int, lab, joueur):
    """
    Cette fonction gère l'affichage graphique  du jeu en initialisant pygame et ouvrant la boucle de gameplay et gère
    aussi les input du joueur
    :param largeur_fenetre: largeur de la fenêtre de jeu
    :param hauteur_fenetre: hauteur de la fenêtre de jeu
    :param lab: instance de classe de Labyrinthe dans laquelle sera stocké le labyrinthe, départ et arrivée
    :param joueur: instance de classe de Personnage qui permet le déplacement du joueur
    :return: rien
    """
    # initialisation
    pygame.init()
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    clock = pygame.time.Clock()
    carre = math.floor(hauteur_fenetre/len(lab.lab))

    # titre et icon
    pygame.display.set_caption("Labyrinthe")
    # icon = pygame.image.load('')
    # pygame.display.set_icon(icon)

    # game_font = pygame.font.Font()
    rouge = (255, 0, 0)
    vert = (0, 255, 0)
    noir = (0, 0, 0)
    coord = list(lab.depart)
    lab_visible = Labyrinthe.creation_lab.__get__(lab)
    while True:
        for i in range(len(lab_visible)):
            for j in range(len(lab_visible[i])):
                if lab_visible[i][j] == "#":
                    pygame.draw.rect(screen, rouge, (carre*j, carre*i, carre, carre))
                else:
                    pygame.draw.rect(screen, noir, (carre * j, carre * i, carre, carre))
        pygame.draw.rect(screen, vert, (carre * coord[1], carre * coord[0], carre, carre))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    coord = joueur.deplacement(lab, "q", coord, lab_visible)
                elif event.key == pygame.K_RIGHT:
                    coord = joueur.deplacement(lab, "d", coord, lab_visible)
                elif event.key == pygame.K_UP:
                    coord = joueur.deplacement(lab, "z", coord, lab_visible)
                elif event.key == pygame.K_DOWN:
                    coord = joueur.deplacement(lab, "s", coord, lab_visible)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)
