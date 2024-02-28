from Seq1 import *
print("-----| Practice 1, Exercise 4 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")

seq_list = [seq1, seq2, seq3]
num_seq = 1
for seq in seq_list:
    print(f'Sequence {num_seq}: (Length: {seq.seq_len()}) {seq.strbases}')
    num_seq += 1

