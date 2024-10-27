

def decompose_power_of_2(a):
    # exponente e en 0
    e = 0

    if a % 2 != 0:
        return e, a

    # Dividir a con 2 hasta que sea impar, obtener el exponente en cada iteracion
    while a % 2 == 0:
        a //= 2
        e += 1
    return e, a

# funcion que regresa True en caso de que a congruente mod n, False en otro caso
def is_congruent(a, b, n):
    return (a - b) % n == 0

# funcion que regresa el simbolo de Jacobi, si n es primo, entonces devuelve el simbolo de Legendre
def jacobi(a,n):
    s = 1
    if n <= 3:
        print("n must be greater than 3")
    if not(a < n and a >= 0):
        print("a must be greater or equal than 0 and less than n")
    if a == 0:
        return 0
    if a == 1:
        return 1
    e, a1 = decompose_power_of_2(a)
    if e % 2 == 0:
        s = 1
    else:
        if is_congruent(n,1,8) and is_congruent(n,-1,8):
            s = 1
        elif is_congruent(n,3,8) and is_congruent(n,-3,8):
            s = -1

    if is_congruent(a1, 3, 4) and is_congruent(n, 3, 4):
        s = -s
    n1 = n % a1
    if a1 == 1:
        return s
    else:
        return s*jacobi(n1, a1)