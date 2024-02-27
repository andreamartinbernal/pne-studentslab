from Seq1 import *
print("-----| Practice 1, Exercise 7 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")

print(f'Sequence 1: (Length: {seq1.seq_len()}) {seq1.seq}')
print('Bases:',  seq1.seq_count())
print('Rev:', seq1.seq_reverse())

print(f'Sequence 2: (Length: {seq2.seq_len()}) {seq2.seq}')
print('Bases:',  seq2.seq_count())
print('Rev:', seq2.seq_reverse())

print(f'Sequence 3: (Length: {seq3.seq_len()}) {seq3.seq}')
print('Bases:',  seq3.seq_count())
print('Rev:', seq3.seq_reverse())