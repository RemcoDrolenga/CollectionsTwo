import random
Kleuren = ["harten","klaveren","Schoppen","Ruiten"]
Kaarten = ["1","2","3","4","5","6","7","8","9","10","Boer","vrouw","Heer","Aas"]
NieuweKaarten = ["joker","joker"]
RandomKaarten = []
for i in Kleuren:
    for x in Kaarten:
        NieuweKaarten.append(i + x)
random.shuffle(NieuweKaarten)
for i in range(7):
    KaartenRandom = random.choice(NieuweKaarten)
    RandomKaarten.append(KaartenRandom)
    NieuweKaarten.remove(KaartenRandom)
for i in range(len(RandomKaarten)):
    print(RandomKaarten[i])
print("")
print(NieuweKaarten)
