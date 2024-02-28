from Seq1 import *
print("-----| Practice 1, Exercise 5 |------")
seq1 = Seq()
seq2 = Seq("TATAC")
seq3 = Seq("TATAX")
seq_list = [seq1, seq2, seq3]

for seq in seq_list:
    print(f"\nSequence {seq} (Length: {seq.seq_len()}) {seq.strbases}'\n\tA: {seq.count_base('A')},  T: {seq.count_base('T')},  C: {seq.count_base('C')},  G: {seq.count_base('G')}")
