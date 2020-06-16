#50.042 FCS Lab 6 template
# Year 2019
# See Wan Yi Faith (1002851)

import random

def square_multiply(a,x,n):
    y = 1

    coeffs = []
    binX = bin(x)           # convert x to binary
    for i in binX[2:]:      # ignore first 2 characters: 0b
        coeffs.append(int(i))

    n_b = (len(binX) - 2)   # n_b is the number of bits in x

    for i in range(n_b):
        y = y**2 % n
        if coeffs[i] == 1:
            y = a*y % n

    return y

def miller_rabin(num, iter):
    # n / num: number to check if it is prime
    # a / iter: number of iterations

    # A return value of False means n is certainly not prime.
    # A return value of True means n is very likely a prime.
    if num == 2:          # 2 is the only even prime number
        return True
    if not (num & 1):     # binary AND
        return False

    num1 = num - 1
    u = 0
    r = num1

    while r % 2 == 0:
        r >>= 1           # bit shift to the right by 1
        u += 1

    assert num-1 == 2**u*r

    def witness(b):
        z = square_multiply(b, r, num)
        if z == 1:
            return False

        for i in range(u):
            z = square_multiply(b, 2**i*r, num)
            if z == num1:
                return False
        return True

    # finding number of bits of num:
    numBits = len(bin(num).lstrip('0b'))

    for j in range(iter):
        b = random.randrange(1<<numBits-1, 1<<numBits)
        if witness(b):
            return False

    return True

def gen_prime_nbits(n):
    # generate a random number
    x = random.getrandbits(n)

    # call miller_rabin to check if x is a prime, return x if prime, else generate new x
    while not miller_rabin(x, iter=2):
        x = random.getrandbits(n)

    # ls = []
    # for i in str(x):
    #     ls.append(i)
    #
    # while len(ls) != n:
    #     ls.insert(0, 0)
    #
    # s = [str(j) for j in ls]
    # res = int("".join(s))
    #
    # return res
    return x

if __name__=="__main__":
    print("4 = 5^2 % 7")
    print(square_multiply(5,2,7))
    print("1 = 3^8 % 5")
    print(square_multiply(3,8,5))
    print("0 = 4^4 % 4")
    print(square_multiply(4,4,4))

    print ('Is 561 a prime?')
    print (miller_rabin(561,2))
    print ('Is 27 a prime?')
    print (miller_rabin(27,2))
    print ('Is 61 a prime?')
    print (miller_rabin(61,2))

    print ('Random number (100 bits):')
    print (gen_prime_nbits(100))
    print ('Random number (80 bits):')
    print (gen_prime_nbits(80))
