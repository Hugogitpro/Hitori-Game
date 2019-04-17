from lib import *


def get_image(path):
    """
    Chercher l'image dans le PATH indiqué
    en fonction du nom de l'image en paramètre
    :param path:
    :return:
    """
    return "image\\" + path


def caseToPixel(num, default=0.0):
    """
    Convertir les coordoonées des cases en pixel
    :param num:
    :param default:
    :return:
    """
    return math.floor(num * 43 + 22 + default)


def displayScore(maxPlayers, points, player):
    """
    Afficher les joueurs et le score des joueurs
    :param maxPlayers:
    :param points:
    :param player:
    """
    if maxPlayers == 2:
        textePlayer1 = pygame.font.Font(POLICE, 48).render("Player 1", True, COLOR[8], COLOR[3])  # On affiche les joueurs
        ecran.blit(textePlayer1, (LONGUEUR * 0.1, HAUTEUR * 0.05))
        textePlayer2 = pygame.font.Font(POLICE, 48).render("Player 2", True, COLOR[8], COLOR[6])
        ecran.blit(textePlayer2, (LONGUEUR * 0.8, HAUTEUR * 0.05))

        scorePlayer1 = pygame.font.Font(POLICE, 70).render(str(points[0]), True, COLOR[0],COLOR[3])  # On affiche le score des joueurs
        ecran.blit(scorePlayer1, (LONGUEUR * 0.15, HAUTEUR * 0.4))
        scorePlayer2 = pygame.font.Font(POLICE, 70).render(str(points[1]), True, COLOR[1], COLOR[6])
        ecran.blit(scorePlayer2, (LONGUEUR * 0.85, HAUTEUR * 0.4))
    if maxPlayers > 2:
        textePlayer1 = pygame.font.Font(POLICE, 48).render("Player 1", True, COLOR[8], COLOR[3])  # On affiche les joueurs
        ecran.blit(textePlayer1, (LONGUEUR * 0.05, HAUTEUR * 0.05))
        scorePlayer1 = pygame.font.Font(POLICE, 70).render(str(points[0]), True, COLOR[0], COLOR[3])
        ecran.blit(scorePlayer1, (LONGUEUR * 0.2, HAUTEUR * 0.05))

        textePlayer2 = pygame.font.Font(POLICE, 48).render("Player 2", True, COLOR[8], COLOR[6])
        ecran.blit(textePlayer2, (LONGUEUR * 0.85, HAUTEUR * 0.05))
        scorePlayer2 = pygame.font.Font(POLICE, 70).render(str(points[1]), True, COLOR[1], COLOR[6])
        ecran.blit(scorePlayer2, (LONGUEUR * 0.8, HAUTEUR * 0.05))

        textePlayer3 = pygame.font.Font(POLICE, 48).render("Player 3", True, COLOR[8], COLOR[3])
        ecran.blit(textePlayer3, (LONGUEUR * 0.05, HAUTEUR * 0.3))
        scorePlayer3 = pygame.font.Font(POLICE, 70).render(str(points[2]), True, COLOR[2], COLOR[3])
        ecran.blit(scorePlayer3, (LONGUEUR * 0.2, HAUTEUR * 0.3))

        if maxPlayers > 3:
            textePlayer4 = pygame.font.Font(POLICE, 48).render("Player 4", True, COLOR[8], COLOR[6])
            ecran.blit(textePlayer4, (LONGUEUR * 0.85, HAUTEUR * 0.3))
            scorePlayer4 = pygame.font.Font(POLICE, 70).render(str(points[3]), True, COLOR[3], COLOR[6])
            ecran.blit(scorePlayer4, (LONGUEUR * 0.8, HAUTEUR * 0.3))

            if maxPlayers > 4:
                textePlayer5 = pygame.font.Font(POLICE, 48).render("Player 5", True, COLOR[8], COLOR[3])
                ecran.blit(textePlayer5, (LONGUEUR * 0.05, HAUTEUR * 0.6))
                scorePlayer5 = pygame.font.Font(POLICE, 70).render(str(points[4]), True, COLOR[4], COLOR[3])
                ecran.blit(scorePlayer5, (LONGUEUR * 0.2, HAUTEUR * 0.6))

                if maxPlayers > 5:
                    textePlayer6 = pygame.font.Font(POLICE, 48).render("Player 6", True, COLOR[8], COLOR[6])
                    ecran.blit(textePlayer6, (LONGUEUR * 0.85, HAUTEUR * 0.6))
                    scorePlayer6 = pygame.font.Font(POLICE, 70).render(str(points[5]), True, COLOR[5], COLOR[6])
                    ecran.blit(scorePlayer6, (LONGUEUR * 0.8, HAUTEUR * 0.6))


def displayPlayer(ecran, player):
    """
    Afficher le tour du joueur
    :param ecran:
    :param player:
    """
    if player == 0:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 1", True, COLOR[6], COLOR[3])
        ecran.blit(textePlayer, (LONGUEUR * 0.1, HAUTEUR * 0.2))
    elif player == 1:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 2", True, COLOR[3], COLOR[6])
        ecran.blit(textePlayer, (LONGUEUR * 0.8, HAUTEUR * 0.2))
    elif player == 2:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 3", True, COLOR[6], COLOR[3])
        ecran.blit(textePlayer, (LONGUEUR * 0.1, HAUTEUR * 0.4))
    elif player == 3:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 4", True, COLOR[3], COLOR[6])
        ecran.blit(textePlayer, (LONGUEUR * 0.8, HAUTEUR * 0.4))
    elif player == 4:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 5", True, COLOR[6], COLOR[3])
        ecran.blit(textePlayer, (LONGUEUR * 0.1, HAUTEUR * 0.7))
    elif player == 5:
        textePlayer = pygame.font.Font(POLICE, 25).render("Player's turn 6", True, COLOR[3], COLOR[6])
        ecran.blit(textePlayer, (LONGUEUR * 0.8, HAUTEUR * 0.7))


