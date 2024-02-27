from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")

print(f'Sequence 1: (Length: {seq1.seq_len()}) {seq1.seq}')
print(' A:', (seq1.seq_count())['A'], ' T', (seq1.seq_count())['T'],' C:', (seq1.seq_count())['C'], ' G:', (seq1.seq_count())['G'])

print(f'Sequence 2: (Length: {seq2.seq_len()}) {seq2.seq}')
print(' A:', (seq2.seq_count())['A'], ' T', (seq2.seq_count())['T'],' C:', (seq2.seq_count())['C'], ' G:', (seq2.seq_count())['G'])


print(f'Sequence 3: (Length: {seq3.seq_len()}) {seq3.seq}')
print(' A:', (seq3.seq_count())['A'], ' T', (seq3.seq_count())['T'],' C:', (seq3.seq_count())['C'], ' G:', (seq3.seq_count())['G'])


