# Nom, Matricule
# Nom, Matricule

#référence : https://www.geeksforgeeks.org/depth-first-traversal-dfs-on-a-2d-array/

import sys

def read_problem(MyGraph, input_file="input.txt"):
    """Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
    faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
    d'autres librairies.
    Functions to read/write in files. you can modify them, do some parsing,
    add a return value, but don't use other librairies"""

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    height, width = map(int, lines[0].split())
    
    grid= []

    for line in lines[1:]:
        row = [int(char) for char in line.strip()]
        grid.append(row)

    return height, width, grid


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

def checkAdjacent(row, col, grid, visited, height, width):

    directions = [(0,1), (0,-1), (1,0), (-1,0)] #right, left, down, up
    adjacents = []

    for d_row, d_col in directions:
        adj_row, adj_col = row + d_row, col + d_col
        #check if adjacent cell is within grid bounds, is part of aquifer and hasnt been visited 
        if 0 <= adj_row < height and 0 <= adj_col < width and grid[adj_row][adj_col] == 1 and not visited[adj_row][adj_col]:
            adjacents.append((adj_row, adj_col))
    return adjacents
    
def find_largest_aquifer(problem):

    height, width, grid = problem

    visited = [[False for _ in range(width)] for _ in range(height)]
    max_aquifer_size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)] # Initialize stack with the starting cell
                aquifer_size = 0

                #DFS traversal
                while stack:
                    row, col = stack.pop()
                    if not visited[row][col]:
                        visited[row][col] = True
                        aquifer_size += 1

                        #Use checkAdjacent to find and append adjacent cells
                        adjacents = checkAdjacent(row, col, grid, visited, height, width)
                        for adj in adjacents:
                            stack.append(adj)

                max_aquifer_size = max(max_aquifer_size, aquifer_size)

    return max_aquifer_size

def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    problem = read_problem("", input_file)
    answer = find_largest_aquifer(problem)

    # answering
    write(output_file, str(answer))

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])