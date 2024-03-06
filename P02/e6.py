from Seq1 import *
from Client0 import Client
PRACTICE = 2
EXERCISE = 6
IP_1 = "192.168.1.39"
PORT_1 = 8080
IP_2 = "192.168.1.39"
PORT_2 = 8081

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

seq = Seq()
FOLDER = "./../P00/sequences/"
FILENAME = "FRAT1.txt"
full_filename = Path(FOLDER) / FILENAME
seq.read_fasta(full_filename)
print("Gene FRAT1:", str(seq))
fragment = ""
nb_of_fragment = 0
for base in str(seq)[:100]:
    fragment += base
    if len(fragment) == 10:
        nb_of_fragment += 1
        print("Fragment", nb_of_fragment, ":", fragment)
        if nb_of_fragment % 2 == 0:
            c = Client(IP_1, PORT_1)
            c.talk(fragment)
        else:
            c = Client(IP_2, PORT_2)
            c.talk(fragment)
        fragment = ""