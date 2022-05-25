import random
from random import shuffle
Opnieuw = True 
Namen = []   
while Opnieuw == True:
    Naam = input("Welke naam wilt u toevoegen? ").lower()
    if Naam in Namen:
        print("Er kan niet 2 keer dezelfde naam worden toegevoegd.")
    else:
        Namen.append(Naam)
    NogEenKeer = input("Wilt u nog een naam toevoegen? ").lower()
    if NogEenKeer == "ja":
        Opnieuw == True
    else:
        Koos = list(Namen)
        Check = True
        while Check == True:
            for i in Namen:
                Kees = random.choice(Koos)
                Koos.remove(Kees)
                print(i,Kees)
            if i == Kees:
                Check = True
            else:
                Check = False


