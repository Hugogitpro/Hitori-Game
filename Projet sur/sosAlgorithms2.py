from sosGUI import *


'''def chargement():
    try:
        fichier = open("texte.json", "r")
        joueur = int(fichier.readline())
        print("Good opening")
        scores = json.loads(fichier.readline())
        print("Good opening")
        saveLine = json.loads(fichier.readline())
        print("Good opening")
        tableau = json.loads(fichier.readline())
        print("Good opening")
        fichier.close()
        return joueur, scores, saveLine, tableau
    except:
        print("error opening")
        return -1'''


def PixelToCase(nbPix, default=0.0):
    return math.floor((nbPix - default) // 43)


def inversePlayer(player, maxPlayers):
    if player == maxPlayers - 1:
        return 0
    player += 1
    return player


def new_Board(ecran):
    menu_dimension = pygame.image.load(get_image("dimension.PNG"))
    pygame.transform.scale(menu_dimension, (LONGUEUR, HAUTEUR))
    ecran.blit(menu_dimension, (0, 0))
    pygame.display.update()
    dimension = 0
    while dimension == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONUP:
                posX, posY = event.pos
                if 330 < posY < 410:
                    if 65 < posX < 240:
                        dimension = 1
                    if 290 < posX < 465:
                        dimension = 2
                    if 510 < posX < 685:
                        dimension = 3
                    if 730 < posX < 910:
                        dimension = 4
                    if 950 < posX < 1130:
                        dimension = 5
                    if 1170 < posX < 1355:
                        dimension = 6
                if 495 < posY < 570:
                    if 65 < posX < 245:
                        dimension = 7
                    if 285 < posX < 495:
                        dimension = 8
                    if 510 < posX < 685:
                        dimension = 9
                    if 730 < posX < 910:
                        dimension = 10
                    if 950 < posX < 1130:
                        dimension = 11
                    if 1170 < posX < 1355:
                        dimension = 12
                if 655 < posY < 740:
                    if 625 < posX < 735:
                        dimension = 13
    tableau = [[0] * dimension for i in range(dimension)]
    return tableau


def display(ecran, tableau, points, mot, lines, player, maxPlayers, default, saveLine=[[] * 0 for i in range(0)]):
    pygame.draw.rect(ecran, COLOR[3], (0, 0, LONGUEUR // 2, HAUTEUR))  # On dessine les 2 zones de couleur
    pygame.draw.rect(ecran, COLOR[6], (LONGUEUR // 2, 0, LONGUEUR, HAUTEUR))

    logo = pygame.image.load(get_image("logo.PNG"))  # On affiche le Logo
    ecran.blit(logo, (LONGUEUR * 0.35, HAUTEUR * 0.78))

    ecran.blit(pygame.image.load(get_image("help.png")), (LONGUEUR * 0.9, HAUTEUR * 0.895))

    drawBoard(ecran, tableau, default)
    displayScore(maxPlayers, points)
    lines = drawLines(ecran, lines, mot, default, player, saveLine)
    displayPlayer(ecran, player)

    pygame.display.update()
    return lines


def selectSquare(tableau, default, points, mot, lines, player, maxPlayers):
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONDOWN:
                if 1305 < event.pos[0] < 1355:
                    if 734 < event.pos[1] < 784:
                        rules(ecran)
                        print("display")
                        display(ecran, tableau, points, mot, lines, player, maxPlayers, default)
                typeOfMouse = pygame.mouse.get_pressed()
                if possibleSquare(tableau, event.pos[0], event.pos[1], default):
                    return PixelToCase(event.pos[0], default[0]), PixelToCase(event.pos[1], default[1]), typeOfMouse


def possibleSquare(tableau, posX, posY, default):
    if default[0] < posX < default[0] + 43 * len(tableau):
        if default[1] < posY < default[1] + 43 * len(tableau):
            if tableau[PixelToCase(posX, default[0])][PixelToCase(posY, default[1])] == 0:
                return True
    return False


def update(tableau, x, y, joueur, points, lines, choice, nbMot, maxPlayers):
    if choice[0]:  # Si clique droit, alors valeur S
        tableau[x][y] = 1
        points, nbMot, lines = updateScoreS(tableau, x, y, points, joueur, lines)
    elif choice[2]:  # Si clique gauche alors valeur O
        tableau[x][y] = 2
        points, nbMot, lines = updateScoreO(tableau, x, y, points, joueur, lines)
    if not nbMot:
        joueur = inversePlayer(joueur, maxPlayers)
    return tableau, points, joueur, nbMot, lines


def updateScoreO(tableau, x, y, points, joueur, lines):
    # On vérifie SOS en diagonale (on cherche les 2 S autour de O)
    nbSegment = 0
    check = False
    if x - 1 >= 0 and y - 1 >= 0 and tableau[x - 1][y - 1] == 1:  # On vérifie si on a SOS en diagonale
        if x + 1 < len(tableau) and y + 1 < len(tableau) and tableau[x + 1][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x - 1, y - 1), (x + 1, y + 1)]
            nbSegment += 1
            check = True
            print("O diagonale")
    if x + 1 < len(tableau) and y - 1 >= 0 and tableau[x + 1][y - 1] == 1:  # On vérifie si on a SOS en diagonale
        if x - 1 >= 0 and y + 1 < len(tableau) and tableau[x - 1][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x + 1, y - 1), (x - 1, y + 1)]
            nbSegment += 1
            check = True
            print("O diagonale")
    if y - 1 >= 0 and tableau[x][y - 1] == 1:  # On vérifie si on a SOS en verticale
        if y + 1 < len(tableau) and tableau[x][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y - 1), (x, y + 1)]
            nbSegment += 1
            check = True
            print("O verticale")
    if x + 1 < len(tableau) and tableau[x + 1][y] == 1:  # On vérifie si on a SOS en horizontale
        if x - 1 >= 0 and tableau[x - 1][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x + 1, y), (x - 1, y)]
            nbSegment += 1
            check = True
            print("O horizontale")
    return points, check, lines


def updateScoreS(tableau, x, y, points, joueur, lines):
    nbSegment = 0
    check = False
    if x - 1 >= 0 and y - 1 >= 0 and tableau[x - 1][y - 1] == 2:
        if x - 2 >= 0 and y - 2 >= 0 and tableau[x - 2][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y - 2)]
            nbSegment += 1
            check = True
            print("S diagonale haut gauche")
    if x + 1 < len(tableau) and y - 1 >= 0 and tableau[x + 1][y - 1] == 2:
        if x + 2 < len(tableau) and y - 2 >= 0 and tableau[x + 2][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y - 2)]
            nbSegment += 1
            check = True
            print("S diagonale haut droite")
    if x - 1 >= 0 and y + 1 < len(tableau) and tableau[x - 1][y + 1] == 2:
        if x - 2 >= 0 and y + 2 < len(tableau) and tableau[x - 2][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y + 2)]
            nbSegment += 1
            check = True
            print("S diagonale bas gauche")
    if x + 1 < len(tableau) and y + 1 < len(tableau) and tableau[x + 1][y + 1] == 2:
        if x + 2 < len(tableau) and y + 2 < len(tableau) and tableau[x + 2][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y + 2)]
            nbSegment += 1
            check = True
            print("S diagonale bas droite")
    if y - 1 >= 0 and tableau[x][y - 1] == 2:
        if y - 2 >= 0 and tableau[x][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x, y - 2)]
            nbSegment += 1
            check = True
            print("S verticale haut")
    if y + 1 < len(tableau) and tableau[x][y + 1] == 2:
        if y + 2 < len(tableau) and tableau[x][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x, y + 2)]
            nbSegment += 1
            check = True
            print("S verticale bas")
    if x + 1 < len(tableau) and tableau[x + 1][y] == 2:
        if x + 2 < len(tableau) and tableau[x + 2][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y)]
            nbSegment += 1
            check = True
            print("S horizontale droite")
    if x - 1 >= 0 and tableau[x - 1][y] == 2:
        if x - 2 >= 0 and tableau[x - 2][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y)]
            nbSegment += 1
            check = True
            print("S horizontale gauche")
    return points, check, lines


