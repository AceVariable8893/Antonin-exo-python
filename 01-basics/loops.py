#Etape 1
for i in range(5):
    print(i)        # affiche 0, 1, 2, 3, 4

#Etape 2
for prenom in ["Emma", "Hugo", "Chloé"]:
    print(f"Bonjour {prenom}")

#Etape 3
total = 0

for i in range(1, 11):
    total = total + i

print(total)        # 55

#Etape 4
compteur = 3

while compteur > 0:
    print(compteur)
    compteur = compteur - 1

print("Décollage !")



#Exercice de base
nombre = int(input("Choisi un nombre : "))

for i in range(1, nombre+1):
    print(i)

#Exercice bonus
nombre = int(input("Choisi un nombre : "))

for i in range(1, 11):
    print(i * nombre)