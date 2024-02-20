import time # module pour pouvoir utiliser time.sleep()
import csv
from random import *


def espace(n): # 42 pour une page entière
    """Ajouter des lignes vides
    Paramètres
    ----------
    n : int
        la taille de la ligne vide, l'espace
    """
    for i in range (n):
        print('')

def affichage(tab):
    """Afficher les éléments de tab
    Paramètres
    ----------
    tab : list
        les informations des personnages
    """
    for personnage in tab:
        print(personnage)
        print()

def qui_est_ce():
    """Lance la boucle de jeu du Qui est-ce ?
    Retourne
    --------
    gagnant : int
        le gagnant de la partie
    """
    gagnant = None
    persos = open("personnages.csv")
    tab = list(csv.DictReader(persos)) # les infos des personnages

    elimines1=[]     # tableau personnes éliminées du joueur 1
    restants1=tab    # tableau personnes restantes du joueur 1

    elimines2=[]     # tableau personnes éliminées du joueur 2
    restants2=tab    # tableau personnes restantes du joueur 2

    perso1 = []     # personnage choisi par le joueur 1
    perso2 = []     # personnage choisi par le joueur 2

    ## Choix des personnages
    print("Voici la liste des personnages: ")
    affichage(tab)
    perso1 = tab[int(input("Joueur 1, quel est votre personnage (rentrez un id) ? "))]
    # personne choisie par j1 = personne que j2 doit chercher
    espace(42)
    print("Voici la liste des personnages: ")
    affichage(tab)
    perso2 = tab[int(input("Joueur 2, quel est votre personnage (rentrez un id) ? "))]
    # personne choisie par j2 = personne que j1 doit chercher
    espace(42)

    while len(restants1)>=1 and len(restants2)>=1:

    ###TOUR DU JOUEUR 1
        print("Joueur 1, voici la liste des personnages: ")
        affichage(restants1)

        if len(restants1)!=1:
            print("Joueur 1: ")
            categorie = str(input("Choisissez un catégorie : "))
            # variable catégorie (cheveux,sexe,...)
            caractere = str(input("Choisissez une caractéristique : "))
            # variable caracéristique correspondant à la catégorie
            # (bleus pour les yeux,...)
    
            if perso2["prenom"] == caractere:
                # si j1 entre le bon prénom = il a deviné le perso de j2
                print("Bravo, Joueur 1 a gagné, c'est : ", perso2["prenom"])
                gagnant = 1
                break

            if perso2[categorie] != caractere:
                print("Le personnage recherché n'a pas cette caractéristique. ")
                for personnage in tab:
                    if personnage[categorie] == caractere and personnage["prenom"] not in elimines1:
                        print("On élimine",personnage["prenom"])
                        elimines1.append(personnage["prenom"])
                restants1 = [personnage for personnage in tab if personnage["prenom"] not in elimines1]
                """
                print("Il reste : ")
                affichage(restants1)
                """

            elif perso2[categorie] == caractere:
                print("Le personnage recherché a cette caractéristique, d'autres ne correspondent donc pas : ")
                for personnage in tab:
                    if personnage[categorie] != caractere and personnage["prenom"] not in elimines1:
                        print("On élimine",personnage["prenom"])
                        elimines1.append(personnage["prenom"])
                restants1 = [personnage for personnage in tab if personnage["prenom"] not in elimines1]
                """
                print("Il reste:")
                affichage(restants1)
                """

        if len(restants1) == 1:
            time.sleep(2)
            espace (21)
            print("Bravo, Joueur 1 a gagné, c'est : ", perso2["prenom"])
            gagnant = 1
            break

        time.sleep(4)
        espace(42)

    ###TOUR DU JOUEUR 2
        print("Joueur 2, voici la liste des personnages: ")
        affichage(restants2)

        if len(restants2)!=1:
            print("Joueur 2: ")
            categorie = str(input("catégorie ? "))
            # variable catégorie (cheveux,sexe,...)
            caractere = str(input("caractéristique ? "))
            # variable caracéristique correspondant à la catégorie
            # (bleus pour les yeux,...)

            if perso1["prenom"] == caractere:
                print("Bravo, Joueur 2 a gagné c'est : ", perso1["prenom"])
                gagnant = 2
                break

            if perso1[categorie] != caractere:
                print("Le personnage recherché n'a pas cette caractéristique. ")
                for personnage in tab:
                    if personnage[categorie] == caractere and personnage["prenom"] not in elimines2:
                        print("On élimine",personnage["prenom"])
                        elimines2.append(personnage["prenom"])
                restants2 = [personnage for personnage in tab if personnage["prenom"] not in elimines2]
                """
                print("Il reste: ")
                affichage(restants2)
                """

            elif perso1[categorie] == caractere:
                print("Le personnage recherché a cette caractéristique, d'autres ne correspondent donc pas : ")
                for personnage in tab:
                    if personnage[categorie] != caractere and personnage["prenom"] not in elimines2:
                        print("On élimine",personnage["prenom"])
                        elimines2.append(personnage["prenom"])
                restants2 = [personnage for personnage in tab if personnage["prenom"] not in elimines2]
                """
                print("Il reste:")
                affichage(restants2)
                """

        if len(restants2) == 1:
            time.sleep(2)
            espace (21)
            print("Bravo, Joueur 2 a gagné, c'est : ", perso1["prenom"])
            gagnant = 2
            break

        time.sleep(4)
        espace(42)
        #print(gagnant)
    return gagnant

