import math
from functools import reduce
from itertools import combinations

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def legendre_symbol(a, p): # Verify if a is a quadratic residue modulo p
    return pow(a, (p - 1) // 2, p)

def get_factor_base(n, limit=1000): # Get the factor base
    base = []
    for p in range(2, limit):
        if is_prime(p) and legendre_symbol(n, p) == 1:
            base.append(p)
    return base

def if_smooth(b, B): #If b is B-smooth, return its factors, otherwise return None
    factors = []
    for p in B:
        while b % p == 0:
            factors.append(p)
            b //= p
    return factors if b == 1 else None

def quadratic_sieve(n):
    #Select the factor base
    S = get_factor_base(n, limit=100)
    m = math.isqrt(n)
    smooth_numbers = []
    x_values = []
    for x in range(1, len(S) + 2000): # Arbitrarily chosen limit
        a = m + x
        b = a * a - n
        factors = if_smooth(b, S)
        if factors:
            smooth_numbers.append((a, factors))
            x_values.append(a)

    if len(smooth_numbers) < len(S):
        print("No hay suficientes números suaves. Intente con un límite mayor.")
        return None

    #Matrix of exponents modulo 2
    matrix = []
    for _, factors in smooth_numbers:
        row = [factors.count(p) % 2 for p in S]
        matrix.append(row)

    #Find a dependent subset
    T = find_dependent_subset(matrix)
    if not T:
        print("Error: No se encontró un subconjunto dependiente.")
        return None

    #Get the factors
    x = reduce(lambda a, b: a * b % n, [x_values[i] for i in T])
    y_squared = reduce(lambda a, b: a * b % n, [smooth_numbers[i][0]**2 - n for i in T])
    y = math.isqrt(y_squared)

    #Check if the factors are correct
    factor = greatest_common_divisor(x - y, n)
    if factor != 1 and factor != n:
        other_factor = n // factor
        return factor, other_factor
    else:
        return None

#Find a dependent subset of rows in the matrix modulo 2
def find_dependent_subset(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    #Try to get a subset of rows that sum to the zero vector
    for r in range(1, num_rows + 1):
        for rows in combinations(range(num_rows), r):
            sum_row = [sum(matrix[i][j] for i in rows) % 2 for j in range(num_cols)]
            if all(val == 0 for val in sum_row):
                return list(rows)
    return None

if __name__ == "__main__":
    n = 8746  # Número compuesto de ejemplo
    factors = quadratic_sieve(n)
    if factors:
        print("Factores encontrados:", factors)
    else:
        print("No se encontraron factores")
