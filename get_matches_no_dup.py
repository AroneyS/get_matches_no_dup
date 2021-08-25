#############################
### get_matches_no_dup.py ###
#############################
# Author: Samuel Aroney
# Search pfam/tigrfam search output for matching HMM IDs

import argparse
import csv
import re
from collections import Counter


parser = argparse.ArgumentParser(description='Search pfam/tigrfam search output for matching HMM IDs.')
parser.add_argument('--fam-search', type=str, metavar='FAM TBLOUT', help='path to fam output file')
parser.add_argument('--fam-type', type=str, metavar='FAM TYPE', help='type of fam output [pfam, tigrfam]')
parser.add_argument('--hmm-list', type=str, metavar='REQ HMMS', help='path to required HMM list')
parser.add_argument('--output', type=str, metavar='OUTPUT', help='path to fam output file')

args = parser.parse_args()
fam_search_path = getattr(args, 'fam_search')
fam_type = getattr(args, 'fam_type')
HMM_id_list = getattr(args, 'hmm_list')
NEW_VERSION_HMM_COLUMN = "r202"
output_path = getattr(args, 'output')


if fam_type.lower() == "pfam":
    FAM_HMM_ID_COLUMN = 5
elif fam_type.lower() == "tigrfam":
    FAM_HMM_ID_COLUMN = 3
else:
    raise(Exception("Fam type (%s) not supported" % fam_type))


with open(HMM_id_list) as hmm_file:
    hmms = csv.DictReader(hmm_file, delimiter="\t")
    HMM_set = set(line[NEW_VERSION_HMM_COLUMN] for line in hmms)


with open(fam_search_path) as input_file, open(output_path, 'w') as output_file:
    input = csv.reader(input_file, delimiter="\t")
    output = csv.writer(output_file, delimiter="\t")

    match_list = []
    for line in input:
        if len(line)>0 and not line[0].startswith("#"):
            line_split = re.split('\s{1,}', line[0])
            if line_split[FAM_HMM_ID_COLUMN] in HMM_set:
                match_list.append([line_split[i] for i in [0, FAM_HMM_ID_COLUMN]])

    c = Counter([hmm_id for _,hmm_id in match_list])
    output_list = [[seq_id,hmm_id] for seq_id,hmm_id in match_list if c[hmm_id] == 1]

    output.writerows(output_list)

