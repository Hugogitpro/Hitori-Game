from sosAlgorithms2 import*

while True:
    choix = menu(ecran)
    if choix == 1:
        board = new_Board(ecran)
        SOS_multi(2, board)
    if choix == 2:
        board = new_Board(ecran)
        SOS_multi(nbJoueurs(ecran), board)
    if choix == 3:
        board = new_Board(ecran)
        SOS_ia(board)
    if choix == 4:
        if download() != -1:
            mode, maxPlayers, players, scores, saveLine, tableau = download()
            if mode == 0:
                SOS_ia(tableau, maxPlayers, players, saveLine, scores)
            else:
                SOS_multi(maxPlayers, tableau, players, saveLine, scores)