def drawCell(ecran, tableau, x, y, absc, ordo):
    """
    Afficher la case et la valeur qu'elle contient (Graphiquement)
    :param ecran:
    :param tableau:
    :param x:
    :param y:
    :param absc:
    :param ordo:
    """
    case = pygame.image.load(get_image("case.png"))  # On affiche le tableau
    if tableau[x][y] == 1:
        value = pygame.font.Font(POLICE, 20).render("S", True, COLOR[8], COLOR[7])
    elif tableau[x][y] == 2:
        value = pygame.font.Font(POLICE, 20).render("O", True, COLOR[8], COLOR[7])
    else:
        value = pygame.font.Font(POLICE, 20).render(".", True, COLOR[8], COLOR[7])
    ecran.blit(case, (absc, ordo))
    ecran.blit(value, (absc + 20, ordo + 15))


def drawBoard(ecran, tableau, default):
    """
    Afficher/Dessiner le tableau avec les valeurs (Graphiquement)
    :param ecran:
    :param tableau:
    :param default:
    """
    absc = default[0]
    ordo = default[1]
    for y in range(len(tableau)):
        for x in range(len(tableau)):
            drawCell(ecran, tableau, x, y, absc, ordo)
            absc += 43
        ordo += 43
        absc = default[0]


def drawLines(ecran,lines, mot, default, player, saveLine):
    """
    Dessiner les lignes marquant les "SOS" réalisées
    :param ecran:
    :param lines:
    :param mot:
    :param default:
    :param player:
    :param saveLine:
    :return:
    """
    x = 0
    for line in lines:
        if type(line) == list and len(line) != 0:
            if mot:
                while len(saveLine[x]) != 0:
                    x+=1
                saveLine[x] = [(caseToPixel(line[0][0], default[0]), caseToPixel(line[0][1], default[1]), player),(caseToPixel(line[1][0], default[0]), caseToPixel(line[1][1], default[1]), player)]

    for line in saveLine:
        if type(line) == list and len(line) != 0:
                pygame.draw.line(ecran, COLOR[line[0][2]],(line[0][0],line[0][1]),(line[1][0],line[1][1]),EPAISSEUR)

    for line in lines:
        line[:] = []
    return lines


def rules(ecran):
    """
    Afficher les règles de jeu
    :param ecran:
    """
    go = False
    while not go:
        print("rules")
        ecran.blit(pygame.image.load(get_image("regles.png")), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                go = True


def displayWinner(scores, maxPlayers):
    """
    Afficher le résulat de la partie
    Proposer différentes solutions ( Rejoueur, Menu)
    :param scores:
    :param maxPlayers:
    :return:
    """
    tmp = 0
    for i in range(maxPlayers):
        if scores[i] > tmp:
            tmp = scores[i]
    if scores.count(tmp) > 1:
        win = "Egalite"
    else:
        win = "Winner " + str((scores.index(tmp)) + 1)
    result = pygame.font.Font(
        POLICE, 30).render(str(win), True, COLOR[7], COLOR[8])
    ecran.blit(result, (LONGUEUR * 0.47, 20))
    ecran.blit(pygame.image.load(get_image("home.png")), (LONGUEUR * 0.84, HAUTEUR * 0.863))
    ecran.blit(pygame.image.load(get_image("replay.png")), (LONGUEUR * 0.8, HAUTEUR * 0.85))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                posX, posY = event.pos
                if 734 < posY < 784:
                    if 1160 < posX < 1210:
                        return True
                    if 1218 < posX < 1268:
                        return False


def menu(surface):
    """
    Afficher menu
    Choisir mode de jeu
    :param surface:
    :return:
    """
    choice = pygame.image.load(get_image('menu1.PNG'))
    surface.blit(choice, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                if 1214 < event.pos[0] < 1411:
                    if 74 < event.pos[1] < 126:
                        return 1
                    if 264 < event.pos[1] < 309:
                        return 3
                    if 172 < event.pos[1] < 215:
                        return 2
                    if  340 < event.pos[1] < 385:
                        return 4


def nbJoueurs(ecran):
    """
    Sélectionner le nombre de joueurs
    :param ecran:
    :return:
    """
    while True:
        ecran.blit(pygame.image.load(get_image("joueur1.png")), (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONUP:
                posX, posY = event.pos
                if 395 < posY < 475:
                    if 265 < posX < 445:
                        return 3
                    if 635 < posX < 815:
                        return 4
                    if 1030 < posX < 1210:
                        return 5
                if 615 < posY < 695:
                    if 635 < posX < 815:
                        return 6


pygame.init()
ecran = pygame.display.set_mode((LONGUEUR, HAUTEUR))
pygame.display.set_caption("SOS Game")
pygame.display.set_icon(pygame.image.load(get_image("icon.png")))
