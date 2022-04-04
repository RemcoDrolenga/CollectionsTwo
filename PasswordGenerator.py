import random 
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"]
Hoofdletters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]
Symbolen = ["@","#","$","%","&","_","?"]
Getallen = ["1","2","3","4","5","6","7","8","9"]
Lijst1 = []
Lijst2 = []
Lijst3 = []

RandomGetalHoofdLetters = random.randint(2,6)
RandomGetalCijfers = random.randint(4,7)
GetalGetallen = 24
GetalLetters = GetalGetallen - RandomGetalHoofdLetters - RandomGetalCijfers - 3 
RandomHoofdletter = random.choices(Hoofdletters, k=RandomGetalHoofdLetters)
RandomLetter = random.choices(Letters, k=GetalLetters)
RandomSymbolen = random.choices(Symbolen, k=3)
RandomGetallen = random.choices(Getallen, k=RandomGetalCijfers )
Lijst2.extend(RandomLetter)
Lijst2.extend(RandomHoofdletter)
for i in range(3):
    Lijst1.append(Lijst2[0])
    bal = Lijst2[0]
    Lijst2.remove(bal)
Lijst3.append(Lijst2[0])
Nee = Lijst2[0]
Lijst2.remove(Nee)
Lijst2.extend(RandomSymbolen)
Lijst2.extend(RandomGetallen)
random.shuffle(Lijst2)
Lijst1.extend(Lijst2)
Lijst1.extend(Lijst3)
print(Lijst1)
