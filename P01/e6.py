from Seq1 import *
print("-----| Practice 1, Exercise 6 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")
seq_list = [seq1, seq2, seq3]
n = 1
for seq in seq_list:
    print(f'Sequence {n}: (Length: {seq.seq_len()}) {seq.strbases}\nBases:,  {seq.seq_count()}')
    n += 1
