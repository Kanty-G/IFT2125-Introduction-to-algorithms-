//Kanty-Louange Gakima, 20184109
//Marianne Schmit Pemmerl, 20192143 

#include "PrimeCalculator.h"
#include <vector>
#include <math.h>

// ce fichier contient les definitions des methodes de la classe PrimeCalculator
// this file contains the definitions of the methods of the PrimeCalculator class


PrimeCalculator::PrimeCalculator()
{
}


//fonction qui verifie si un nombre est premier
bool PrimeCalculator:: isPrime(int k){

    if (k <= 1)
        return false;
    if (k <= 3)
        return true;

    if (k % 2 == 0 || k % 3 == 0)
        return false;

    for (int i = 5; i * i <= k; i += 6) {
        if (k % i == 0 || k % (i + 2) == 0)
            return false;
    }

    return true; 
}

int PrimeCalculator::CalculateNthPrime(int N)
{
    int count = 0;
    int num = 2;
    while (true) {
        if (isPrime(num)) {
            count++;
            if (count == N)
                return num;
        }
        num++;
    }
}
