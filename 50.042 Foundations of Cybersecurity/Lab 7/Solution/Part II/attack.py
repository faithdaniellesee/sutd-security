# 50.042 FCS Lab 7 template
# Year 2019
# See Wan Yi Faith (1002851)

from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode

import pyrsa_sq_mul as psm
import pyrsa as pyrsa
from Crypto.Hash import SHA256

# obtaining keys
# public key
with open('mykey.pem.pub', 'r') as fin:
    key = fin.read()                                # 'mykey.pem.pub'
    pubkey = RSA.importKey(key)                     # import public key as an RSA object
    fin.close()

# private key
with open('mykey.pem.priv', 'r') as fin:
    key = fin.read()                                # 'mykey.pem.pub'
    privkey = RSA.importKey(key)                     # import public key as an RSA object
    fin.close()

##############################################
# RSA Encryption Protocol Attack
##############################################
print("##############################################")
print("RSA Encryption Protocol Attack")
print("##############################################")
yInt = 100
yByteArray = psm.pack_bigint(yInt) # convert int to byte array
yBytes = bytes(yByteArray)

print("Part II-------------")

# 1. Encryption
print("Encrypting: " + str(yInt) + "\n")
print("Result:")
encryptedInt = psm.square_multiply(yInt, pubkey.e, pubkey.n)
encryptedByteArray = psm.pack_bigint(encryptedInt)
encryptedBytes = bytes(encryptedByteArray)
encodedEncryptedBytes = b64encode(encryptedBytes)
encryptionStringResult = encodedEncryptedBytes.decode("utf-8")
print(encryptionStringResult)

print("\n" + "Modified to:")
# 2a. Choose a multiplier s equal to 2
s = 2
sByteArray = psm.pack_bigint(s) # convert int to byte array
sBytes = bytes(sByteArray)

# 2b. Calculate s
sInt = psm.square_multiply(s, pubkey.e, pubkey.n) # exponentiation
sByteArray = psm.pack_bigint(sInt)       # convert long int to bytearray
sBytes = bytes(sByteArray)               # convert bytearray to bytes
encodedSBytes = b64encode(sBytes)
sStringResult = encodedSBytes.decode("utf-8")

# 3. Multiply the two numbers
newYInt = sInt*encryptedInt
newYByteArray = psm.pack_bigint(newYInt)
newYBytes = bytes(newYByteArray)
encodedYBytesStringResult = b64encode(newYBytes).decode("utf-8")
print(encodedYBytesStringResult)

# 4. Decryption
cipherInt = psm.unpack_bigint(newYBytes)        # convert cipher to long int for exponentiation
plainTextInt = psm.square_multiply(cipherInt, privkey.d, privkey.n) # exponentiation
print("\n" + "Decrypted: " + str(plainTextInt) + "\n")

##############################################
# RSA Digital Signature Protocol Attack
##############################################
print("##############################################")
print("RSA Digital Signature Protocol Attack")
print("##############################################")
# 1. Generate a random signature s
s = 2
sByteArray = psm.pack_bigint(s) # convert int to byte array
sBytes = bytes(sByteArray)

# 2. Compute a new digest
xInt = psm.square_multiply(s, pubkey.e, pubkey.n) # exponentiation
xByteArray = psm.pack_bigint(xInt)       # convert long int to bytearray
xBytes = bytes(xByteArray)               # convert bytearray to bytes
encodedXBytes = b64encode(xBytes)
xStringResult = encodedXBytes.decode("utf-8")

# 3. Verify signature s for digest x
signInt = psm.unpack_bigint(sBytes)   # convert sign (signed message) to long int for exponentiation
signExponentiationInt = psm.square_multiply(signInt, pubkey.e, pubkey.n) # exponentiation
signExponentiationByteArray = psm.pack_bigint(signExponentiationInt)   # convert long int to bytearray
signExponentiationBytes = bytes(signExponentiationByteArray)           # convert bytearray to bytes
encodedSignExponentiationBytes = b64encode(signExponentiationBytes)
encodedSignExponentiationStringResult = encodedSignExponentiationBytes.decode("utf-8")

if xStringResult == encodedSignExponentiationStringResult:
    print("Verified: Hash value of plaintext = exponentiation.")
else:
    print("Not verified.")
