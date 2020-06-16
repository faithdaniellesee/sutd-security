# 50.042 FCS Lab 7 template
# Year 2019
# See Wan Yi Faith (1002851)

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys

import pyrsa_sq_mul as psm

def generate_RSA(bits=1024):
    newKey = RSA.generate(2048)
    public_key = newKey.publickey().exportKey("PEM")
    private_key = newKey.exportKey("PEM")
    return private_key, public_key

def encrypt_RSA(public_key_file,message):
    # Part I
    with open(public_key_file, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.pub'
        rsakey = RSA.importKey(key)                     # import public key as an RSA object
        messageBytes = open(message, 'rb').read()       # read messaage as bytes
        messageInt = psm.unpack_bigint(messageBytes)    # convert message to long int for exponentiation
        cipherTextInt = psm.square_multiply(messageInt, rsakey.e, rsakey.n) # exponentiation
        cipherTextByteArray = psm.pack_bigint(cipherTextInt) # convert long int to bytearray
        cipherTextBytes = bytes(cipherTextByteArray)         # convert bytearray to bytes
        fin.close()
    return cipherTextBytes

    '''
    # Part III
    with open(public_key_file, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.pub'
        rsakey = RSA.importKey(key)                     # import public key as an RSA object
        rsaoaep = PKCS1_OAEP.new(rsakey)
        messageBytes = open(message, 'rb').read()       # read messaage as bytes
        cipherText = rsaoaep.encrypt(messageBytes)
        fin.close()
    return cipherText
    '''

def decrypt_RSA(private_key_file,cipher):
    # Part I
    with open(private_key_file, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.priv'
        rsakey = RSA.importKey(key)                     # import private key as an RSA object
        cipherBytes = open(cipher, 'rb').read()         # read cipher as bytes
        cipherInt = psm.unpack_bigint(cipherBytes)      # convert cipher to long int for exponentiation
        plainTextInt = psm.square_multiply(cipherInt, rsakey.d, rsakey.n) # exponentiation
        plainTextByteArray = psm.pack_bigint(plainTextInt)   # convert long int to bytearray
        plainTextBytes = bytes(plainTextByteArray)           # convert bytearray to bytes
        fin.close()
    return plainTextBytes

    '''
    # Part III
    with open(private_key_file, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.priv'
        rsakey = RSA.importKey(key)                     # import private key as an RSA object
        rsaoaep = PKCS1_OAEP.new(rsakey)
        cipherBytes = open(cipher, 'rb').read()         # read cipher as bytes
        plainText = rsaoaep.decrypt(cipherBytes)
        fin.close()
    return plainText
    '''

def sign_RSA(private_key_loc,data):
    # Part I
    with open(private_key_loc, 'r') as fin:
        key = fin.read()
        rsakey = RSA.importKey(key)                     # import private key as an RSA object
        dataBytes = open(data, 'rb').read()             # read data as bytes
        digest = SHA256.new(dataBytes).digest()         # hash the plaintext
        digestInt = psm.unpack_bigint(digest)           # convert data to long int for exponentiation
        exponentiateDigestInt = psm.square_multiply(digestInt, rsakey.d, rsakey.n) # exponentiation
        exponentiateDigestByteArray = psm.pack_bigint(exponentiateDigestInt)   # convert long int to bytearray
        exponentiateDigestBytes = bytes(exponentiateDigestByteArray)           # convert bytearray to bytes
        fin.close()
    return exponentiateDigestBytes

    '''
    # Part III
    with open(private_key_loc, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.pub'
        rsakey = RSA.importKey(key)                     # import public key as an RSA object
        rsapss = PKCS1_PSS.new(rsakey)
        dataBytes = open(data, 'rb').read()
        SHAdigest = SHA256.new(dataBytes)
        rsapssSigned = rsapss.sign(SHAdigest)              # return base64
        fin.close()
    return rsapssSigned
    '''

def verify_sign(public_key_loc,sign,data):
    # Part I
    # exponentiation
    with open(public_key_loc, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.pub'
        rsakey = RSA.importKey(key)                     # import public key as an RSA object
        signBytes = open(sign, 'rb').read()             # read sign (signed message) as bytes
        signInt = psm.unpack_bigint(signBytes)   # convert sign (signed message) to long int for exponentiation
        signExponentiationInt = psm.square_multiply(signInt, rsakey.e, rsakey.n) # exponentiation
        signExponentiationByteArray = psm.pack_bigint(signExponentiationInt)   # convert long int to bytearray
        signExponentiationBytes = bytes(signExponentiationByteArray)           # convert bytearray to bytes
        fin.close()

    # hash value of plaintext
    dataBytes = open(data, 'rb').read()             # read data as bytes
    plaintextHash = SHA256.new(dataBytes).digest()  # hash the plaintext

    if plaintextHash == signExponentiationBytes:
        print("Verified: Hash value of plaintext = exponentiation.")
        return True
    else:
        print("Not verified.")
        return False

    '''
    # Part III
    with open(public_key_loc, 'r') as fin:
        key = fin.read()                                # 'mykey.pem.pub'
        rsakey = RSA.importKey(key)                     # import public key as an RSA object
        rsapss = PKCS1_PSS.new(rsakey)
        dataBytes = open(data, 'rb').read()
        digest = SHA256.new(dataBytes)
        fin.close()

    signBytes = open(sign, 'rb').read()

    if rsapss.verify(digest, signBytes):
        print("Verified.")
        return True
    else:
        print("Not verified.")
        return False
    '''

def encrypt(filein, fileout, key):
    encryptedText = encrypt_RSA(key, filein)
    with open(fileout, 'wb') as fout:
        fout.write(encryptedText)
        print("Encryption complete: encryptedmessage.txt.") # Part I
        # print("Encryption complete: encryptedmydata.txt.") # Part III
        fout.close()

def decrypt(filein, fileout, key):
    decryptedText = decrypt_RSA(key, filein)
    with open(fileout, 'wb') as fout:
        fout.write(decryptedText)
        print("Decryption complete: decryptedmessage.txt. This will match the original message.txt.") # Part I
        # print("Decryption complete: decryptedmydata.txt. This will match the original mydata.txt.") # Part III
        fout.close()

def signFile(filein, signout, key):
    signedText = sign_RSA(key, filein)
    with open(signout, 'wb') as sout:
        sout.write(signedText)
        print("Signing complete.")
        sout.close()

def genKey(fileout):
    privateKey, publicKey = generate_RSA()
    with open(fileout + '.priv', 'wb') as fpriv:
        fpriv.write(privateKey)
        print("Private key generated: key.priv")
        fpriv.close()
    with open(fileout + '.pub', 'wb') as fpub:
        fpub.write(publicKey)
        print("Public key generated: key.pub")
        fpub.close()

if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest = 'filein',help = 'input file')
    parser.add_argument('-o', dest = 'fileout', help = 'output file')
    parser.add_argument('-so', dest = 'signout', help = 'sign file')
    parser.add_argument('-k', dest = 'key', help = 'key')
    parser.add_argument('-m', dest = 'mode', help = 'mode')

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    signout = args.signout
    key = args.key
    mode = args.mode

    if (mode == "e" or mode == "E"):
        encrypt(filein, fileout, key)
    elif (mode == "d" or mode == "D"):
        decrypt(filein, fileout, key)
    elif (mode == "s" or mode == "S"):
        signFile(filein, signout, key)
    elif (mode == "v" or mode == "V"):
        verify_sign(key, fileout, filein)
    elif (mode == "g" or mode == "G"):
        genKey(fileout)
    else:
        print("Mode must be either 'e', 'E', 'd', 'D', 's', 'S', 'v', 'V', 'g' or 'G'.")
