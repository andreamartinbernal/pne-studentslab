DNA_BASES = ["A", "T", "C", "G"]
COMPLEMENTARY_BASES = {"A": "T", "C": "G", "G": "C", "T": "A"}

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


    def __len__(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)


    def __str__(self):
        return self.strbases

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            number = 0
            for each_base in self.strbases:
                if each_base == base:
                    number += 1
            return number

    def seq_len(self):
        if self.strbases == None or self.strbases == 'ERROR':
            length = 0
        else:
            length = len(self.strbases)
        return length

    def seq_count(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            length = self.seq_len()
            bases_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
            if length != 0:
                for base in self.strbases:
                    bases_dict[base] += 1
            return bases_dict

    def seq_reverse(self, seq_len):
        return self.strbases[:seq_len][::-1]

    def seq_complement(self, seq):
        complementary_seq = ""
        for base in seq:
            complementary_seq += COMPLEMENTARY_BASES[base]
        return complementary_seq

    def seq_read_fasta(self, filename):
        with open(filename, "r") as f:
            file_contents = Path(filename).read_text()
            list_contents = file_contents.split("\n")
            complete_seq = ""
            for i in range(1, len(list_contents)):
                complete_seq += (list_contents[i])
            f.close()
        return complete_seq

    def reverse(self):
        if self.strbases == None:
            return "NULL"
        else:
            for i in self.strbases:
                if i == "A" or i == "C" or i == "T" or i == "G":
                    seq_n = self.strbases[:len(self.strbases)]
                    return seq_n[::-1]
                else:
                    return "ERROR"

    def complement(self):
        complement = ""
        if self.strbases == None:
            return "NULL"
        else:
            for base in self.strbases:
                if base == "A":
                    complement += "T"
                elif base == "G":
                    complement += "C"
                elif base == "C":
                    complement += "G"
                elif base == "T":
                    complement += "A"
                else:
                    return "ERROR"
        return complement

