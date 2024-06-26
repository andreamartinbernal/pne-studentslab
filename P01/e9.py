from pathlib import Path
from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")
seq = Seq()
FOLDER = "./../P00/sequences/"
FILENAME = "U5.txt"
full_filename = Path(FOLDER) / FILENAME
seq.read_fasta(full_filename)
n = 1
print(f"Sequence {n} (Length: {len(seq)}): {seq}\n\tBases: {seq.seq_count()}\n\tRev: {seq.seq_reverse()}\n\tComp: {seq.seq_complement()}")


