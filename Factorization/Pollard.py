    
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def pollards_rho(n):
    a = b = 2
    while True:
        a = (a*a + 1) % n
        b = (b*b + 1) % n
        b = (b*b + 1) % n
        d = greatest_common_divisor(abs(a-b), n)
        if 1 < d < n:
            return d, n // d
        elif d == n:
            return None


if __name__ == "__main__":
    n = 256961
    factores = pollards_rho(n)
    if factores:
        print("Factores encontrados:", factores)
    else:
        print("No se encontraron factores. Intenta de nuevo.")
