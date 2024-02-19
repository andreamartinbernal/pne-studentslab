#exercice 1
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
#You can also use a for loop and if it is different than the four bases it is error

    def __str__(self):
        return self.strbases



s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")