"""
La liste des courses.
"""
import os
import json

# vérification de l'existence du fichier sur le disque
CURRENT_DIR = os.path.dirname(__file__)
CHEMIN_LISTE = os.path.join(CURRENT_DIR, "course.json")

if os.path.exists(CHEMIN_LISTE):
    with open(CHEMIN_LISTE, "r") as f:  # Pour lire le fichier au début du programme et le fermer
        liste = json.load(f)
else:
    liste = []

choix = ""
option = ""

while True:
    print("Choisissez parmi les 5 options suivantes :")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément de la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter")

    choix = input("👉 Votre choix : ")

    if choix == "1":
        option = input("Entrez le nom d'un élément à ajouter à la liste de course : ").capitalize()
        if option in liste:
            print(f"{option} est déjà dans la liste")
        else:
            liste.append(option)  # ajoute le contenu de la variable option à liste[] -> fichier course.json
            print(f"L'élément '{option}' à bien été ajouter à la liste")

    elif choix == "2":
        option = input("Quel élément voulez-vous retirer de la liste ? : ").capitalize()
        if option in liste:
            liste.remove(option)  # on supprime la valeur de la variable option de la liste
            print(f"L'élément '{option}' à bien été supprimer de la liste")
        else:
            print("L'élément n'est pas présent dans la liste")

    elif choix == "3":
        print("Contenu de votre liste :")
        if not liste:  # si la liste est vide
            print("votre liste est vide")
        else:  # sinon on parcous la liste
            numero = 1
            for i in liste:
                print(f"{numero} -> {i}")
                numero += 1

    elif choix == "4":
        liste.clear()  # fonction .clear() efface totalement une liste
        print("Votre liste à été supprimé")

    elif choix == "5":  # seule possibilité de sortir de la boucle et donc du programme
        # A la fermeture du programme, on sauvegarde la liste dans le fichier course.json
        with open(CHEMIN_LISTE, "w") as f:
            json.dump(liste, f, indent=4, ensure_ascii=False)  # ensure_ascii pour les caractères accentués
        print("A bientôt")
        break

    else:  # si la valeur de la variable choix est différente de 1, 2, 3, 4, 5 -> message d'erreur
        print()
        print("ERREUR : Veuillez faire un choix parmi les 5 options !")
        print()

    print("_" * 50)