def selectSquareIA(tableau):
    while True:
        x = random.randint(0, len(tableau) - 1)
        y = random.randint(0, len(tableau) - 1)
        if possibleSquareIA(tableau, x, y):
            return x, y


def possibleSquareIA(tableau, x, y):
    if tableau[x][y] == 0:
        return True
    return False


def updateIA(tableau, x, y, joueur, points, lines, nbMot, maxPlayers):
    lettre = random.randint(0, 1)
    if lettre == 0:  # Si clique droit, alors valeur S
        tableau[x][y] = 1
        points, nbMot, lines = updateScoreS(tableau, x, y, points, joueur, lines)
    elif lettre == 1:  # Si clique gauche alors valeur O
        tableau[x][y] = 2
        points, nbMot, lines = updateScoreO(tableau, x, y, points, joueur, lines)
    if not nbMot:
        joueur = inversePlayer(joueur, maxPlayers)
    return tableau, points, joueur, nbMot, lines


def SOS_multi(maxPlayers, board):
    default = [(LONGUEUR * 0.5) - (44 * (len(board) / 2)), HAUTEUR * 0.1]
    while True:
        scores = [0] * maxPlayers
        nbTours, player, mot = 0, 0, False
        lines = [[] * 2 for i in range(8)]
        saveLine = [[] * 2 for i in range(20)]
        while nbTours != len(board) * len(board):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit(0)
            lines = display(ecran, board, scores, mot, lines, player, maxPlayers, default, saveLine)
            i, j, typeMouse = selectSquare(board, default, scores, mot, lines, player, maxPlayers)
            board, scores, player, mot, lines = update(board, i, j, player, scores, lines, typeMouse, mot,
                                                       maxPlayers)
            lines = display(ecran, board, scores, mot, lines, player, maxPlayers, default, saveLine)
            nbTours += 1
        if not displayWinner(scores, maxPlayers):
            break


def SOS_ia(board):
    default = [(LONGUEUR * 0.5) - (44 * (len(board) / 2)), HAUTEUR * 0.1]
    while True:
        maxPlayers = 2
        scores = [0, 0]
        nbTours, player, mot = 0, 0, False
        lines = [[0] * 2 for i in range(8)]
        saveLine = [[] * 2 for i in range(20)]
        while nbTours != len(board) * len(board):
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            lines = display(ecran, board, scores, mot, lines, player, maxPlayers, default, saveLine)
            if player == 0:
                i, j, typeMouse = selectSquare(board, default, scores, mot, lines, player, maxPlayers)
                board, scores, player, mot, lines = update(board, i, j, player, scores, lines, typeMouse, mot,
                                                           maxPlayers)
                lines = display(ecran, board, scores, mot, lines, player, maxPlayers, default, saveLine)
            elif player == 1:
                i, j = selectSquareIA(board)
                board, scores, player, mot, lines = updateIA(board, i, j, player, scores, lines, mot, maxPlayers)
                time.sleep(2)
                lines = display(ecran, board, scores, mot, lines, player, maxPlayers, default, saveLine)
            nbTours += 1
        if not displayWinner(scores, maxPlayers):
            break
