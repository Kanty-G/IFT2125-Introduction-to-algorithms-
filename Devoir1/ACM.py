#Marianne Schmit Pemmerl, 20192143
#Kanty-Louange Gakima, 20184109

import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies

def read_problems(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    problems = []  # Liste pour stocker les problèmes
    n = int(lines[0])  # Nombre de problèmes dans le fichier
   
    # Parcourir les lignes pour extraire chaque problème
    index = 1  

    for _ in range(n):
        m = int(lines[index])  # Nombre de coordonnées dans le problème
        coordinates = []  # Liste pour stocker les coordonnées du problème
        
        # Parcourir les lignes pour extraire les coordonnées
        for i in range(index + 1, index + m + 1):
            coords = tuple(map(float, lines[i].strip().split()))
            coordinates.append(coords)
        
        problems.append(coordinates)
        index += m + 1 
    return problems

def write(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()


#On a utilisé l'algorithme de Kruskal pour trouver l'arbre couvrant minimal
   
def distance(sommet1, sommet2):
    #formule de la distance euclidenne
    return math.sqrt((sommet1[0]-sommet2[0])**2 + (sommet1[1]-sommet2[1])**2)

#fonction pour trouver le parent
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y): 
    if rank[x] < rank[y]: 
        parent[x] = y 
    elif rank[x] > rank[y]: 
        parent[y] = x 

    else: 
        parent[y] = x 
        rank[x] += 1
 
# Calcul du poids de l'Arbre Couvrant Minimal pour un seul  problème 
def calculate_weight(coordinates):
    v = len(coordinates)  # Nombre de sommets

    # Création  des arêtes
    edges = []
    for i in range(v):
        for j in range(i + 1, v):
            edges.append((i, j, distance(coordinates[i], coordinates[j])))

    # Algorithme de Kruskal pour trouver l'arbre couvrant minimal
    edges.sort(key=lambda x: x[2])  # Trier les arêtes par poids croissant
    parent = [i for i in range(v)]
    rank = [0] * v
    min_weight = 0
    for edge in edges:
        x, y, weight = edge
        x_root = find(parent, x)
        y_root = find(parent, y)
        if x_root != y_root:
            min_weight += weight
            union(parent, rank, x_root, y_root)

    return min_weight


def main(args):
    input_file = args[0]
    output_file = args[1]
    
    problems = read_problems(input_file)

    min_weights = []
    for problem in problems:

        # Calcul du poids de l'ACM pour le problème actuel
        min_weight = calculate_weight(problem)
     
         #Arrondir à trois chiffres après la virgule
        min_weight_rounded = round(min_weight, 3)

        min_weights.append(str(min_weight_rounded))

    write(output_file, '\n'.join(min_weights))

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
