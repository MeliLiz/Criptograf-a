# Finding square roots modulo n givem its prime factors p and q
from Modp import square_roots, inv_mod_p


def find_square_roots(n, p, q,a):
    roots_p = square_roots(a, p)
    roots_q = square_roots(a, q)
    print(roots_p)
    print(roots_q)
    # Get the inverses of p and q
    c = inv_mod_p(p, q)
    d = inv_mod_p(q, p)  

    pos_roots = []
    # Possible roots
    for r in roots_p:
        for s in roots_q:
            x = (r * q * d + s * p * c) % n
            pos_roots.append(x)

    roots = list(set(pos_roots))
    return roots
    
    
    
if __name__ == '__main__':
    print("Finding square roots modulo n given its prime factors p and q")
    n = int(input("Enter a number n: "))
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    a = int(input("Enter a number a: "))
    roots = find_square_roots(n, p, q, a)
    if roots:
        print("The roots of", a, "mod",n, "are", roots)
    else:
        print(n, "doesn't have a square root mod", p, "and", q)
