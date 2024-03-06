from Seq1 import *
from Client0 import Client
PRACTICE = 2
EXERCISE = 4
IP = "192.168.1.39"
PORT = 8080

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
# -- Create a client object
c = Client(IP, PORT)
print(c)

FOLDER = "./../P00/sequences/"
FILENAMES = ["U5.txt", "ADA.txt", "FRAT1.txt", "FXN.txt", "RNU6_1155P.txt"]

for filename in FILENAMES:
    full_filename = Path(FOLDER) / filename
    seq = Seq()
    seq.read_fasta(full_filename)
    msg_to_send = f"Sending {filename.replace('.txt', '')} to the server..."
    print("To server:", msg_to_send)
    response = c.talk(msg_to_send)
    print(f"From server: {response}")
    msg_to_send = str(seq)
    print("To server:", msg_to_send)
    response = c.talk(msg_to_send)
    print(f"From server: {response}")