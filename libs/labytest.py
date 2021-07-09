import unittest
from libs.personnage import Personnage
from libs.labyrinthe import Labyrinthe

lb = ["##########",
      "#        #",
      "# #####  #",
      "# #   ####",
      "# # #     ",
      "# # ######",
      "# #      #",
      "# ###### #",
      "#        #",
      "##########"]
depart = [2, 8]
arrivee = [4, 9]
lab1 = Labyrinthe(lb, len(lb), depart, arrivee)
lab_visible1 = Labyrinthe.creation_lab.__get__(lab1)

lb = ["#####",
      "#   #",
      "# ###",
      "#    ",
      "#####"]
depart = [1, 3]
arrivee = [3, 4]
lab2 = Labyrinthe(lb, len(lb), depart, arrivee)
lab_visible2 = Labyrinthe.creation_lab.__get__(lab2)


class LabyTestCase(unittest.TestCase):

    def test_type_renvoye(self):
        """Vérification du type renvoyé"""
        self.assertIsInstance(lab_visible1, list)
        self.assertIsInstance(lab_visible1[1], str)
        self.assertIsInstance(lab_visible2, list)
        self.assertIsInstance(lab_visible2[1], str)

    def test_contenu(self):

        self.assertEqual(lab_visible2, ["#####",
                                        "#---#",
                                        "#---#",
                                        "#----",
                                        "#####"])

        self.assertEqual(lab_visible1, ["##########",
                                        "#--------#",
                                        "#--------#",
                                        "#--------#",
                                        "#---------",
                                        "#--------#",
                                        "#--------#",
                                        "#--------#",
                                        "#--------#",
                                        "##########"])

    def test_type_renvoye(self):

        self.assertIsInstance(Labyrinthe.remplacer(self, "hello", 1, "a"), (str, int, str))
        self.assertIsInstance(Labyrinthe.remplacer(self, "Ceci est un test unitaire", 20, "p"), (str, int, str))
        self.assertIsInstance(Labyrinthe.remplacer(self, "#---#", 2, "x"), (str, int, str))
        self.assertIsInstance(Labyrinthe.remplacer(self, "#---#", 0, "-"), (str, int, str))

    def test_caractere_remplacer(self):

        self.assertEqual(Labyrinthe.remplacer(self,"hello", 1, "a"), "hallo")
        self.assertEqual(Labyrinthe.remplacer(self, "Ceci est un test unitaire", 20, "p"), "Ceci est un test unipaire")
        self.assertEqual(Labyrinthe.remplacer(self, "#---#", 2, "x"), "#-x-#")
        self.assertEqual(Labyrinthe.remplacer(self, "#---#", 0, "-"), "----#")

class PersoTestCase(unittest.TestCase):

    def test_deplacement_correcte(self):
        """Déplacements possible"""
        self.assertEqual(Personnage().deplacement(lab2, "d", [1, 2], lab_visible2), [1, 3])
        self.assertEqual(Personnage().deplacement(lab2, "q", [1, 2], lab_visible2), [1, 1])
        self.assertEqual(Personnage().deplacement(lab2, "z", [2, 1], lab_visible2), [1, 1])
        self.assertEqual(Personnage().deplacement(lab2, "s", [2, 1], lab_visible2), [3, 1])

    def test_deplacement_vers_mur(self):
        """Déplacements sur un mur"""
        self.assertEqual(Personnage().deplacement(lab2, "d", [2, 1], lab_visible2), [1, 3])
        self.assertEqual(Personnage().deplacement(lab2, "q", [1, 1], lab_visible2), [1, 3])
        self.assertEqual(Personnage().deplacement(lab2, "z", [1, 2], lab_visible2), [1, 3])
        self.assertEqual(Personnage().deplacement(lab2, "s", [3, 3], lab_visible2), [1, 3])

    def test_mauvais_input(self):
        """Mauvais input"""
        self.assertEqual(Personnage().deplacement(lab2, "r", [2, 1], lab_visible2), [2, 1])
        self.assertEqual(Personnage().deplacement(lab2, "2", [1, 1], lab_visible2), [1, 1])
        self.assertEqual(Personnage().deplacement(lab2, "@", [1, 2], lab_visible2), [1, 2])
        self.assertEqual(Personnage().deplacement(lab2, "", [3, 3], lab_visible2), [3, 3])


if __name__ == '__main__':
    # ATTENTION : Pour exécuter ce test dans un notebook, il faut utiliser un appel à unittest.main() modifié.
    # Dans PyCharm, vous pouvez utiliser la version normale sans paramètre, cfr ci-dessous.
    # unittest.main()
    unittest.main()
