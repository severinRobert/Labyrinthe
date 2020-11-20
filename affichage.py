import pygame

# initialize the pygame
pygame.init()
FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

# create the screen
x = 1920
y = 1020
screen = pygame.display.set_mode((x,y))

# title and icon
pygame.display.set_caption("Labyrinthe")
icon = pygame.image.load('labyrinth.png')
pygame.display.set_icon(icon)

#set up the colors
white = (255, 255, 255)
black = (  0,   0,   0)
green = (0, 255, 0)
blue = (0, 0, 180)
red   = (255,   0,   0)

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        font = pygame.font.SysFont(None, round(y/24))
        img = font.render("z", True, (255, 255, 255))
        screen.blit(img, (20, 20))
    if keys[pygame.K_q]:
        font = pygame.font.SysFont(None, 84)
        img = font.render("q", True, (255, 255, 255))
        screen.blit(img, (20, 20))
    if keys[pygame.K_s]:
        font = pygame.font.SysFont(None, 64)
        img = font.render("s", True, (255, 255, 255))
        screen.blit(img, (20, 20))
    if keys[pygame.K_d]:
        font = pygame.font.SysFont(None, 24)
        img = font.render("d", True, (255, 255, 255))
        screen.blit(img, (20, 20))

    pygame.draw.rect(screen,red, (200, 150, 50, 50))
    pygame.display.update()

    fpsClock.tick(FPS)