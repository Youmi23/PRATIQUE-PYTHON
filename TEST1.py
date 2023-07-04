#EXERCICE1
def bissextile(an):
    if an % 4 == 0:
        if an % 100 == 0:
            if an % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

an = int(input("Entrez une année : "))
if bissextile(an):
    print("L'année est bissextile.")
else:
    print("L'année n'est pas bissextile.")

#EXERCICE2
import random

def lancer_deux_des():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    somme = d1 + d2
    return somme

resultat = lancer_deux_des()
print("Le résultat du lancer de deux dés est :", resultat)

import random

def lancer_des(nombre_des):
    somme = 0
    for _ in range(nombre_des):
        d = random.randint(1, 6)
        somme += d
    return somme

resultat = lancer_des(2)
print("Résultat du lancer de deux dés :", resultat)

resultat = lancer_des(3)
print("Résultat du lancer de trois dés :", resultat)

#EXERCICE3
def suite_carres(n):
    for i in range(n+1):
        carre = i ** 2
        print(carre, end="")
        if i != n:
            print("_", end="")
    print("")

entier = int(input("Entrez un entier n : "))
suite_carres(entier)

#EXERCICE4
def produit(n1, n2):
    prod8 = 1
    for i in range(n1, n2 + 1):
        prod8 *= i
    return prod8

n1 = int(input("Entrez un entier : "))
n2 =int(input("Entrez un entier : "))
resultat = produit(n1, n2)
print("Le produit des entiers de", n1, "à", n2, "est :", resultat)

#EXERCICE5
def nbPairImpair():
    taille = int(input("Entrez la taille du tableau : "))
    tableau = []
    for i in range(taille):
        element = int(input("Entrez l'élément à l'indice {}: ".format(i)))
        tableau.append(element)
    
    nb_pair = 0
    nb_impair = 0
    for element in tableau:
        if element % 2 == 0:
            nb_pair += 1
        else:
            nb_impair += 1
    
    return nb_pair, nb_impair

pair, impair = nbPairImpair()
print("Nombre d'éléments pairs :", pair)
print("Nombre d'éléments impairs :", impair)
#EXERCICE6
def decaleCircDroite(tableau):
    dernier_element = tableau[-1]
    for i in range(len(tableau) - 1, 0, -1):
        tableau[i] = tableau[i - 1]
    tableau[0] = dernier_element
    return tableau
taille = int(input("Entrez la taille du tableau : "))
mon_tableau = []
for i in range(taille):
    element = int(input("Entrez l'élément à l'indice {}: ".format(i)))
    mon_tableau.append(element)

print("Avant décalage circulaire à droite :", mon_tableau)
mon_tableau = decaleCircDroite(mon_tableau)
print("Après décalage circulaire à droite :", mon_tableau)

#EXERCICE7
#EXO 7.1
def bin2Dec(nBin):
    nDec = int(nBin, 2)
    return nDec

nBin = input("Entrez la représentation binaire d'un nombre : ")
nDec = bin2Dec(nBin)
print("Le nombre binaire (codage entier naturel)", nBin, "se convertit en base 10 :", nDec)


#EXERCICE8
def somme(n):
    if n == 1:
        return 1
    else:
        return n + somme(n - 1)

# Demander à l'utilisateur de fournir la valeur de n
n = int(input("Entrez un entier : "))

# Appeler la fonction récursive pour calculer la somme
somme = somme(n)

# Afficher le résultat
print("La somme des", n, "premiers entiers est :", somme)


#EXERCICE9
def puissance(x, n):
    if n == 0:
        return 1
    else:
        return x * puissance(x, n - 1)

# Demander à l'utilisateur de fournir les valeurs de x et n
x = int(input("Entrez la valeur de x : "))
n = int(input("Entrez la valeur de n : "))

# Appeler la fonction récursive pour calculer x^n
resultat = puissance(x, n)

# Afficher le résultat
print(x, "à la puissance", n, "égal à :", resultat)


#EXERCICE10
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Demander à l'utilisateur de fournir la valeur de n
n = int(input("Entrez un entier : "))

# Appeler la fonction récursive pour calculer le nième terme de Fibonacci
resultat = fibonacci(n)

# Afficher le résultat
print("Le terme de Fibonacci à l'indice", n, "est :", resultat)


#EXERCICE11
chiffres = list(range(1, 11))
resultat = ';'.join(map(str, chiffres))
print(resultat)

#EXERCICE12
import random

# Fonction pour échanger deux valeurs dans un tableau
def echanger(tableau, indice1, indice2):
    tableau[indice1], tableau[indice2] = tableau[indice2], tableau[indice1]

# Création du tableau avec des chiffres aléatoires entre 1 et 100
chiffres = [random.randint(1, 100) for _ in range(10)]

#La méthode du tri à bulles
n = len(chiffres)
tri_effectue = False
while not tri_effectue:
    tri_effectue = True
    for i in range(n-1):
        if chiffres[i] > chiffres[i+1]:
            echanger(chiffres, i, i+1)
            tri_effectue = False

# Affichage des valeurs séparées par une virgule
resultat = ', '.join(map(str, chiffres))
print(resultat)

#EXERCICE13

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)

# Calcul de la factorielle 
n =int(input("Entrez un entier n : "))
resultat = factorielle(n)

# Affichage du résultat
print("La factorielle de", n, "est :", resultat)

#EXERCICE14
import random

def phrase(mots):
    random.shuffle(mots)
    phrase = ' '.join(mots)
    print(phrase)

# Exemple d'utilisation
mots = ['Niska', 'est', 'le', 'meilleur', 'rappeur', 'de', 'France']
phrase(mots)
