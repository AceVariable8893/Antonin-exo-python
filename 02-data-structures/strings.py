#Etape 1
mot = "Python"

print(mot[0])       # P
print(mot[-1])      # n
print(mot[0:3])     # Pyt   (slicing : du 0 au 3 exclu)
print(len(mot))     # 6

#Etape 2
texte = "  Bonjour le Monde  "

print(texte.strip())         # "Bonjour le Monde"  (enlève les espaces)
print(texte.lower())         # "  bonjour le monde  "
print(texte.replace("o", "0"))

#Etape 3
phrase = "Emma,Hugo,Chloé"
prenoms = phrase.split(",")
print(prenoms)              # ['Emma', 'Hugo', 'Chloé']

#Etape 4
mot = "banane"
compteur = 0

for lettre in mot:
    if lettre == "a":
        compteur = compteur + 1

print(compteur)             # 2



#Exercice de base
mot = input("Entrer un mot : ")

nb_voyelle = 0

for lettre in mot:
    if lettre in "aeiouy":
        nb_voyelle += 1

print(nb_voyelle)

#Exercice bonus
phrase = input("Entrer une phrase : ")

mots = phrase.split()

mot_long = len(mots[0]) 
indice_mot_long = 0

for i in range(len(mots)):
    longueur_mot = len(mots[i])
    if longueur_mot > mot_long:
        mot_long = longueur_mot
        indice_mot_long = i

print(mots[indice_mot_long])