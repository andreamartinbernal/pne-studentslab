from Seq1 import *
print("-----| Practice 1, Exercise 8 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")

print(f'Sequence 1: (Length: {seq1.seq_len()}) {seq1.seq}')
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

####################################
from Seq1 import Seq
print("\n--- Exercise 8 | Practice 1 ---\n")
s1 = Seq("AGCAGATAGCTGATCGT")
s2 = Seq()
s3 = Seq("Invalid sequence")

print(f"\nSequence 1 (Length: {seq1.len()}): {seq1}\n\tBases: {seq1.count()}\n\tRev: {seq1.reverse()}\n\tComp: {seq1.complement()}\n")
print(f"Sequence 2 (Length: {seq2.len()}): {seq2}\n\tBases: {seq2.count()}\n\tRev: {seq2.reverse()}\n\tComp: {seq2.complement()}\n")
print(f"Sequence 3 (Length: {seq3.len()}): {seq3}\n\tBases: {seq3.count()}\n\tRev: {seq3.reverse()}\n\tComp: {seq3.complement()}")