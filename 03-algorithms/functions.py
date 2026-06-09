#Etape 1
def dire_bonjour(prenom):
    print(f"Bonjour {prenom} !")

dire_bonjour("Emma")
dire_bonjour("Hugo")

#Etape 2
def carre(n):
    return n * n

resultat = carre(5)
print(resultat)     # 25

#Etape 3
def puissance(base, exposant=2):
    return base ** exposant

print(puissance(3))        # 9   (exposant par défaut = 2)
print(puissance(2, 10))    # 1024

#Etape 4
def est_pair(n):
    return n % 2 == 0

def moyenne(liste):
    return sum(liste) / len(liste)

print(est_pair(4))             # True
print(moyenne([10, 20, 30]))   # 20.0



#Exercice de base
def est_pair(n):
    return n % 2 == 0

#Exercice bonus
def moyenne(liste):
    total = 0

    for nombre in liste:
        total = total + nombre

    return total / len(liste)

print(f"La moyenne est : {moyenne([10, 20, 30])}")   # → La moyenne est : 20.0