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
    '''if choix == 4:
        if chargement() != -1:
            players, scores, saveLine, tableau = chargement()'''
