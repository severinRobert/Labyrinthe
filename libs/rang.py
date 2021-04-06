import random as r


def bordsLab(bords,taille):
    for i in range(taille):
        if i == 0 or i == taille - 1:
            for j in range(taille):
                bords.append([i, j])
        else:
            bords.append([i, 0])
            bords.append([i, taille - 1])
    bords.remove([0, 0])
    bords.remove([0, taille - 1])
    bords.remove([taille - 1, 0])
    bords.remove([taille - 1, taille - 1])

def rng_lab(labyrinthe):
    """
    Cette fonction crée un labyrinthe random pour après inscrire les informations dans une instance de classe
    :param labyrinthe: instance de classe de Labyrinthe dans laquelle sera stocké le labyrinthe,départ et arrivée
    :return: rien
    """
    taille = labyrinthe.taille
    lab = []
    bords = []
    bordsLab(bords,taille)
    sortie_interdite = [[0, 0], [0, 1], [0, taille - 1], [0, taille], [1, 0], [1, taille], [taille - 1, 0],
                        [taille - 1, taille],[taille, 0], [taille, 1], [taille, taille - 1], [taille, taille]]
    for i in range(taille):
        lab.append("#" * taille)

    choix_sortie = [bords[i] for i, bord in enumerate(bords) if (bords[i][0] % 2 == 1 or bords[i][1] % 2 == 1) and
                    bords[i] not in sortie_interdite]
    sortie = r.choice(choix_sortie)
    pointRef = list(sortie)
    if sortie[0] == taille - 1:
        pointRef[0] -= 1
    elif sortie[0] == 0:
        pointRef[0] += 1
    elif sortie[1] == taille - 1:
        pointRef[1] -= 1
    elif sortie[1] == 0:
        pointRef[1] += 1

    premier_cul_de_sac = False
    chemin = [sortie, pointRef]
    point = list(pointRef)
    nb_visite_max = ((taille - 1) / 2) ** 2
    # stocks les coordonnées par lesquelles on est passé
    visite = []
    stack = []
    # tant que le labyrinthe entier n'a pas été rempli de chemins
    while len(visite) != nb_visite_max:
        # on regarde si dans les cases à 2 pas sont libre donc si il n'y a pas un mur ou déjà un chemin
        choix_suite = [i for i in [[[point[0], point[1] + 2], [point[0], point[1] + 1]],
                                    [[point[0], point[1] - 2], [point[0], point[1] - 1]],
                                    [[point[0] + 2, point[1]], [point[0] + 1, point[1]]],
                                    [[point[0] - 2, point[1]], [point[0] + 1, point[1]]]]
                        if not i[0] in bords and not i[0] in visite and 0 < i[0][0] < taille - 1 and 0 < i[0][1] < taille-1]
        # si toute les cases sont déjà prises on regarde à la case précédente
        if choix_suite == []:
            stack.pop()
            point = list(stack[-1])
            depart = depart if premier_cul_de_sac else point
        # sinon on choisit un point au hazard dans les choix possible
        else:
            nouveau_point = r.choice(choix_suite)
            visite.append(nouveau_point[0])
            stack.append(nouveau_point[0])
            chemin.append(nouveau_point[0])
            chemin.append(nouveau_point[1])
            point = list(nouveau_point[0])
    # on remplace toutes les coordonnées dans chemin par des espace
    for i in chemin:
        if not i in bords or i == sortie:
            lab[i[0]] = labyrinthe.remplacer(lab[i[0]], i[1], " ")
    # on enregistre toutes les données du labyrinthe crée dans l'instance passée en paramètre
    labyrinthe.arrivee = sortie
    labyrinthe.lab = lab
    labyrinthe.depart = point
    print(sortie)
    print(pointRef)
