#Etape 1
notes = [12, 15, 8, 19, 14]

print(notes[0])      # 12  (premier élément, index 0)
print(notes[-1])     # 14  (dernier élément)
print(len(notes))    # 5   (nombre d'éléments)

#Etape 2
notes = [12, 15, 8]
notes.append(19)        # ajoute à la fin
notes[0] = 13           # remplace le premier
print(notes)            # [13, 15, 8, 19]

#Etape 3
notes = [12, 15, 8, 19, 14]

for note in notes:
    print(note)

#Etape 4
notes = [12, 15, 8, 19, 14]
total = 0

for note in notes:
    total = total + note

moyenne = total / len(notes)
print(moyenne)          # 13.6



#Exercice de base
table = [51, -5, 47, 3, 0, 45, 15, -95, 65, 64]

max = table[0]

for elem in table:
    if elem > max:
        max = elem

print(max)  #65

#Exercice bonus
total = 0

for nombre in table:
    total += nombre

moyenne = total / len(table)
print(moyenne)  #19

compteur = 0
for nombre in table:
    if nombre > moyenne:
        compteur += 1

print(compteur) #5