from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")

print(f'Sequence 1: (Length: {seq1.seq_len()}) {seq1.strbases}')
print(' A:', seq1.count_base('A'), ' T:', seq1.count_base('T'),' C:', seq1.count_base('C'), ' G:', seq1.count_base('G'))

print(f'Sequence 2: (Length: {seq2.seq_len()}) {seq2.strbases}')
print(' A:', seq2.count_base('A'), ' T:', seq2.count_base('T'),' C:', seq2.count_base('C'), ' G:', seq2.count_base('G'))


print(f'Sequence 3: (Length: {seq3.seq_len()}) {seq3.strbases}')
print(' A:', seq3.count_base('A'), ' T:', seq3.count_base('T'),' C:', seq3.count_base('C'), ' G:', seq3.count_base('G'))


