import pygame
from pygame.locals import *

pygame.init()


def menu(surface):
    choice = pygame.image.load('menu.PNG')
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                if 1214 < event.pos[0] < 1411 and 74 < event.pos[1] < 126:
                    go = False
        surface.blit(choice, (0, 0))
        pygame.display.update()


def display(ecran, l, h, taille):
    police = 'freesansbold.ttf'
    point1 = 5
    point2 = 2
    pygame.draw.rect(ecran, ORANGE, (0, 0, LONGUEUR // 2, HAUTEUR))  # On dessine les 2 zones de couleur
    pygame.draw.rect(ecran, GRIS, (LONGUEUR // 2, 0, LONGUEUR, HAUTEUR))

    textePlayer1 = pygame.font.Font(police, 48).render("Player 1", True, BLACK, ORANGE)  # On affiche les joueurs
    ecran.blit(textePlayer1, (l * 0.1, h * 0.05))
    textePlayer2 = pygame.font.Font(police, 48).render("Player 2", True, BLACK, GRIS)
    ecran.blit(textePlayer2, (l * 0.8, h * 0.05))

    scorePlayer2 = pygame.font.Font(police, 70).render(str(point2), True, WHITE,
                                                       ORANGE)  # On affiche le score des joueurs
    ecran.blit(scorePlayer2, (l * 0.15, h * 0.4))
    scorePlayer1 = pygame.font.Font(police, 70).render(str(point1), True, WHITE, GRIS)
    ecran.blit(scorePlayer1, (l * 0.85, h * 0.4))

    logo = pygame.image.load("logo.PNG")  # On affiche le Logo
    ecran.blit(logo, (LONGUEUR * 0.29, HAUTEUR * 0.75))
    pygame.draw.line(ecran, BLACK, (LONGUEUR * 0.5, HAUTEUR * 0.80), (LONGUEUR * 0.5, HAUTEUR), 10)

    case = pygame.image.load("case.png")  # On affiche le tableau
    defaultValue = (l * 0.5) - (44 * (
            taille / 2))  # On place le tableau à la moitié de la fenêtre, puis on soustrait la taille de la moitié des cases pour avoir le même nombre de cases de chaque côté
    absc = defaultValue
    ordo = h * 0.1
    for y in range(taille):
        for x in range(taille):
            value = pygame.font.Font(police, 20).render("0", True, BLACK, WHITE)
            ecran.blit(case, (absc, ordo))
            ecran.blit(value, (absc + 20, ordo + 15))
            absc += 43
        ordo += 43
        absc = defaultValue

    pygame.display.update()


LONGUEUR = 1450
HAUTEUR = 815
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (228, 108, 10)
GRIS = (42, 46, 63)

ecran = pygame.display.set_mode((LONGUEUR, HAUTEUR))
pygame.display.set_caption("SOS Game")

n = 10
menu(ecran)
display(ecran, LONGUEUR, HAUTEUR, n)

Play = True
while Play:
    for event in pygame.event.get():
        if event.type == QUIT:
            Play = False
pygame.quit()
