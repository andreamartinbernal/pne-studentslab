from pathlib import Path

DNA_BASES = ["A", "T", "C", "G"]
COMPLEMENTARY_BASES = {"A": "T", "C": "G", "G": "C", "T": "A"}
FILENAMES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_1155P"]
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

    def is_ok(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return False
        else:
            return True

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
        return len(self)

    def seq_count(self):
        bases_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return bases_dict
        else:
            length = self.seq_len()
            if length != 0:
                for base in self.strbases:
                    bases_dict[base] += 1
            return bases_dict

    def seq_reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complementary_seq = ""
            for base in self.strbases:
                complementary_seq += COMPLEMENTARY_BASES[base]
            return complementary_seq

    def read_fasta(self, filename):
        with open(filename, "r") as f:
            if filename in FILENAMES:
                file_contents = Path(filename).read_text()
                list_contents = file_contents.split("\n")
                complete_seq = ""
                wrong_seq = ""
                for i in range(1, len(list_contents)):
                    if i == "A" or i =="C" or i == "G" or i == "T":
                        complete_seq += (list_contents[i])
                    wrong_seq += (list_contents[i])
                    f.close()
                    if len(wrong_seq) == len(complete_seq):
                        self.strbases = "ERROR"
                    else:
                        self.strbases = complete_seq
                return self.strbases
            else:
                self.strbases = "ERROR"
                return self.strbases





