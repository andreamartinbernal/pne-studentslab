from pathlib import Path
from Seq1 import *
print("-----| Practice 1, Exercise 10 |------")
FOLDER = "./../P00/sequences/"
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_1155P.txt"]

for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    seq = Seq()
    seq.read_fasta(full_filename)
    bases_count_dict = seq.seq_count()
    most_frequent_base = ""
    max_nb_occurrences = 0
    for base in bases_count_dict:
        if bases_count_dict[base] > max_nb_occurrences:
            max_nb_occurrences = bases_count_dict[base]
            most_frequent_base = base

    print(f"Gene {filename.replace('.txt','')}: Most frequent Base: {most_frequent_base}")