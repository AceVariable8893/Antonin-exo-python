#Etape 1
client = {
    "prenom": "Lucas",
    "age": 25,
    "ville": "Lyon",
}

print(client["prenom"])     # Lucas
print(client["age"])        # 25

#Etape 2
client = {"prenom": "Lucas"}
client["email"] = "lucas@example.com"   # ajout
client["prenom"] = "Lucas M."           # modification
print(client)

#Etape 3
client = {"prenom": "Lucas", "age": 25, "ville": "Lyon"}

for cle, valeur in client.items():
    print(f"{cle} : {valeur}")

#Etape 4
mots = ["chat", "chien", "chat", "oiseau", "chat"]
compteur = {}

for mot in mots:
    if mot in compteur:
        compteur[mot] = compteur[mot] + 1
    else:
        compteur[mot] = 1

print(compteur)     # {'chat': 3, 'chien': 1, 'oiseau': 1}



#Exercice de base
annuaire = {"Mathilde" : "0754862435", "Esteban" : "0756943285", "Dylan" : "0735129856"}

nom = input("Entrer un nom : ")

if nom in annuaire:
    print(annuaire[nom])
else:
    print("Ce nom n'existe pas")

#Exercice bonus
phrase = input("Entrer une phrase : ")

mots = phrase.split()
compteur = {}

for mot in mots:
    if mot not in compteur:
        compteur[mot] = 1
    else:
        compteur[mot] += 1


for cle, valeur in compteur.items():
    print(f"{cle} : {valeur}")