# Finding square roots modulo a prime p
import random

def find_s_t(n):
    s = 0
    t = n - 1
    while t % 2 == 0:
        t //= 2
        s += 1
    return s, t

def legendre(a, p): #Legendre symbol
    return pow(a, (p - 1) // 2, p)

def inv_mod_p(a, p): # Find the inverse of a mod p
    return pow(a, -1, p)

def square_roots(a, p):
    if legendre(a, p) != 1:
        return None  #a is not a quadratic residue mod p

    #Find a quadratic non-residue (b/p) = -1
    b = random.randint(2, p - 1) 
    while legendre(b, p) != p - 1:  # p-1 = -1
        b = random.randint(2, p - 1)

    s, t = find_s_t(p) # p-1 = 2^s * t
    a_inv = inv_mod_p(a, p) # a_inv = a^(-1) mod p

    c = pow(b, t, p) # c = b^t mod p
    r = pow(a, (t + 1) // 2, p) # r = a^((t+1)/2) mod p

    for i in range(1, s):
        d = pow(r * r * a_inv, 2**(s - i - 1), p)
        if d == p - 1:  #p-1 = -1
            r = (r * c) % p
        c = (c * c) % p

    return r, p - r


if __name__ == '__main__':
    print("Find the square roots modulo a prime p")
    p = int(input("Enter a prime number n: "))
    a = int(input("Enter a number a: "))   
    roots = square_roots(a, p)
    if roots:
        print("The roots of", a, "mod", p, "are", roots[0], "and", roots[1])
    else:
        print(a," doesn't have a square root mod", p)
