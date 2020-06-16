from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode,b64encode
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import argparse
import sys

def generate_RSA(bits=1024):
    pass
    return private_key, public_key
    
def encrypt_RSA(public_key_file,message):
    pass

def decrypt_RSA(private_key_file,cipher):
    pass

def sign_RSA(private_key_loc,data):
    pass

def verify_sign(private_key_loc,sign,data):
    pass

if __name__=="__main__":
    pass
