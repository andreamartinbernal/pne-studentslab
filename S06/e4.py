import termcolor


DNA_BASES = ["A", "T", "C", "G"]


class Seq:
    def __init__(self, strbases):
        count = 0
        for base in DNA_BASES:
            count += strbases.count(base)

        if count == len(strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR!!"
            print("ERROR!!")

    def __len__(self):
        return len(self.strbases)

    def __str__(self):
        return self.strbases


def print_seqs(seq_list, color):
    n = 0
    for seq in seq_list:
        termcolor.cprint(f"Sequence {n} : (Length: {len(seq)}) {seq}", color)
        n += 1


def generate_seqs(pattern, number):
    seq_list = []
    seq = ""
    for i in range(number):
        seq += pattern
        seq_list.append(Seq(seq))
    return seq_list


#Main program

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)


termcolor.cprint("List 1:", 'blue')
print_seqs(seq_list1, 'blue')

print()

termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')
