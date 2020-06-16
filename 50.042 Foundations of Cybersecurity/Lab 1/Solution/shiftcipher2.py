#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# See Wan Yi Faith (1002851)
# Part 2: Shift Cipher for binary input

# Import libraries
import sys
import argparse
import string

def doStuff(filein,fileout,key,mode):
    # open file handles to both files
    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    # c    = fin.read()         # read in file into c as a str
    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode='rb') as fin:
        text = fin.read()
        bytearraytext = bytearray(text)
        # do stuff
    with open(fileout, mode='wb') as fout:
        for i in bytearraytext:
            if (mode == "e" or mode == "E"):
                encrypt(i,key,fout)
            else:
                decrypt(i,key,fout)
        fin.close()
        fout.close()

        # file will be closed automatically when interpreter reaches end of the block

def encrypt(i,key,fout):
    charout = (i + key) % 256
    fout.write(bytes([charout]))

def decrypt(i,key,fout):
    charout = (i - key) % 256
    fout.write(bytes([charout]))

# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key')
    parser.add_argument('-m', dest='mode', help='mode')

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key=int(args.key)
    mode=args.mode

    if (key >= 0 and key <= 255):
        doStuff(filein,fileout,key,mode)
    else:
        print("Key has to be >= 0 and <= 255")

    # check encryption / decryption mode
    if (mode == "e" or mode == "E" or mode == "d" or mode == "D"):
        doStuff(filein,fileout,key,mode)
    else:
        print("Mode must be either 'e', 'E', 'd' or 'D'")

    # all done
