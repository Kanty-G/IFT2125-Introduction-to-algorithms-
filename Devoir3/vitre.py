#Kanty-Louange Gakima, matricule
#Marianne Schmit Pemmerl, 20192143

#Fonction à compléter. Ne modifiez pas sa signature.
#N : Force maximale
#k : Nombre de fenêtres disponibles
#Valeur de retour : le nombre minimal de tests qu'il faut faire 
#                   en pire cas pour déterminer le seuil de solidité 
#                   d'une fenêtre
#Doit retourner la réponse comme un int.
#
#Function to complete. Do not change its signature.
#N : Maximum force
#k : Number of windows available
#return value : Minimum number of tests needed in the worst case
#               to find the solidity threshold of a window
#Must return the answer as an int. 
#source: https://brilliant.org/wiki/egg-dropping/

import sys
def vitre(N, k):
    # Initialisation de la table dp avec infini 
    dp = [[float('inf') for x in range (N + 1)] for x in range(k + 1)]
    
    # Cas de base test de forces et vitres
    for i in range(1, k + 1):
        dp[i][0] = 0  #Aucune force à tester
        dp[i][1] = 1  #Une seule force à tester donc un seul test
        if(N>=2):
            dp[i][2] = 1 #Pas bsn de tester x=2 car si s = 2 le lancé x=1 le detectera puisque la fenetre ne se serait pas cassée
    for j in range(N + 1):
        dp[0][j] = 0
        dp[1][j] = j-1  #Avec une seule vitre, on va tester chaque force-1
    
    # Remplissage de la table dp pour les cas où k > 1 et N > 2
    for i in range(2, k + 1):  # Pour chaque nombre de fenêtres disponibles
        for j in range(3, N + 1):  # Pour chaque niveau de force à tester
            for x in range(1, j):  # Tester chaque niveau de force  
                nombre_de_tests = 1 + max(dp[i-1][x], dp[i][j-x]) #1 test + le pire cas entre casser et ne pas casser la fenêtre
                dp[i][j] = min(dp[i][j], nombre_de_tests)
    return dp[k][N]

#Fonction main, vous ne devriez pas avoir à modifier
#Main function, you shouldn't have to modify it
def main(args):
    N = int(args[0])
    k = int(args[1])

    answer = vitre(N,k)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])
