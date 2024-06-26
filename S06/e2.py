#ejercicio 2

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        print("New list created!")

    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(self.strbases)


def print_seqs(seq_list):
    n = 0
    for seq in seq_list:
        print(f"Sequence {n} : (Length: {len(seq)}) {seq}")
        n += 1


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

print_seqs(seq_list)
