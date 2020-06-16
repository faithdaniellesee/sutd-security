#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 3
# See Wan Yi Faith (1002851)
'''
Time taken:
1. Brute force 5-character: 387.2673816680908s (15 out of 15 hashes)
2. Rainbow table 5-character: 48.86s (15 out of 15 hashes)
3. Rainbow table 6-character: 132.64s (14 out of 15 hashes)
'''

# Import libraries
import hashlib
import time
import itertools
import random

def bruteForce():
    character_list = "qwertyuiopasdfghjklzxcvbnm1234567890"
    inputs = []

    start = time.time()
    with open('hash5_decrypted.txt', 'w') as fout:
        # Open and read the hash5.txt file
        with open('hash5.txt', 'r') as fin:
            hashlist = fin.read().splitlines()  # ['a92b66a9802704ca8616c4b092378272', 'd4efdba5e9725e77c9b9051fa8136f0a'...]

            for input_tuple in itertools.product(character_list, repeat = 5): # e.g.: [('a', 'a', 'a'), ('a', 'a', 'b')]
                input = "".join(input_tuple)                                  # e.g.: aaa
                hash_guess = hashlib.md5(input.encode()).hexdigest()
                if hash_guess in hashlist:
                    inputs.append(input)                                      # append to lists of inputs
                    fout.write(input + '\n')
                    print("Found a match!")
                    if len(inputs) == 15:
                        print("List of inputs: " + str(inputs))
                        break
            fin.close()
        fout.close()

    end = time.time()
    run_time = end - start
    print("Total run time in seconds: " + str(run_time))
    # Total run time in seconds: 387.2673816680908s

'''
Part 4: Rainbow tables

Commands to run:
chmod +x rtgen
chmod +x rtsort
chmod +x rcrack

./rtgen md5 loweralpha-numeric 5 5 0 3800 600000 0
./rtsort /home/faith/rainbowcrack-1.7-linux64
./rcrack /home/faith/rainbowcrack-1.7-linux64 -l /home/faith/rainbowcrack-1.7-linux64/hash5.txt

plaintext found: 15 of 15
total time: 48.86s
'''

def salting():
    character_list = "qwertyuiopasdfghjklzxcvbnm1234567890"
    salted = []

    with open('pass6.txt', 'w') as fout:
        # Open and read the hash5_decrypted.txt file
        with open('hash5_decrypted.txt', 'r') as fin:
            password_list = fin.read().splitlines() # ['egunb', 'tthel'...]

            for password in password_list:
                random_number = random.randint(0, len(character_list))
                password += character_list[random_number]
                salted.append(password)
                fout.write(password + '\n')
                if len(salted) == 15:
                    print("List of salted passwords: " + str(salted))
                    break
            fin.close()
        fout.close()

def hashing_salted():
    hashed_salts = []

    with open('salted6.txt', 'w') as fout:
        # Open and read the hash5_decrypted.txt file
        with open('pass6.txt', 'r') as fin:
            salted_password_list = fin.read().splitlines() # ['egunbw', 'tthelu'...]
            print(salted_password_list)

            for salted_password in salted_password_list:
                hashed_salt = hashlib.md5(salted_password.encode()).hexdigest()
                hashed_salts.append(hashed_salt)
                fout.write(hashed_salt + '\n')
                if len(hashed_salts) == 15:
                    print("List of hashed salted passwords: " + str(hashed_salts))
                    break
            fin.close()
        fout.close()

'''
Part 5: Rainbow tables

Commands to run:
./rtgen md5 loweralpha-numeric 6 6 0 3800 600000 0
./rtsort /home/faith/rainbowcrack-1.7-linux64
./rcrack /home/faith/rainbowcrack-1.7-linux64 -l /home/faith/rainbowcrack-1.7-linux64/salted6.txt

plaintext found: 9 of 15
total time: 366.31s

./rtgen md5 loweralpha-numeric 6 6 0 4500 1000000 0
./rtsort /home/faith/rainbowcrack-1.7-linux64
./rcrack /home/faith/rainbowcrack-1.7-linux64 -l /home/faith/rainbowcrack-1.7-linux64/salted6.txt

plaintext found: 11 of 15
total time: 410.06s

./rtgen md5 loweralpha-numeric 6 6 0 7600 1200000 0
./rtsort /home/faith/rainbowcrack-1.7-linux64
./rcrack /home/faith/rainbowcrack-1.7-linux64 -l /home/faith/rainbowcrack-1.7-linux64/salted6.txt

plaintext found: 12 of 15
total time: 152.89s

./rtgen md5 loweralpha-numeric 6 6 0 7600 2000000 0
./rtsort /home/faith/rainbowcrack-1.7-linux64
./rcrack /home/faith/rainbowcrack-1.7-linux64 -l /home/faith/rainbowcrack-1.7-linux64/salted6.txt

plaintext found: 14 of 15
total time: 132.64s
'''

if __name__ == "__main__":
    bruteForce()
    salting()
    hashing_salted()
