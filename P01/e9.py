from pathlib import Path
from Seq1 import *
print("-----| Practice 1, Exercise 9 |------")


print(f'Sequence: (Length: {FILENAME.seq_len()}) {seq1.seq}')
print('Bases:',  seq1.seq_count())
print('Rev:', seq1.seq_reverse())
print('Complement: ', seq1.seq_complement())

print(f'Sequence 2: (Length: {seq2.seq_len()}) {seq2.seq}')
print('Bases:',  seq2.seq_count())
print('Rev:', seq2.seq_reverse())
print('Complement: ', seq2.seq_complement())

print(f'Sequence 3: (Length: {seq3.seq_len()}) {seq3.seq}')
print('Bases:',  seq3.seq_count())
print('Rev:', seq3.seq_reverse())
print('Complement: ', seq3.seq_complement())
FOLDER = "./sequences/"
FILENAME = "U5.txt"
full_filename = Path(FOLDER) / FILENAME
complete_seq = seq_read_fasta(full_filename)
print("DNA file:", FILENAME)
for base in complete_seq:
    print(base)
