#!/usr/bin/env python3
# ECB plaintext extraction
# SUTD 50.042 FCS Lab 4
# See Wan Yi Faith (1002851)

import argparse

def getInfo(headerfile):
    with open(headerfile, mode='rb') as fin:
        info = fin.read()
        # print(info)
        fin.close()
    return info

def extract(infile,outfile,headerfile):

    header_info = getInfo(headerfile)
    frequency_dict = {}

    with open(infile, mode='rb') as finfile:
        #ignore the first few characters which represent the header
        # finfile.read(len(header_info))
        with open(outfile, mode='wb') as fout:
            finfile.read(len(header_info))
            fout.write(header_info)
            fout.write(b'\n')

            while True:
                bytes = finfile.read(8)
                # print("Reading bytes...")

                # determining EOF
                # print(bytes)
                if  bytes == b'':
                    print("EOF, done!")
                    break

                #frequency analysis
                if bytes in frequency_dict:
                    frequency_dict[bytes] += 1
                else:
                    frequency_dict[bytes] = 1

                frequency_dict_sorted = sorted(frequency_dict, key = frequency_dict.get, reverse = True)

                if bytes == frequency_dict_sorted[0]:
                    fout.write(b'00000000')
                else:
                    fout.write(b'11111111')

        fout.close()
    finfile.close()

# def extract(infile,outfile,headerfile):
#
#     header_info = getInfo(headerfile)
#     frequency_dict = {}
#
#     with open(infile, mode='rb') as finfile:
#         #ignore the first few characters which represent the header
#         finfile.read(len(header_info))
#
#         while True:
#             bytes = finfile.read(8)
#
#             # determining EOF
#             # print(bytes)
#             if  bytes == b'':
#                 print("EOF")
#                 break
#
#             #frequency analysis
#             if bytes in frequency_dict:
#                 frequency_dict[bytes] += 1
#             else:
#                 frequency_dict[bytes] = 1
#
#         finfile.close()
#
#     frequency_dict_sorted = sorted(frequency_dict, key = frequency_dict.get, reverse = True)
#
#     with open(infile, mode='rb') as finfile:
#         #ignore the first few characters which represent the header
#         # finfile.read(len(header_info))
#         with open(outfile, mode='wb') as fout:
#             finfile.read(len(header_info))
#             fout.write(header_info)
#             fout.write(b'\n')
#
#             while True:
#                 bytes = finfile.read(8)
#
#                 # determining EOF
#                 # print(bytes)
#                 if  bytes == b'':
#                     print("EOF")
#                     break
#
#                 if bytes == frequency_dict_sorted[0]:
#                     fout.write(b'00000000')
#                 else:
#                     fout.write(b'11111111')
#
#         fout.close()
#     finfile.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Reading from: %s'%infile)
    print('Reading header file from: %s'%headerfile)
    print('Writing to: %s'%outfile)

    # success=extract(infile,outfile,headerfile)
    extract(infile,outfile,headerfile)
