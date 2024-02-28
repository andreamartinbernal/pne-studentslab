from Seq1 import *
print("-----| Practice 1, Exercise 8 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")
seq_list = [seq1, seq2, seq3]
for seq in seq_list:
    print(f"Sequence 1 (Length: {len(seq)}): {seq}\n\tBases: {seq.seq_count()}\n\tRev: {seq.seq_reverse()}\n\tComp: {seq.seq_complement()}")
