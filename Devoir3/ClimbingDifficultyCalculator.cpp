// Kanty-Louange Gakima , 20184109
// Marianne schmit Pemmerl, 20192143

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
//#include <unordered_set>
//#include <math.h>
//#include <algorithm>
#include <iostream>

// ce fichier contient les definitions des methodes de la classe ClimbingDifficultyCalculator
// this file contains the definitions of the methods of the ClimbingDifficultyCalculator class

ClimbingDifficultyCalculator::ClimbingDifficultyCalculator()
{
  
}


int ClimbingDifficultyCalculator::minDifficulty(std::vector<std::vector<int> > wall) {
    int rows = wall.size();
    int cols = wall[0].size();

    // Initialisation de la matrice de programmation dynamique
    std::vector<std::vector<int> > dp(rows, std::vector<int>(cols, std::numeric_limits<int>::max()));
    
    //Initialisation de la dernière ligne de la matrice dynamique
    for (int i = 0; i < cols; ++i) {
        dp[rows - 1][i] = wall[rows - 1][i];
    }
    // Calcul des valeurs optimales pour atteindre chaque case en utilisant la programmation dynamique
    for (int i = rows-2; i >=0 ; --i) {
        for (int j = 0; j < cols; ++j) {

            // Choix de la difficulté minimale pour atteindre la case (i,j)
            int updifficulty = dp[i + 1][j];
            int leftDifficulty = (j > 0) ? dp[i ][j - 1] : std::numeric_limits<int>::max();
            int rightDifficulty = (j < cols - 1) ? dp[i ][j + 1] : std::numeric_limits<int>::max();
            dp[i][j] = wall[i][j] + std::min(updifficulty, std::min(leftDifficulty, rightDifficulty));
            
            //Mettre à jour les cases précédentes de la ligne si elles peuvent être optimisées
            for (int k = j; k > 0; --k) {
                if (wall[i][k - 1] + dp[i][k] < dp[i][k - 1]) {
                    dp[i][k - 1] = wall[i][k - 1] + dp[i][k];
                }
                else { break; }
 
            }
        } 
    }

    // Trouver la difficulté minimale dans la première ligne de la matrice dynamique
    int minDiff = *std::min_element(dp[0].begin(), dp[0].end());
    
    return minDiff;
}


int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    // Ouvrir le fichier
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr<< "Impossible d'ouvrir le fichier" << std::endl;
        return -1;
    }

    int m = 0; // Nombre de lignes
    int n = 0; // Nombre de colonnes

    // Lire le fichier pour compter le nombre de lignes et de colonnes
    std::string line;
    while (std::getline(file, line)) {
        ++m;
    if (n == 0) {
        n = std::count(line.begin(), line.end(), ',') + 1;
    }
}

    file.clear();
    file.seekg(0, std::ios::beg);

    std::vector<std::vector<int> > wall(m, std::vector<int>(n));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            char delimiter; // Pour stocker la virgule
            file >> wall[i][j]; // Stockage des données dans la matrice
            // Lecture du délimiteur (virgule) sauf pour le dernier élément de chaque ligne
            if (j < n - 1) {
                file >> delimiter; // Lire la virgule
                if (delimiter != ',') {
                    std::cerr << "Erreur de format dans le fichier." << std::endl;
                    return -1; // Arrêter le programme en cas d'erreur de format
                }
            }
        }
    }

    file.close();
    return minDifficulty(wall);
}
