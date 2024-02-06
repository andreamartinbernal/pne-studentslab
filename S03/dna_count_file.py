def get_dna_sequence(filename):
    with open("dna_file.txt", "r") as f:
        complete_seq = f.read().replace("\n", "")
        f.close()
    return complete_seq


def get_bases_count(dna_sequence):
    bases_dna = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in bases_dna:
        bases_dna[base] = dna_sequence.count(base)
    return bases_dna


#The main program starts here

filename = "dna_file.txt"
dna_sequence = get_dna_sequence(filename)
bases_count = get_bases_count(dna_sequence)
print("The resultant sequence is: ", dna_sequence)
print("------------------------------")
print("The present bases of the sequence are: ")
total_bases = 0
for base, value in bases_count.items():
    if value != 0:
        print(f"{base} : {value} times")
        total_bases += value
print("------------------------------")
print("The total number of bases is: ", total_bases)

