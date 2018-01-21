import sys
import time
import os


def test_positivite(y):
    if y != 0:
        return 1
    else:
        return 0


def listeur_grille(Grille):
    p = 0
    liste = []
    for i in range(0, 9):
        for j in range(0, 9):
            if Grille[i][j] == 0:
                liste.append((i, j))
                p = p + 1
    return liste


def afficher_grille(Grille):
    for p in Grille:
        print(*p, sep=' ')
    return 0


default = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # colonne ou ligne par défaut


def tester_colonne(i, j, Grille):
    col = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for p in list(range(0, i)) + list(range(i + 1, 8)):
        if Grille[p][j] != 0:
            # print('colonne={}'.format(col))
            # print('Grille[i][j]={}'.format(Grille[i][j]))
            # print('i={} j={}'.format(i, j))
            sys.stdout.flush()
            col.remove(Grille[p][j])
    return col


def tester_ligne(i, j, Grille):
    lin = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for p in list(range(0, j)) + list(range(j + 1, 8)):
        if Grille[i][p] != 0:
            # print('ligne={}'.format(lin))
            # print('Grille[i][j]={}'.format(Grille[i][j]))
            # print('i={} j={}'.format(i, j))
            lin.remove(Grille[i][p])
    return lin


def tester_carre(i, j, Grille):
    car = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    range_i = []
    range_j = []

    if (i % 3 == 0):
        range_i = [i, i + 1, i + 2]
    if (i % 3 == 1):
        range_i = [i - 1, i, i + 1]
    if (i % 3 == 2):
        range_i = [i - 2, i - 1, i]

    if (j % 3 == 0):
        range_j = [j, j + 1, j + 2]
    if (j % 3 == 1):
        range_j = [j - 1, j, j + 1]
    if (j % 3 == 2):
        range_j = [j - 2, j - 1, j]

    # print('range_i={}'.format(range_i))
    # print('range_j={}'.format(range_j))

    for m in range_i:
        for p in [x for x in range_j if (x != j or m != i)]:
            if Grille[m][p] != 0:
                # print("Grille[m][p] = {}".format(Grille[m][p]))
                # print (car)
                car.remove(Grille[m][p])

    return car


def list_solution(i, j, Grille):
    col = tester_colonne(i, j, Grille)
    lin = tester_ligne(i, j, Grille)
    car = tester_carre(i, j, Grille)
    # print('col = {} lin = {} car = {}'.format(col, lin, car))
    col = set(col)
    lin = set(lin)
    car = set(car)
    sol = col.intersection(lin, car)
    # print('list = {}'.format(sol))
    # sys.stdout.flush()
    sol = list(sol)
    # print('list = {}'.format(sol))
    # sys.stdout.flush()
    sol.sort
    return sol


Grille = []
Grille.append([0, 5, 4, 1, 0, 0, 8, 9, 0])
Grille.append([0, 0, 8, 4, 5, 0, 0, 6, 3])
Grille.append([0, 9, 0, 0, 8, 0, 5, 1, 0])
Grille.append([4, 0, 0, 0, 7, 0, 1, 0, 0])
Grille.append([8, 0, 0, 6, 0, 1, 0, 0, 5])
Grille.append([0, 0, 1, 0, 4, 0, 0, 0, 7])
Grille.append([0, 7, 5, 0, 6, 0, 0, 8, 0])
Grille.append([9, 8, 0, 0, 1, 4, 3, 0, 0])
Grille.append([0, 4, 6, 0, 0, 7, 2, 5, 0])

# afficher_grille(Grille)
liste_cases = listeur_grille(Grille)
# print(liste_cases)
possibilites = [[default for i in range(9)] for j in range(9)]
compteur = [0 for i in range(len(liste_cases))]
taille = len(liste_cases)
k = 0
t = 0
condition = 0

for i in range(9):
    for j in range(9):
        possibilites[i][j] = [list_solution(i, j, Grille)]


# Début de l'algorithme============================================================
while condition != 81:
    # print('(i,j)={}'.format(liste_cases[k]))
    i = liste_cases[k][0]
    j = liste_cases[k][1]
    possibilites[i][j] = list_solution(i, j, Grille)
    if len(possibilites[i][j]) > 0 + compteur[k] <= len(possibilites[i][j]):
        # print("k = {} , compteur[k] = {}".format(k, compteur[k]))
        # print("k = {}/{} , case {}".format(k, taille, liste_cases[k]))
        # print('possibilités={}'.format(possibilites[i][j]))
        # print(compteur)
        Grille[i][j] = possibilites[i][j][compteur[k]]
        for s in range(k + 1, taille):
            compteur[s] = 0
        # print('possibilité retenue={}'.format(possibilites[i][j][compteur[k]]))
        compteur[k] = compteur[k] + 1
        k = k + 1
        afficher_grille(Grille)
        os.system('clear')
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        # time.sleep(1)
    else:
        # print("/!\ incohérence")
        # print('(i,j)={}'.format(liste_cases[k - 1]))
        i = liste_cases[k - 1][0]
        j = liste_cases[k - 1][1]
        Grille[i][j] = 0
        # print('i={} j={}'.format(i, j))
        # print(liste_cases[k - 1])
        # possibilites[i][j].pop(0)
        # print('possibilités dans le else={}'.format(possibilites[i][j]))
        # print(possibilites)
        k = k - 1

    t = t + 1
    s = [test_positivite(y) for x in Grille for y in x]
    condition = sum(s)
    # print("nombre de cases remplies  = {}/81".format(condition))

print('programme terminé correctment. Résultat : ')
afficher_grille(Grille)
