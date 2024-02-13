from pathlib import Path
from Seq0 import *

FOLDER = "./sequences/"
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
print("-----| Exercise 3 |-------")
for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    complete_seq = seq_read_fasta(full_filename)
    print("Gene", filename.replace(".txt", ""), "-> Length:", seq_len(complete_seq))
