#Kanty-Louange Gakima, 20184109
#Marianne Schmit Pemmerl, 20192143
import math
import random
import sys




def write(fileName, content):
    """Write output in file"""
    with open(fileName, "w") as file:
        file.write(content)
#source du test de Miller Rabin: https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/

def power(x, y, p):
    """Modular exponentiation function"""
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def miillerRabinTest(d, n):
    """Miller-Rabin primality test function"""
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def isPrime(n, k):
    """Check if number is prime using Miller-Rabin"""
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2
    for i in range(k):
        if not miillerRabinTest(d, n):
            return False
    return True

def prime_generator():
    """Generate an infinite sequence of prime numbers."""
    i = 2
    while True:
        if isPrime(i, 5):
            yield i
        i += 1

concat_primes = {}
def check_prime_concat(p1, p2):
    """Check if concatenated numbers are primes in both orders"""
    key = str(p1) + "_" + str(p2)  # Use underscore to avoid concatenation issues like "11" and "1" forming "111"
    reverse_key = str(p2) + "_" + str(p1)
    if key not in concat_primes:
        concat_primes[key] = isPrime(int(str(p1) + str(p2)), 4)
        concat_primes[reverse_key] = isPrime(int(str(p2) + str(p1)), 4)
    return concat_primes[key] and concat_primes[reverse_key]

def find_special_numbers(prime_gen, num_sets):
    """Optimized function to find special sets of primes"""
    primes = []
    special_numbers = set()
    connections = {}

    while len(special_numbers) < num_sets:
        new_prime = next(prime_gen)
        primes.append(new_prime)
        new_connections = []

        for p in primes[:-1]:
            if check_prime_concat(new_prime, p):
                new_connections.append(p)
                connections.setdefault(p, []).append(new_prime)

        connections[new_prime] = new_connections

        for p1 in new_connections:
            for p2 in connections[p1]:
                if p2 not in new_connections:
                    continue
                for p3 in connections[p2]:
                    if p3 not in new_connections or p3 not in connections[p1]:
                        continue
                    quadruple = tuple(sorted([new_prime, p1, p2, p3]))
                    special_numbers.add(quadruple)
                    if len(special_numbers) == num_sets:
                        return list(special_numbers)

    return list(special_numbers)

def main(args):
    n = int(args[0])
    output_file = args[1]
    primes_gen = prime_generator()
    if n<=50:
        num_special_sets = n*6
    else:
        num_special_sets = 400
    special_numbers = find_special_numbers(primes_gen, num_special_sets)
    special_numbers.sort(key=lambda x: sum(x))
    
    answer = sum(special_numbers[n-1])
    write(output_file, str(answer))

    # TODO : Compléter ici/Complete here...
    # Vous pouvez découper votre code en d'autres fonctions...
    # You may split your code in other functions...

     

    

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])