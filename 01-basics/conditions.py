#Etape 1
print(10 > 5)     # True
print(3 == 3)     # True
print(4 != 4)     # False
print(7 <= 2)     # False

#Etape 2
age = 20

if age >= 18:
    print("Tu es majeur.")

#Etape 3
age = 15

if age >= 18:
    print("Majeur")
else:
    print("Mineur")

#Etape 4
note = 13

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

#Etape 5
age = 25
a_le_permis = True

if age >= 18 and a_le_permis:
    print("Peut conduire")

#Exercice de base
nombre = int(input("Donner un nombre : "))

if nombre % 2 == 0:
    print("pair")
else:
    print("impair")

#Exercice bonus
age = int(input("Quel est ton âge ? "))

if age < 12:
    print("enfant")
elif age <= 17:
    print("adolescent")
elif age <= 64:
    print("adulte")
else: 
    print("senior")