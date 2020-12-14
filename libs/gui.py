import pygame
class Gui():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.screen = pygame.display.set_mode((x, y), 0, 32)
        self.screen.fill((  0,   0,   0))


    def affichage(self,lab):
        pass

    def print_texte(self,texte):
        pass

    def input(self,texte):
        pass