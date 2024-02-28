from pathlib import Path
from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")
seq = Seq()
FOLDER = "./sequence/"
FILENAME = "U5.txt"
full_filename = Path(FOLDER) / FILENAME
seq.read_fasta(full_filename)
print(f"Sequence 1 (Length: {len(seq)}): {seq}\n\tBases: {seq.seq_count()}\n\tRev: {seq.seq_reverse()}\n\tComp: {seq.seq_complement()}")


