#!/usr/bin/env python3
# Present skeleton file for 50.042 FCS
# This code is written by Wong Chi Seng
# My Lab 4 appears to have errors, thus to complete Lab 6, I have used his Lab 4 code


# constants
FULLROUND = 31

# S-Box Layer
sbox = [0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
        0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2]

sbox_inv = [0x5, 0xE, 0xF, 0x8, 0xC, 0x1, 0x2, 0xD,
            0xB, 0x4, 0x6, 0x3, 0x0, 0x7, 0x9, 0xA]


# PLayer
pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
       4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
       8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
       12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]


pmt_inv = [0 for x in range(64)]
for x in range(64):
    pmt_inv[pmt[x]] = x

# Rotate left: 0b1001 --> 0b0011


def rol(val, r_bits, max_bits): return \
    (val << r_bits % max_bits) & (2**max_bits - 1) | \
    ((val & (2**max_bits - 1)) >> (max_bits - (r_bits % max_bits)))

# Rotate right: 0b1001 --> 0b1100


def ror(val, r_bits, max_bits): return \
    ((val & (2**max_bits - 1)) >> r_bits % max_bits) | \
    (val << (max_bits - (r_bits % max_bits)) & (2**max_bits - 1))

def genRoundKeys(key):
    roundkeys = []
    roundkeys.append(32)
    for i in range(1,FULLROUND + 2):
        roundkeys.append(key >> 16)
        ##########
        #step 1
        rotated = ((key & (2 ** 19 -1)) << 61) #get first 19 bits, shift it left by 61
        key = rotated + (key >> 19) #shift remaining 61 bits to the right to make space for first 19.
        ##########
        #step 2
        get_sbox = (sbox[key >> 76] << 76) # get last 4 bits to index
        key = (key & (2 ** 76 - 1)) + get_sbox
        ##########
        #step 3
        key = key ^ (i << 15) #xor bits 15 16 17 18 19
    return roundkeys

def addRoundKey(state, Ki):
    return state ^ Ki


def sBoxLayer(state):
    output = 0
    for i in range(16):
        output += sbox[(state >> (4*i)) & 0xF] << (4*i)
    return output


def sBoxLayer_inv(state):
    output = 0
    for i in range(16):
        output += sbox_inv[(state >> (4*i)) & 0xF] << (4*i)
    return output

def pLayer(state):
    output = 0
    for i in range(64):
        output += ((state >> i) & 0x01) << pmt[i]
    return output

def pLayer_inv(state):
    output = 0
    for i in range(64):
        output += ((state >> i) & 0x01) << pmt_inv[i]
    return output

def present_round(state, roundKey): #encrypt
    state = addRoundKey(state, roundKey)
    # print("normal addrnd:", state)
    state = sBoxLayer(state)
    # print("normal sBoxLayer:", state)
    state = pLayer(state)
    # print("normal pLayer:", state)
    # print("pLayer:", state)
    return state


def present_inv_round(state, roundKey): #decrypt
    state = pLayer_inv(state)
    state = sBoxLayer_inv(state)
    state = addRoundKey(state, roundKey)
    return state


def present(plain, key):
    K = genRoundKeys(key)
    state = plain
    for i in range(1, FULLROUND + 1):
        state = present_round(state, K[i])
    state = addRoundKey(state, K[32])
    return state


def present_inv(cipher, key):
    K = genRoundKeys(key)
    state = cipher
    state = addRoundKey(state, K[32])
    for i in range(FULLROUND, 0, -1):
        state = present_inv_round(state, K[i])
    return state

if __name__ == "__main__":
    # Testvector for key schedule
    key1 = 0x00000000000000000000
    keys = genRoundKeys(key1)
    keysTest = {0: 32, 1: 0, 2: 13835058055282163712, 3: 5764633911313301505, 4: 6917540022807691265, 5: 12682149744835821666, 6: 10376317730742599722, 7: 442003720503347, 8: 11529390968771969115, 9: 14988212656689645132, 10: 3459180129660437124, 11: 16147979721148203861, 12: 17296668118696855021, 13: 9227134571072480414, 14: 4618353464114686070, 15: 8183717834812044671, 16: 1198465691292819143, 17: 2366045755749583272, 18: 13941741584329639728, 19: 14494474964360714113, 20: 7646225019617799193, 21: 13645358504996018922, 22: 554074333738726254, 23: 4786096007684651070, 24: 4741631033305121237, 25: 17717416268623621775, 26: 3100551030501750445, 27: 9708113044954383277, 28: 10149619148849421687, 29: 2165863751534438555, 30: 15021127369453955789, 31: 10061738721142127305, 32: 7902464346767349504}
    for k in keysTest.keys():
        assert keysTest[k] == keys[k]

    # Testvectors for single rounds without keyscheduling
    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    round1 = present_round(plain1, key1)
    round11 = 0xffffffff00000000
    assert round1 == round11

    round2 = present_round(round1, key1)
    round22 = 0xff00ffff000000
    assert round2 == round22

    round3 = present_round(round2, key1)
    round33 = 0xcc3fcc3f33c00000
    assert round3 == round33

    # invert single rounds
    plain11 = present_inv_round(round1, key1)
    assert plain1 == plain11
    plain22 = present_inv_round(round2, key1)
    assert round1 == plain22
    plain33 = present_inv_round(round3, key1)
    assert round2 == plain33

    # Everything together
    plain1 = 0x0000000000000000
    key1 = 0x00000000000000000000
    cipher1 = present(plain1, key1)
    # print(cipher1)
    plain11 = present_inv(cipher1, key1)
    # print(plain11)
    assert plain1 == plain11

    plain2 = 0x0000000000000000
    key2 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher2 = present(plain2, key2)
    plain22 = present_inv(cipher2, key2)
    assert plain2 == plain22

    plain3 = 0xFFFFFFFFFFFFFFFF
    key3 = 0x00000000000000000000
    cipher3 = present(plain3, key3)
    plain33 = present_inv(cipher3, key3)
    assert plain3 == plain33

    plain4 = 0xFFFFFFFFFFFFFFFF
    key4 = 0xFFFFFFFFFFFFFFFFFFFF
    cipher4 = present(plain4, key4)
    plain44 = present_inv(cipher4, key4)
    assert plain4 == plain44
