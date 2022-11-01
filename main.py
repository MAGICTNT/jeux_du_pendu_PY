
def jeux_du_pendu():
    choix = [ "contrebandier", "pourrir", "grosse", "dix", "apiculteur", "dynamitage", "horloge", "bombe", "brut", "biberonner", "bizarre", "ceinture", "reine", "concept", "crier", "toxique", "avantage"]
    solution = nouveauMotMyster(choix)
    choix.remove(solution)
    point = 3
    tentatives = 6
    bonne_reponse = 0
    affichage = ""
    lettres_trouvees = ""

    messageDebut()
    getionJeux(affichage, lettres_trouvees, point, bonne_reponse, solution, tentatives, choix)
    messageFin()


def nouveauMotMyster(choix):
    import random
    nouveau_mot = random.choice(choix)
    return nouveau_mot


def messageDebut():
    print("*---------------------------*")
    print("|                           |")
    print("|  Jeux du pendu en Python  |")
    print("|                           |")
    print("*---------------------------*")


def messageFin():
    print("*---------------------------*")
    print("|                           |")
    print("|     Fin de la partie      |")
    print("|                           |")
    print("*---------------------------*")


def getionJeux(affichage, lettres_trouvees, point, bonne_reponse, solution, tentatives, choix):
    affichage = generation_mot_cacher(affichage, solution)
    while point > 0 and bonne_reponse < 3:
        print("\nMot à deviner : ", affichage)
        proposition = input("proposez votre lettre : ")[0:1].lower()

        lettres_trouvees, tentatives = actualisationPendu(lettres_trouvees, proposition, solution, tentatives, point)
        affichage = actualisationAffichage(affichage, lettres_trouvees, solution)

        if tentatives == 0:
            affichage, lettres_trouvees, point, solution, tentatives = actualisation_mot_perdu(affichage, choix,
                                                                                               lettres_trouvees, point,
                                                                                               solution, tentatives)

        if "_" not in affichage:
            affichage, bonne_reponse, lettres_trouvees, solution, tentatives = actualisation_mot_trouver(affichage,
                                                                                                         bonne_reponse,
                                                                                                         choix,
                                                                                                         lettres_trouvees,
                                                                                                         point,
                                                                                                         solution,
                                                                                                         tentatives)

    if bonne_reponse == 3:
        print("Bravo, vous avez gagnez")
    else:
        print("Dommage, vous avez perdu")


def actualisation_mot_trouver(affichage, bonne_reponse, choix, lettres_trouvees, point, solution, tentatives):
    tentatives = 6
    bonne_reponse += 1
    print("\nBravo vous avez trouvez le mot ", solution, "\nIl vous reste ", point, "pts")
    solution = nouveauMotMyster(choix)
    choix.remove(solution)
    score(point)
    lettres_trouvees = ""
    affichage = generation_mot_cacher(affichage, solution)
    return affichage, bonne_reponse, lettres_trouvees, solution, tentatives


def actualisation_mot_perdu(affichage, choix, lettres_trouvees, point, solution, tentatives):
    tentatives = 6
    point -= 1
    print("\nPerdu, vous deviez trouver le mot ", solution, "\nIl vous reste ", point, "pts")
    solution = nouveauMotMyster(choix)
    choix.remove(solution)
    lettres_trouvees = ""
    affichage = generation_mot_cacher(affichage, solution)
    return affichage, lettres_trouvees, point, solution, tentatives


def generation_mot_cacher(affichage, solution):
    affichage = ""
    for l in solution:
        affichage = affichage + "_ "
    return affichage


def actualisationPendu(lettres_trouvees, proposition, solution, tentatives, point):
    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("Lettre trouver")
    else:
        tentatives = tentatives - 1
        print("Pas la bonne lettre")
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")

    return lettres_trouvees, tentatives


def actualisationAffichage(affichage, lettres_trouvees, solution):
    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "
    return affichage


def score(point):
    print("Il vous reste :", point)

if __name__ == '__main__':
    jeux_du_pendu()
