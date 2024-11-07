def mod_pow(base, exp, mod): # base^exp % mod
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inv(a, mod):
    g, x, y = extended_gcd(a, mod)
    if g != 1:
        raise Exception(f"No existe inverso modular de {a} modulo {mod}")
    return x % mod

def extended_gcd(a, b): # Extended Euclidean Algorithm
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def is_quadratic_residue(n, p):
    return mod_pow(n, (p - 1) // 2, p) == 1

def tonelli_shanks(n, p): # Tonelli-Shanks Algorithm
    if n == 0:
        return [0]
    if p == 2:
        return [n % 2]
    if mod_pow(n, (p - 1) // 2, p) != 1:
        return []  # No tiene raíz cuadrada

    if p % 4 == 3: # If p is congruent to 3 mod 4
        return [mod_pow(n, (p + 1) // 4, p)]

    s, q = 0, p - 1
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while is_quadratic_residue(z, p):
        z += 1
    m = s
    c = mod_pow(z, q, p)
    t = mod_pow(n, q, p)
    r = mod_pow(n, (q + 1) // 2, p)

    while t != 0 and t != 1:
        t2i = t
        i = 0
        for i in range(1, m):
            t2i = mod_pow(t2i, 2, p)
            if t2i == 1:
                break
        b = mod_pow(c, 2 ** (m - i - 1), p)
        m = i
        c = mod_pow(b, 2, p)
        t = (t * b * b) % p
        r = (r * b) % p

    if t == 0:
        return [0]
    return [r, p - r]


def get_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def chinese_remainder_theorem(rem, mods): 
    x = 0
    prod = 1
    for mod in mods:
        prod *= mod

    for r, mod in zip(rem, mods):
        pp = prod // mod
        inv = mod_inv(pp, mod)
        x += r * inv * pp
    return x % prod


def sqrt_mod_composed(n, mod):
    factors = get_factors(mod)
    solutions = []
    
    for factor in set(factors):
        # Get the square roots mod each factor
        roots = tonelli_shanks(n, factor) 
        if not roots:
            print("No hay raíces cuadradas de", n, "módulo", factor)
            return [] 
        print(roots)
        solutions.append(roots[0])

    x = chinese_remainder_theorem(solutions, [factor for factor in set(factors)])
    return [x]  

if __name__ == '__main__':
    a = 76 
    n = 102

    result = sqrt_mod_composed(a, n)
    if result:
        print("Las raíces cuadradas de", a, "módulo", n, "son", result)
    else:
        print("No hay raíces cuadradas de", a, "módulo", n)
