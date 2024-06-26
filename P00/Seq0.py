from pathlib import Path
DNA_BASES = ["A", "C", "T", "G"]
COMPLEMENTARY_BASES = {"A": "T", "C": "G", "G": "C", "T": "A"}

def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    with open(filename, "r") as f:
        file_contents = Path(filename).read_text()
        list_contents = file_contents.split("\n")
        complete_seq = ""
        for i in range(1, len(list_contents)):
            complete_seq += (list_contents[i])
        f.close()
    return complete_seq


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    number = 0
    for each_base in seq:
        if each_base == base:
            number += 1
    return number


def seq_count(seq):
    bases_dna = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in DNA_BASES:
        bases_dna[base] = seq_count_base(seq, base)
    return bases_dna


def seq_reverse(seq, n):
    return seq[:n][::-1]


def seq_complement(seq):
    complementary_seq = ""
    for base in seq:
        complementary_seq += COMPLEMENTARY_BASES[base]
    return complementary_seq