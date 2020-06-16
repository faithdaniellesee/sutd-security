#!/usr/bin/env python3
# ECB wrapper
# SUTD 50.042 FCS Lab 4
# See Wan Yi Faith (1002851)

from present import *
import argparse

nokeybits=80
blocksize=64

def ecb(infile,outfile,key,mode):

    outputs = []

    with open(keyfile, mode='rb') as kin:
        key_byte = kin.read()
        key_int = int.from_bytes(key_byte, byteorder = 'little')

    with open(infile, mode='rb') as fin:
        while True:
            in_bytes = fin.read(8)
            in_int = int.from_bytes(in_bytes, byteorder = 'little')
            print(in_int)
            if in_int == 0:
                print("EOF")
                break

            if (mode == "e" or mode == "E"):
                print("Appending encrypted block...")
                outputs.append(present(in_int, key_int))
            elif (mode == "d" or mode == "D"):
                print("Appending decrypted block...")
                outputs.append(present_inv(in_int, key_int))
            else:
                print("Mode must be either 'e', 'E', 'd' or 'D'")

    with open(outfile, mode='wb') as fout:
    #write file
        for output in outputs:
            fout.write(output.to_bytes(8, byteorder = 'little'))

        kin.close()
        fin.close()
        fout.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile', help='input file')
    parser.add_argument('-o', dest='outfile', help='output file')
    parser.add_argument('-k', dest='keyfile', help='key file')
    parser.add_argument('-m', dest='mode', help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode=args.mode

    ecb(infile,outfile,keyfile,mode)
