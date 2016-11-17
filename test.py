#!/usr/bin/python3

# comentaire
import sys

print(sys.version_info)
print(sys.version)

print(sys.platform)

print("Hello")
print('Hello')
print("c'est")
print(""" text

        a la suite""")
print("c'est le texte dans C:\\user")

strAdresse = "Spam"
print(strAdresse)

a = ['a','b','c','d','e','f','g','h']

print(a[:4]) # les 4 premiers caractères
print(a[-4:]) # les 4 derniers caractères
print(a[3:-3]) # les 2 caractères de milieu

i = 5.22222
mykey = "temps"
fois = 20
print('la valeur %0.1f et le mot \'%s\' apparaiseent %d fois.' %(i,mykey,fois))#format les chaines
print('la valeur {} et le mot \'{}\' apparaiseent {} fois'.format(i,mykey,fois))

valeur = "dog"
if valeur == "cat" :
    print ("ok")
elif valeur == "dog" :
    print("dog ok")
else:
    print("inconnu")

valeur = "toto"
valeur2= "titi"
if valeur == "toto" and valeur2 == "titi" :
    print("ok")

seq = [1,2,3,"spam"]
a,b,c,d  = seq
print(a,b,c,d)


for letter in "Spam" :
    print("current letter ", letter)

fruits = ['banane','pomme','mangue']
for fruit in fruits:
    print("mon fruit", fruit)

for num in range(1,4):
    if  num == 2:
        continue
    if num == 3:
        break
    print(num)

var = 10
while True:
    var -=1
    if var == 6:
        continue
    print(var)
    if var == 0:
        break
print("end loop")

a = [1,2,3,4,5,6,7,8,9,10]
a = "spam"
squares = [x.capitalize() for x in a]
print(squares)

# on a deux variables temps et distance
temps= 6.896
distance=19.7
#affiché la vitese

vitesse= distance / temps
print("la vitesse est = {:.2f} metre par seconde" .format(vitesse))

#en utilisant la fonction range
# afficher les entiers de 0 a 3"
for intier in range(0,4):
    print(intier)
# autre afficher de 4 a 7
for intier in range(0,10):
    if intier > 3:
        print("   ",intier)
    if intier==7:
        break
# avec une double for afficher les caracteres de la chaine suivante
msg= "c'est la formation DevOps"
for c in msg:
    print(c)

"""caracteres = [c for c in msg]
print(caracteres)"""

# sur la liste suivante faire les actions suivantes
liste = [17,38,10,25,72]
# triez et affichez la liste
liste.sort()
print(liste)
# ajouter l'element 12 et afficher la liste
liste.append(12)
print(liste)
# affichez l'indice de l'element 17
indice = liste.index(17)
print(indice)

"""int = 0
for element in liste:
    if element==17:
        print(int)
    int+=1"""
# enlevez l'element 38 et afficher la liste
print(liste)
liste.remove(38) #seulement enleve le premier 38 de la liste
print(liste)
# afficher la sous-liste du 3eme element jusqu'a la fin de la liste
sousListe = liste[2:]
print(sousListe)
