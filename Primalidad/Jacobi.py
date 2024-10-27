def get_r_s(n):
    r, s = n-1, 0
    while r % 2 == 0 and r > 0:
        r //= 2
        s += 1
    return r, s


def Jacobi(a, n):
    if n<3 or n<=a:
        raise ValueError("n must be greater than 2 and greater than a")
    else:
        if a==0:
            return 0
        elif a==1:
            return 1
        else:
            a1, e = get_r_s(a)
            if e % 2 == 0:
                s = 1
            else:
                if n%8 == 1 or n%8 == 7:
                    s = 1
                elif n%8 == 3 or n%8 == 5:
                    s = -1

            if n%4 == 3 and a1%4 == 3:
                s = -s
            n1 = n % a1
            if a1 == 1:
                return s
            else:
                return s * Jacobi(n1, a1)
            

if __name__ == '__main__':
    input_a = int(input("Enter a: "))
    input_n = int(input("Enter n: "))
    print("Jacobi symbol of a and n is", Jacobi(input_a, input_n))
    
