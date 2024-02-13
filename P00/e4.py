from pathlib import Path
from Seq0 import *
DNA_BASES = ["A", "C", "T", "G"]
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
print("-----| Exercise 4 |------")
for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    complete_seq = seq_read_fasta(full_filename)
    print(f"Gene {filename.replace(".txt", "")}:")
    for base in DNA_BASES:
        print(f"{base}: {seq_count_base(complete_seq, base)}")
    print()
