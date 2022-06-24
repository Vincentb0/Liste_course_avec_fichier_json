"""
La liste des courses.
"""

import json

course = "course.json"

with open(course, "r") as f:  # Pour lire le fichier au début du programme et le fermer
    liste = json.load(f)

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
        else:  # sinon on parcous la liste et affiche les "clés et valeurs" (index et nom)
            for i in liste:
                numero = 1
                print(f"{numero} -> {i}")
                numero += 1

    elif choix == "4":
        liste.clear()  # fonction .clear() efface totalement une liste
        print("Votre liste à été supprimé")

    elif choix == "5":  # seule possibilité de sortir de la boucle et donc du programme
        print("A bientôt")
        # A la fermeture du programme, on sauvegarde la liste dans le fichier course.json
        with open(course, "w") as f:
            json.dump(liste, f, indent=4, ensure_ascii=False)  # ensure_ascii pour les caractères accentués
        break
    else:  # si la valeur de la variable choix est différente de 1, 2, 3, 4, 5 -> message d'erreur
        print()
        print("ERREUR : Veuillez faire un choix parmi les 5 options !")
        print()

    print("_" * 50)
