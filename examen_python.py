import random

""""

#Partie 1 - Tri à bulles

myTable = [12, 77, 5, 89, 26]

print("Exercice 1")

print(myTable)

saveVar = myTable[3]
#Ici, on sauv la valeur 89, en place 3

myTable[3] = myTable[1]
#On place la valeur n°1 à l'emplacement n°3

myTable[1] = saveVar

print(myTable)

#On réinitialise
myTable = [12, 77, 5, 89, 26]

print("Exercice 2")

print(myTable)

for i in range(len(myTable)-1):
    if myTable[i] > myTable[i+1]:

        saveVar = myTable[i+1]
        myTable[i+1] = myTable[i]
        myTable[i] = saveVar

print(myTable)

#On réinitialise
myTable = [12, 77, 5, 89, 26]

print("Exercice 3")

print(myTable)

for i in range(len(myTable)-1):
    for n in range(len(myTable)-1):
        if myTable[n] > myTable[n+1]:

            saveVar = myTable[n+1]
            myTable[n+1] = myTable[n]
            myTable[n] = saveVar
        print(myTable)

print(myTable)

#Exercice 4

#Le tri à bulles est considéré comme très lent, car toutes les valeurs du tableau sont analysées au cours de chaque itération des deux boucles insérées dans le code. A l'inverse, les tris par sélection et par insertion ne -
# - ratissent pas l'entièreté du tableau sur toutes les itérations : chaque itération diminue de 1 le nombre de valeurs à comparer. Il est donc logique que le tri à bulles prenne plus de temps, car demandant d'analyser davantage -
# de données. 

# Je ne saurais véritablement donner le temps exact de son exécution. Mais par analogie, si on estimait qu'une itération de boucle pour notre tableau myTable (comprenant donc 5 variables) prendrait 1 secondes, le tri à bulles - 
# - prendrait 125 secondes (5 itérations i x ((5 itérations n x 5 variables) x 1 seconde) = 125 secondes). En comparaison, les tris par sélection ou par insertion prendrait 75 secondes :
# - (5 itérations i x (itérations n -> 5 variables + 4 variables + 3 variables + 2 variables + 1 variables = 15) x 1 seconde = 75 secondes). Le tri à bulle est donc le plus lent.

"""

#Partie 2 - Tic tac toe

vide = " "
symboleJoueurX = "X"
symboleJoueurO = "O"

A1 = vide
A2 = vide
A3 = vide

B1 = vide
B2 = vide
B3 = vide

C1 = vide
C2 = vide
C3 = vide

print(" ")
print(" ", "1", " ", "2", " ", "3")
print("A", A1, "|", A2, "|", A3)
print("  - - - - -")
print("B", B1, "|", B2, "|", B3)
print("  - - - - -")
print("C", C1, "|", C2, "|", C3)
print(" ")

while(True):
    tourJoueurX = True
    
    if(tourJoueurX == True):
        symbole = symboleJoueurX
        joueur = "Joueur 1"
    
    if(tourJoueurX == False):
        symbole = symboleJoueurO
        joueur = "Joueur 2"

    print("C'est au tour du", joueur, "de jouer. Où souhaitez-vous placer votre symbole ? Rentrez le nom de ligne, puis de la colonne, comme ceci : A1, B2, C3, etc...")
    touche = input()

    if(touche == 'A1'):
        A1 = symbole
    elif(touche == 'B1'):
        B1 = symbole
    elif(touche == 'C1'):
        C1 = symbole
    elif(touche == 'A2'):
        A2 = symbole
    elif(touche == 'B2'):
        B2 = symbole
    elif(touche == 'C2'):
        C2 = symbole
    elif(touche == 'A3'):
        A3 = symbole
    elif(touche == 'B3'):
        B3 = symbole
    elif(touche == 'C3'):
        C3 = symbole
    
    while((touche != 'A1') and (touche != 'B1') and (touche != 'C1') and (touche != 'A2') and (touche != 'B2') and (touche != 'C2') and (touche != 'A3') and (touche != 'B3') and (touche != 'C3')):
        print("Merci d'appuyer sur une touche correcte.")
        touche = input()

    print(" ")
    print(" ", "1", " ", "2", " ", "3")
    print("A", A1, "|", A2, "|", A3)
    print("  - - - - -")
    print("B", B1, "|", B2, "|", B3)
    print("  - - - - -")
    print("C", C1, "|", C2, "|", C3)
    print(" ")

    if(tourJoueurX == True):
        tourJoueurX = False
    else:
        tourJoueurX = True

    #Victoires par Lignes

    if((A1 == A2) and (A1 == A3)) and (A1 != vide):
        print("Le Joueur jouant le symbole", A1, "a gagné !")

    if((B1 == B2) and (B1 == B3)) and (B1 != vide):
        print("Le Joueur jouant le symbole", B1, "a gagné !")

    if((C1 == C2) and (C1 == C3)) and (C1 != vide):
        print("Le Joueur jouant le symbole", C1, "a gagné !")

    #Victoires par Colonnes

    if((A1 == B1) and (A1 == C1)) and (A1 != vide):
        print("Le Joueur jouant le symbole", A1, "a gagné !")

    if((A2 == B2) and (A2 == C2)) and (A2 != vide):
        print("Le Joueur jouant le symbole", A2, "a gagné !")

    if((A3 == B3) and (A3 == C3)) and (A3 != vide):
        print("Le Joueur jouant le symbole", A3, "a gagné !")

    #Victoires par Diagonales

    if((A1 == B2) and (A1 == C3)) and (A1 != vide):
        print("Le Joueur jouant le symbole", A1, "a gagné !")

    if((A3 == B2) and (A3 == C1)) and (A3 != vide):
        print("Le Joueur jouant le symbole", A3, "a gagné !")