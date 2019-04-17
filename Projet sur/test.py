try:
    fichier = open("texte.json","r")
except:
    print("error opening")
'''import json

# On veut enregistrer saveLine, scores, player, tableau
fichier = open('texte.json', "w")
player = 2
scores = [2, 6]
tab = [[2]*5 for i in range(5)]
fichier.write(str(player))
fichier.write("\n")
fichier.write(json.dumps(scores))
fichier.write("\n")
fichier.write(json.dumps(tab))
fichier.close()

fichier = open('texte.json', "r")
joueur = int(fichier.readline())
scores = json.loads(fichier.readline())
tableau = json.loads(fichier.readline())
fichier.close()

fichier = open("texte.json","r")
print(fichier.readline())
# On récupère notre tableau sauvegardé
tableau = json.loads(lignes)'''
