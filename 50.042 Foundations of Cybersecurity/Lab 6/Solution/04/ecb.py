#!/usr/bin/env python3
# ECB wrapper skeleton file for 50.042 FCS
# This code is written by Wong Chi Seng
# My Lab 4 appears to have errors, thus to complete Lab 6, I have used his Lab 4 code

from present import *
import argparse

nokeybits=80
blocksize=64

'''
Read file in chunks of 8 bytes
'''
def ecb(infile,outfile,mode):
    key=0xFFFFFFFFFFFFFFFFFFFF
    if mode == 'e':
        with open(outfile, 'wb') as fout:
            with open(infile, 'rb') as fin:
                output = fin.read(8)
                while output:
                    to_encr = int.from_bytes(output, "little")
                    encr = present(to_encr,key)
                    fout.write(encr.to_bytes(8, byteorder='little', signed=False))
                    output = fin.read(8)
            fin.close()
        fout.close()

    if mode == 'd':
        with open(outfile, 'wb') as fout:
            with open(infile, 'rb') as fin:
                output = fin.read(8)
                while output:
                    to_decr = int.from_bytes(output, "little")
                    decr = present_inv(to_decr,key)
                    fout.write(decr.to_bytes(8, byteorder='little', signed=False))
                    output = fin.read(8)
            fin.close()
        fout.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile
    mode = args.mode
    ecb(infile, outfile, mode)
