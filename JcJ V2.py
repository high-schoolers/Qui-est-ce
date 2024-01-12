import time #module pour pouvoir utiliser time.sleep()
import csv
from random import*
f=open("personnages.csv")
tab=list(csv.DictReader(f))

def espace (n): #42 pour une page entière
    for i in range (n):
        print('')

def affichage(tab):
    for e in tab:
        print(e)

t1j1=[]#tableau personnes éliminées du j1
t2j1=tab#tableau personnes restantes du j1

t1j2=[]#tableau personnes éliminées du j2
t2j2=tab#tableau personnes restantes du j2

tou=[]
tod=[]

###choix des personnages
print("Voici la liste des personnages: ")
affichage(tab)
tou=tab[int(input("Joueur 1, quel est votre personnage (rentrez un id) ? "))]#personne choisie par j1 = personne que j2 doit chercher
espace(42)
print("Voici la liste des personnages: ")
affichage(tab)
tod=tab[int(input("Joueur 2, quel est votre personnage (rentrez un id) ? "))]#personne choisie par j2 = personne que j1 doit chercher
espace(42)

while len(t2j1)>=1 and len(t2j2)>=1:

###TOUR DU J1
    print("Joueur 1, voici la liste des personnages: ")
    affichage(t2j1)

    if len(t2j1)!=1:
        print("Joueur 1: ")
        a=str(input("catégorie ? ")) #variable catégorie (cheveux,sexe,...)
        b=str(input("caractéristique ? "))#variable caracéristique correspondant à la catégorie (bleus pour les yeux,...)

        if tod["prenom"]==b:
            print("Bravo, Joueur 1 a gagné, c'est : ", tod["prenom"])
            break

        if tod[a]!=b:
            print("Le personnage recherché n'a pas cette caractéristique. ")
            for e in tab:
                if e[a]==b and e["prenom"] not in t1j1:
                    print("on élimine",e["prenom"])
                    t1j1.append(e["prenom"])
            t2j1=[e for e in tab if e["prenom"] not in t1j1]
            print("Il reste: ")
            affichage(t2j1)

        elif tod[a]==b:
            print("Le personnage recherché a cette caractéristique, d'autres ne correspondent donc pas : ")
            for e in tab:
                if e[a]!=b and e["prenom"] not in t1j1:
                    print("On élimine",e["prenom"])
                    t1j1.append(e["prenom"])
            t2j1=[e for e in tab if e["prenom"] not in t1j1]
            print("Il reste:")
            affichage(t2j1)

    if len(t2j1)==1:
        time.sleep(2)
        espace (21)
        print("Bravo, Joueur 1 a gagné, c'est : ", tod["prenom"])
        break

    time.sleep(4)
    espace(42)

###TOUR DU J2
    print("Joueur 2, voici la liste des personnages: ")
    affichage(t2j2)

    if len(t2j2)!=1:
        print("Joueur 2: ")
        a=str(input("catégorie ? ")) #variable catégorie (cheveux,sexe,...)
        b=str(input("caractéristique ? "))#variable caracéristique correspondant à la catégorie (bleus pour les yeux,...)

        if tou["prenom"]==b:
            print("Bravo, c'est : ", tou["prenom"])
            break

        if tou[a]!=b:
            print("Le personnage recherché n'a pas cette caractéristique. ")
            for e in tab:
                if e[a]==b and e["prenom"] not in t1j2:
                    print("on élimine",e["prenom"])
                    t1j2.append(e["prenom"])
            t2j2=[e for e in tab if e["prenom"] not in t1j2]
            print("Il reste: ")
            affichage(t2j2)

        elif tou[a]==b:
            print("Le personnage recherché a cette caractéristique, d'autres ne correspondent donc pas : ")
            for e in tab:
                if e[a]!=b and e["prenom"] not in t1j2:
                    print("On élimine",e["prenom"])
                    t1j2.append(e["prenom"])
            t2j2=[e for e in tab if e["prenom"] not in t1j2]
            print("Il reste:")
            affichage(t2j2)

    if len(t2j2)==1:
        time.sleep(2)
        espace (21)
        print("Bravo, Joueur 2 a gagné, c'est : ", tou["prenom"])
        break

    time.sleep(4)
    espace(42)
