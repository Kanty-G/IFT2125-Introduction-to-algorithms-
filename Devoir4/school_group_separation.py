#Marianne Schmit Pemmerl, 
#Kanty-Louange Gakima, 20184109

import sys

#Fonction pour lire le fichier d'input. Vous ne deviez pas avoir besoin de la modifier.
#Retourne la liste des noms d'étudiants (students) et la liste des paires qui ne peuvent
#doivent pas être mis dans le même groupe (pairs)
#
#Function to read the input file. You shouldn't have to modify it.
#Returns the list of student names (students) and the list of pairs of students that
#shouldn't be put in the same group (pairs)
def read(fileName):
    # lecture du fichier
    fileIn = open(fileName,"r")
    linesIn = fileIn.readlines()
    fileIn.close()

    nbStudents = int(linesIn[0])
    students = []
    if(nbStudents != 0):
        students = [s.strip() for s in linesIn[1:nbStudents+1]]
    nbPairs = int(linesIn[nbStudents+1])
    pairs = []
    if(nbPairs != 0):
        pairs = [s.strip().split() for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

    return students, pairs


#Fonction qui écrit dans le fichier d'output. 
#le paramètre content est un string
#
#Function that writes in the output file.
#The content parameter is a string
def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()

#Fonction principale à compléter.
#students : liste des noms des étudiants
#pairs : liste des paires d'étudiants à ne pas grouper ensemble
#        chaque paire est sous format de liste [x, y]
#Valeur de retour : string contenant la réponse. Si c'est impossible, retourner "impossible"
#                   Sinon, retourner en un string les deux lignes représentant les
#                   les deux groupes d'étudants (les étudiants sont séparés par des
#                   espaces et les deux lignes séparées par un \n)
#
#Function to complete
#students : list of student names
#pairs : list of pairs of students that shouldn't be grouped together.
#        each pair is given as a list [x, y]
#Return value : string with the output. If it is impossible, return "impossible".
#               otherwise, return in a single string both ouput lines that contain
#               two groups (students are separated by spaces and the two lines by a \n)
def createGroups(students, pairs):
    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

    #on a utilisé l'algorithme de BFS pour résoudre ce problème

    if len(students) == 0:
        return "impossible"
    #graphe non orienté ou chaque étudiant est un noeud et chaque paire est une arête
    graph = {student: [] for student in students}
    for x, y in pairs:
        graph[x].append(y)
        graph[y].append(x)

    #dictionnaire pour stocker les couleurs des noeuds   
    colors ={}

    #file pour le parcours en largeur(BFS)
    queue = []

    for student in students:
        if student not in colors:
            #Affecter une couleur 0 au premier noeud découvert
            colors[student] = 0
            queue.append(student)

            #parcourir les noeuds de la file
            while queue:
                currrent_student  = queue.pop(0)
                #parcourir les voisins du noeud courant
                for neighbor in graph[currrent_student]:
                    if neighbor not in colors:
                        #si le voisin n'a pas de couleur, on lui affecte une couleur différente de celle du noeud courant
                        colors[neighbor] = 1 - colors[currrent_student]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[currrent_student]:
                        return "impossible"

    group1 = [student for student in students if colors[student] == 0]
    group2 = [student for student in students if colors[student] == 1]

    return " ".join(group1) + "\n" + " ".join(group2)


#Normalement, vous ne devriez pas avoir à modifier
#Normaly, you shouldn't need to modify
def main(args):
    input_file = args[0]
    output_file = args[1]
    students, pairs = read(input_file)
    output = createGroups(students, pairs)
    write(output_file, output)
            

#Ne pas changer
#Don't change
if __name__ == '__main__':
    main(sys.argv[1:])