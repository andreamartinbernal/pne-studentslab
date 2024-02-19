DNA_BASES = ["A", "T", "C", "G"]

def print_seqs(seq_list):
    n = 0
    for seq in seq_list:
        print(f"Sequence {n} : (Length: {len(seq)}) {seq}")
        n += 1


def generate_seqs(pattern, number):
    seq_list = []
    seq = ""
    for i in range(number):
        seq += pattern
        seq_list.append(Seq(seq))
    return seq_list


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
