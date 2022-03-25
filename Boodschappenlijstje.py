Boodschappen = {

}

def BoodschappenVragen():
    global Items
    global Hoeveelheid
    Items = input("Wat zou u op uw boodschappenlijstje willen zetten? ")
    Hoeveelheid = input("Hoevaak zou u dit product willen? ")
    NogMeer = input("Wilt u nog meer bestellen? ").lower()
    if NogMeer == "ja":
        Boodschappen[Items] = Hoeveelheid
        BoodschappenVragen()
    else:
        Boodschappen[Items] = Hoeveelheid
        print(Boodschappen)

BoodschappenVragen()