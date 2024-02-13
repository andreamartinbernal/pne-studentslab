from pathlib import Path

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

def len_seq(seq):
    len_seq = len(seq)
    return len_seq
#without dicts
def number_of_bases(seq):
    numberA = 0
    numberC = 0
    numberG = 0
    numberT = 0
    #secToProcess = seq_X51501 . replace(">X51501.1 H.sapiens GPIPI gene, exon 1 (and joined CDS)" , "")
    secToProcess = ""
    for character in secToProcess:
        if character == "A":
            numberA += 1
        elif character == "C":
            numberC += 1
        elif character == "G":
            numberG += 1
        elif character == "T":
            numberT += 1
    print("Number of times that letter 'A' appears in the sentence:",numberA)
    print("Number of times that letter 'C' appears in the sentence:",numberC)
    print("Number of times that letter 'G' appears in the sentence:",numberG)
    print("Number of times that letter 'T' appears in the sentence:",numberT)


def get_bases_count(dna_sequence):
    bases_dna = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in bases_dna:
        bases_dna[base] = dna_sequence.count(base)
    return bases_dna

def seq_complement(seq):
    for i in seq:
        if i == "A":
            i="T"
        if i == "T":
            i="A"
        if i == "C":
            i="G"
        if i == "G":
            i="C"
    return seq