# Solovay-Strassen primality test

import random
# from Jacobi import jacobi

def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be an odd positive number")
    result = 1
    a = a % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0

def test(n, times):
    if n < 3:
        raise ValueError("n must be greater than 2")
    else:
        for i in range(times):
            a = random.randint(2, n-2) # 2 <= a <= n-2
            r = pow(a, (n-1)//2, n)
            if r != 1 and r != n-1:
                return False
            s = jacobi(a, n)
            # If r is not congruent to s mod n, it is composite
            if r % n != s % n:
                return False
        return True # It is probably prime
    
if __name__ == '__main__':
    n = int(input("Enter a number: "))
    times = int(input("Enter the number of times: "))
    if test(n, times):
        print("It is probably prime.")
    else:
        print("It is composite.")