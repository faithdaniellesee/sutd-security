import binascii
import struct

# create 256-entry list (S) based on a key (key)
def KSA(key):
    S = list(range(256))                            #initialize the array
    # Add KSA implementation Here
    j = 0
    for i in list(range(256)):                      # index i randomly over the entire array
        j = (j + S[i] + key[i % len(key)]) % 256    # index j randomly over the entire array, j depends on the key (pseudo-random)
        S[i], S[j] = S[j], S[i]                     # swap the contents of i and j
    return S

# yield a pseudo-random stream of bytes based on the 256-entry list generated (S)
def PRGA(S):
    K = 0
    # Add PRGA implementation here
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

if __name__ == '__main__':
    # RC4 algorithm please refer to http://en.wikipedia.org/wiki/RC4

    ## key = a list of integer, each integer 8 bits (0 ~ 255)
    ## ciphertext = a list of integer, each integer 8 bits (0 ~ 255)
    ## binascii.unhexlify() is a useful function to convert from Hex string to integer list
    print ("**********************************************************")
    print ("#1: Beginning RC4 test cases..." + '\n')
    # Test cases:
    #1: plaintext1 = '0F6D13BC'
    key1 = list(binascii.unhexlify('1A2B3C'))
    ciphertext1 = list(binascii.unhexlify('00112233'))

    ## Use RC4 to generate keystream
    keystream1 = RC4(key1)
    # print(keystream)

    ## Cracking the ciphertext
    plaintext1 = ""
    for i in ciphertext1:
        plaintext1 += ('{:02X}'.format(i ^ next(keystream1)))
    print("Solution: " + plaintext1)
    print("Answer: " + '0F6D13BC')

    if plaintext1 == '0F6D13BC':
        print("RC4 test case 1 passed." + '\n')
    else:
        print("RC4 test case 1 failed." + '\n')

    #2: plaintext2 = 'DE09AB72'
    key2 = list(binascii.unhexlify('000000'))
    ciphertext2 = list(binascii.unhexlify('00112233'))

    ## Use RC4 to generate keystream
    keystream2 = RC4(key2)
    # print(keystream)

    ## Cracking the ciphertext
    plaintext2 = ""
    for i in ciphertext2:
        plaintext2 += ('{:02X}'.format(i ^ next(keystream2)))
    print("Solution: " + plaintext2)
    print("Answer: " + 'DE09AB72')

    if plaintext2 == 'DE09AB72':
        print("RC4 test case 2 passed." + '\n')
    else:
        print("RC4 test case 2 failed." + '\n')

    #3: plaintext3 = '6F914F8F'
    key3 = list(binascii.unhexlify('012345'))
    ciphertext3 = list(binascii.unhexlify('00112233'))

    ## Use RC4 to generate keystream
    keystream3 = RC4(key3)
    # print(keystream)

    ## Cracking the ciphertext
    plaintext3 = ""
    for i in ciphertext3:
        plaintext3 += ('{:02X}'.format(i ^ next(keystream3)))
    print("Solution: " + plaintext3)
    print("Answer: " + '6F914F8F')

    if plaintext3 == '6F914F8F':
        print("RC4 test case 3 passed." + '\n')
    else:
        print("RC4 test case 3 failed." + '\n')

    if plaintext1 == '0F6D13BC' and plaintext2 == 'DE09AB72' and plaintext3 == '6F914F8F':
        print ("RC4 test cases completed successfully :')")
    else:
        print("RC4 test cases completed unsuccessfully :'()")
    print ("**********************************************************")

    print ("#2: Checking ICV..." + '\n')
    ## Check ICV
    # 1. Decrypt the message (data + ICV)
    #    a. IV, key from task #1 = 46bcf4, 1F1F1F1F1F
    #       input key = IV || key
    keyM = list(binascii.unhexlify('46bcf41F1F1F1F1F'))
    #    b. ciphertext = encrypted message = data + ICV
    ciphertextM = list(binascii.unhexlify('98999de0ce2db11eb2169a5d442143cdd0470a8832f6712745fb4ffacdcc9ff99681c1da2f8c479ef446300eaa68aaca018b6a0a985c8ba2536e'))

    #    c. use RC4 to generate keystream
    keystreamM = RC4(keyM)

    #    d. cracking the ciphertext
    plaintextM = ""
    for i in ciphertextM:
        plaintextM += ('{:02X}'.format(i ^ next(keystreamM)))

    # 2. Extract decrypted IVC
    encIVC = '8ba2536e'
    decIVC = plaintextM[-len(encIVC):]
    print("Decrypted IVC: " + decIVC)

    # 3. Calculate CRC from data only
    decData = plaintextM[:-len(encIVC)] # encrypted ICV obtained from Wireshark PCAP
    crcle = binascii.crc32(bytes.fromhex(decData)) & 0xffffffff
    crc = struct.pack('<L', crcle).hex().upper()
    print("Message CRC: " + crc)

    if crc == decIVC:
        print("CRC of message = decrypted IVC, successful cracking. :')" + '\n')
    else:
        print("CRC of message != decrypted IVC, unsuccessful cracking. :'()" + '\n')

    print("Decrypted data: " + decData)
    print("Decrypted IVC: " + decIVC)
    print ("**********************************************************")


dddd
