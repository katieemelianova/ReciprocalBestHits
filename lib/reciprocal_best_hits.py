import sys
import os
import argparse
from string import ascii_lowercase
sys.path.append(os.path.abspath(".."))
from lib.utilities import *

def encode_fasta_headers(fasta_list):
    for i in range(len(fasta_list)):
        letter_code = ascii_lowercase[i].upper()
        fasta_dict = fastaDict(fasta_list[i])
        new_keys = ['_'.join([letter_code, i]) for i in list(fasta_dict.keys())]
        values = list(fasta_dict.values())
        new_dict = dict(zip(new_keys, values))
        new_filename = '_'.join([(os.path.splitext(fasta_list[i])[0]), 'encoded'])
        with open(new_filename, "w") as write_file:
            for entry in new_dict:
                # put into utilities a dict to fasta functon
                write_file.write('\n'.join(['>' + entry, new_dict[entry], '\n']))




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fasta', required=True, nargs='+', help="provide at least two fasta file paths")
    args = parser.parse_args()
    encode_fasta_headers(args.fasta)



if __name__ == '__main__':
    main()
