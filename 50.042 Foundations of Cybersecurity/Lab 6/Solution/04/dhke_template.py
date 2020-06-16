#50.042 FCS Lab 6 template
#Year 2019
# See Wan Yi Faith (1002851)

import primes_template as primes
import random

# prime number closest to 2**80 = 1208925819614629174706189

def dhke_setup(nb):
    p = primes.gen_prime_nbits(nb)
    alpha = random.randint(2, p-2)
    return p, alpha

def gen_priv_key(p):
    a = random.randint(2, p-2)
    return a

def get_pub_key(alpha, a, p):
    A = primes.square_multiply(alpha, a, p)
    return A

def get_shared_key(keypub,keypriv,p):
    sharedKey = primes.square_multiply(keypub, keypriv, p)
    return sharedKey

if __name__=="__main__":
    p,alpha= dhke_setup(80)
    print ('Generate P and alpha:')
    print ('P:',p)
    print ('alpha:',alpha)
    a=gen_priv_key(p)
    b=gen_priv_key(p)
    print ('My private key is: ',a)
    print ('Test other private key is: ',b)
    A=get_pub_key(alpha,a,p)
    B=get_pub_key(alpha,b,p)
    print ('My public key is: ',A)
    print ('Test other public key is: ',B)
    sharedKeyA=get_shared_key(B,a,p)
    sharedKeyB=get_shared_key(A,b,p)
    print ('My shared key is: ',sharedKeyA)
    print ('Test other shared key is: ',sharedKeyB)
    print ('Length of key is %d bits.'%sharedKeyA.bit_length())
