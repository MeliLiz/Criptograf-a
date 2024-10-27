# Fermat test for primality
import random

def FermatTest(n, times):
    if n<3:
        raise ValueError("n must be greater than 2")
    else:
        for i in range(0, times):
            a = random.randint(2, n-2) # 2 <= a <= n-2
            if pow(a, n-1, n) != 1: # If a^(n-1) mod n != 1, it is composite
                return False
        return True # It is probably prime

if __name__ == '__main__':
    input_n = int(input("Enter a number: "))
    input_times = int(input("Enter the number of times: "))
    if FermatTest(input_n, input_times):
        print("It is probably prime.")
    else:
        print("It is composite.")