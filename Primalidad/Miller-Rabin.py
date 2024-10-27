# Miller Rabin primality test
import random

def get_r_s(n):
    r, s = n-1, 0
    while r % 2 == 0 and r > 0:
        r //= 2
        s += 1
    return r, s

def MillerRabin(n, times):
    if n < 3:
        raise ValueError("n must be greater than 2")
    else:
        # Calculate r such that n-1 = 2^s * r
        r, s = get_r_s(n)
        print("r:", r, "s:", s)
        for i in range(times):
            a = random.randint(2, n-2) # 2 <= a <= n-2
            y = pow(a, r, n)
            if y != 1 and y != n-1:
                j = 1
                while j <= s-1 and y != n-1:
                    y = pow(y, 2, n)
                    if y == 1:
                        return False
                    j += 1
                if y != n-1:
                    return False
        return True
    
if __name__ == '__main__':
    input_n = int(input("Enter a number: "))
    input_times = int(input("Enter the number of times: "))
    if MillerRabin(input_n, input_times):
        print("It is probably prime.")
    else:
        print("It is composite.")