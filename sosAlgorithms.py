def new_board():
    while True:
        try:
            n = int(input("Dimension : "))
            if n > 2:
                break
            print("Un nombre supérieur à 2 !")
        except ValueError:
            print("Un nombre !")
    tableau = [[0] * n for i in range(n)]
    return tableau, n


def display(tableau, a):
    print("C'est le tour du joueur ", player + 1)
    for y in range(a):
        for x in range(a):
            print(tableau[x][y], end="    ")
        print("\n")


def inversePlayer(player):
    if player == 1:
        return 0
    return 1


def selectSquare(tableau, n):
    while True:
        try:
            x = int(input("Abscisse : ")) - 1
            y = int(input("Ordonnée  : ")) - 1
            if possibleSquare(tableau, x, y, n):
                return x, y
        except ValueError:
            print("Un nombre !")


def possibleSquare(tableau, x, y, n):
    if 0 <= x < n and 0 <= y < n:
            if tableau[x][y] == 0:
                return True
    print("La case n'existe pas ou est déjà prise !")
    return False


def update(tableau, n, x, y, joueur, points):
    lines = [[0] * 2 for i in range(8)]
    while True:
        print("Quelle lettre voulez poser aux coordonnées x = ", x + 1, " et y = ", y + 1, end=" : ")
        choice = input().upper()
        print("\n")
        if choice == "S":
            tableau[x][y] = 1
            points, nbMot = updateScoreS(board, n, x, y, points, joueur, lines)
            break
        elif choice == "O":
            tableau[x][y] = 2
            points, nbMot = updateScoreO(board, n, x, y, points, joueur, lines)
            break
    if nbMot == 0:
        joueur = inversePlayer(player)
    return tableau, points, joueur


def updateScoreO(tableau, n, x, y, points, joueur, lines):
    # On vérifie SOS en diagonale (on cherche les 2 S autour de O)
    nbSegment = 0
    if x - 1 >= 0 and y - 1 >= 0 and tableau[x - 1][y - 1] == 1:  # On vérifie si on a SOS en diagonale
        if x + 1 < n and y + 1 < n and tableau[x + 1][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x - 1, y - 1), (x + 1, y + 1)]
            nbSegment += 1
            print("O diagonale")
    if x + 1 < n and y - 1 >= 0 and tableau[x + 1][y - 1] == 1:  # On vérifie si on a SOS en diagonale
        if x - 1 >= 0 and y + 1 < n and tableau[x - 1][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x + 1, y - 1), (x - 1, y + 1)]
            nbSegment += 1
            print("O diagonale")
    if y - 1 >= 0 and tableau[x][y - 1] == 1:  # On vérifie si on a SOS en verticale
        if y + 1 < n and tableau[x][y + 1] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y - 1), (x, y + 1)]
            nbSegment += 1
            print("O verticale")
    if x + 1 < n and tableau[x + 1][y] == 1:  # On vérifie si on a SOS en horizontale
        if x - 1 >= 0 and tableau[x - 1][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x + 1, y), (x - 1, y)]
            print("O horizontale")
    print(points)
    print(lines)
    return points, nbSegment


def updateScoreS(tableau, n, x, y, points, joueur, lines):
    nbSegment = 0
    if x - 1 >= 0 and y - 1 >= 0 and tableau[x - 1][y - 1] == 2:
        if x - 2 >= 0 and y - 2 >= 0 and tableau[x - 2][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y - 2)]
            nbSegment += 1
            print("S diagonale haut gauche")
    if x + 1 < n and y - 1 >= 0 and tableau[x + 1][y - 1] == 2:
        if x + 2 < n and y - 2 >= 0 and tableau[x + 2][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y - 2)]
            nbSegment += 1
            print("S diagonale haut droite")
    if x - 1 >= 0 and y + 1 < n and tableau[x - 1][y + 1] == 2:
        if x - 2 >= 0 and y + 2 < n and tableau[x - 2][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y + 2)]
            nbSegment += 1
            print("S diagonale bas gauche")
    if x + 1 < n and y + 1 < n and tableau[x + 1][y + 1] == 2:
        if x + 2 < n and y + 2 < n and tableau[x + 2][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y + 2)]
            nbSegment += 1
            print("S diagonale bas droite")
    if y - 1 >= 0 and tableau[x][y - 1] == 2:
        if y - 2 >= 0 and tableau[x][y - 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x, y - 2)]
            nbSegment += 1
            print("S verticale haut")
    if y + 1 < n and tableau[x][y + 1] == 2:
        if y + 2 < n and tableau[x][y + 2] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x, y + 2)]
            nbSegment += 1
            print("S verticale bas")
    if x + 1 < n and tableau[x + 1][y] == 2:
        if x + 2 < n and tableau[x + 2][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x + 2, y)]
            nbSegment += 1
            print("S horizontale droite")
    if x - 1 >= 0 and tableau[x - 1][y] == 2:
        if x - 2 >= 0 and tableau[x - 2][y] == 1:
            points[joueur] += 1
            lines[nbSegment] = [(x, y), (x - 2, y)]
            nbSegment += 1
            print("S horizontale gauche")
    print(points)
    print(lines)
    return points, nbSegment


def winner(scores):
    if scores[0] > scores[1]:
        print("Le gagnant est le joueur 1 !")
    elif scores[0] < scores[1]:
        print("Le gagnant est le joueur 2 !")
    else:
        print("Egalité !")


board, n = new_board()
player = 0
scores = [0, 0]
nbTours = 0
while nbTours != n * n:
    display(board, n)
    i, j = selectSquare(board, n)
    board, scores, player = update(board, n, i, j, player, scores)
    nbTours += 1
print("Le score est de ", scores[0], "-", scores[1])
winner(scores)
