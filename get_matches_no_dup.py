#############################
### get_matches_no_dup.py ###
#############################
# Author: Samuel Aroney
# Search pfam/tigrfam search output for matching HMM IDs

import argparse

parser = argparse.ArgumentParser(description='Search pfam/tigrfam search output for matching HMM IDs.')
parser.add_argument('-i', type=str, default='interleaved.fq',
                    metavar='INPUT', help='path to input file')
parser.add_argument('-1', type=str, default='read1.fq',
                    metavar='OUTPUT1', help='path to read 1 output file')
parser.add_argument('-2', type=str, default='read2.fq',
                    metavar='OUTPUT2', help='path to read 2 output file')

args = parser.parse_args()
input_path = getattr(args, 'i')
output1_path = getattr(args, '1')
output2_path = getattr(args, '2')

with open(input_path) as input, open(output1_path, 'a') as output1, open(output2_path, 'a') as output2:
    while True:
        line = input.readline()

        if not line:
            break

        # ID row starts with @ symbol
        if line.startswith('@'):
            # check ending of ID row for read indicator (/1 or /2)
            if line.strip().endswith('/1'):
                output1.write(line)
                output1.write(input.readline())
                output1.write(input.readline())
                output1.write(input.readline())
            elif line.strip().endswith('/2'):
                output2.write(line)
                output2.write(input.readline())
                output2.write(input.readline())
                output2.write(input.readline())


