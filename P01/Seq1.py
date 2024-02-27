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
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            count = 0
            for base in DNA_BASES:
                count += strbases.count(base)

            if count == len(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                print("INVALID sequence created")
                self.strbases = "ERROR"


    def __len__(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)


    def __str__(self):
        return self.strbases

    def count_base(self, base):
        number = 0
        for each_base in self.strbases.split():
            if each_base == base:
                number += 1
        return number

    def seq_len(self):
        if self.seq == None or self.seq == 'ERROR':
            length = 0
        else:
            length = len(self.seq)
        return length

    def seq_count(self):
        length = self.seq_len()
        bases_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if length != 0:
            for base in self.seq:
                bases_dict[base] += 1
        return bases_dict



