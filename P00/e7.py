from pathlib import Path
from Seq0 import *

FOLDER = "./sequences/"
FILENAME = "U5.txt"
full_filename = Path(FOLDER) / FILENAME
complete_seq = seq_read_fasta(full_filename)
print("-----| Exercise 7 |------")
print("Gene U5")
print("Frag:\t", complete_seq[0:20])
print("Comp:\t",  seq_complement(complete_seq[0:20]))
