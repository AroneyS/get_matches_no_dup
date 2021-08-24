#############################
### get_matches_no_dup.py ###
#############################
# Author: Samuel Aroney
# Search pfam/tigrfam search output for matching HMM IDs

import argparse

parser = argparse.ArgumentParser(description='Search pfam/tigrfam search output for matching HMM IDs.')
parser.add_argument('--fam-search', type=str, metavar='FAM TBLOUT', help='path to fam output file')
parser.add_argument('--fam-type', type=str, metavar='FAM TYPE', help='type of fam output [pfam, tigrfam]')
parser.add_argument('--hmm-list', type=str, metavar='REQ HMMS', help='path to required HMM list')
parser.add_argument('--output', type=str, metavar='OUTPUT', help='path to fam output file')

args = parser.parse_args()
fam_search_file = getattr(args, 'fam-search')
fam_type = getattr(args, 'fam-type')
HMM_id_list = getattr(args, 'hmm-list')
output_file = getattr(args, 'output') # or STDOUT

# check output non-existant?

with open(fam_search_file) as input, open(output_file, 'a') as output:
    while True:
        line = input.readline()

        if not line:
            break

        if not line.startswith('#'):
            if False:
                output.write(line)

