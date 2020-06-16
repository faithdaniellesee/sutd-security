# 50.042 FCS Lab 7 template
# Year 2019
# See Wan Yi Faith (1002851)

from Crypto.PublicKey import RSA
from base64 import b64encode,b64decode
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

# function to convert long int to byte string
def pack_bigint(i):
    b=bytearray()
    while i:
        b.append(i&0xFF)
        i>>=8
    return b

# function to convert byte string to long int
def unpack_bigint(b):
    b=bytearray(b)
    return sum((1<<(bi*8))* bb for (bi,bb) in enumerate(b))

if __name__=="__main__":
    pass
