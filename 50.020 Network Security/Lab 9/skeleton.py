import binascii
import struct

def KSA(key):
    S = list(range(256))
    # Add KSA implementation Here
    
    return S

def PRGA(S):
    K = 0
    # Add PRGA implementation here
    while True:
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

if __name__ == '__main__':
    # RC4 algorithm please refer to http://en.wikipedia.org/wiki/RC4

    ## key = a list of integer, each integer 8 bits (0 ~ 255)
    ## ciphertext = a list of integer, each integer 8 bits (0 ~ 255)
    ## binascii.unhexlify() is a useful function to convert from Hex string to integer list

    ## Use RC4 to generate keystream
    keystream = RC4(key)
    print(keystream)
    
    ## Cracking the ciphertext
    plaintext = ""
    for i in ciphertext:
        plaintext += ('{:02X}'.format(i ^ next(keystream)))
    
    #     Several test cases: (to test RC4 implementation only)
    #     1. key = '1A2B3C', cipertext = '00112233' -> plaintext = '0F6D13BC'
    #     2. key = '000000', cipertext = '00112233' -> plaintext = 'DE09AB72'
    #     3. key = '012345', cipertext = '00112233' -> plaintext = '6F914F8F'
    
    
    
    ## Check ICV