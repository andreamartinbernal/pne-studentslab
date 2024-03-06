from Seq1 import *
from Client0 import Client
PRACTICE = 2
EXERCISE = 5
IP = "192.168.1.39"
PORT = 8080

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
# -- Create a client object
c = Client(IP, PORT)
print(c)
seq = Seq()
FOLDER = "./../P00/sequences/"
FILENAME = "FRAT1.txt"
full_filename = Path(FOLDER) / FILENAME
seq.read_fasta(full_filename)
print("Gene FRAT1:", str(seq))

response = c.talk("Sending FRAT1 Gene, in fragments of 10 bases...")
fragment = ""
nb_of_fragment = 0
for base in str(seq)[:50]:
    fragment += base
    if len(fragment) == 10:
        nb_of_fragment += 1
        print("Fragment", nb_of_fragment ,":", fragment)
        c = Client(IP, PORT)
        c.talk(fragment)
        fragment = ""



