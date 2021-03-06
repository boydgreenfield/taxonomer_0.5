import argparse
from Bio import SeqIO
import math
import numpy as np

parser = argparse.ArgumentParser(description="Calculate effective lengths of sequences")
parser.add_argument("fasta_file", type=str, help="fasta file of reference sequences")
args = parser.parse_args()

n_records = 0
record_lens = []

handle = open(args.fasta_file,'r')
for record in SeqIO.parse(handle, "fasta"):
    n_records += 1
    record_lens.append(len(record.seq))
handle.close()

print "n seqs: %d"%(n_records)
print "mean length: %f"%(np.mean(record_lens))
print "median length: %f"%(np.median(record_lens))
print "stdev seq length: %f"%(np.std(record_lens))
print "min, max: %d, %d"%(np.min(record_lens),np.max(record_lens))


