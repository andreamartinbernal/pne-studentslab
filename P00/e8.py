from pathlib import Path
from Seq0 import *
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt"]
FOLDER = "./sequences/"
print("-----| Exercise 8 |------")
for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    complete_seq = seq_read_fasta(full_filename)
    bases_count_dict = seq_count(complete_seq)
    most_frequent_base = ""
    max_nb_occurrences = 0
    for base in bases_count_dict:
        if bases_count_dict[base] > max_nb_occurrences:
            max_nb_occurrences = bases_count_dict[base]
            most_frequent_base = base
    print(f"Gene {filename.replace(".txt", "")}: Most frequent Base: {most_frequent_base}")
