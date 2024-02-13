from pathlib import Path
from Seq0 import *

FOLDER = "./sequences/"
FILENAME = "U5.txt"
full_filename = Path(FOLDER) / FILENAME
complete_seq = seq_read_fasta(full_filename)
print("DNA file:", FILENAME)
print("The first 20 bases are: ")
print(complete_seq[0:20])



