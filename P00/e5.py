from pathlib import Path
from Seq0 import *
DNA_BASES = ["A", "C", "T", "G"]
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
print("-----| Exercise 5 |------")
for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    complete_seq = seq_read_fasta(full_filename)
    bases_count_dict = seq_count(complete_seq)
    print(f"Gene {filename.replace(".txt", "")}: {bases_count_dict}")
