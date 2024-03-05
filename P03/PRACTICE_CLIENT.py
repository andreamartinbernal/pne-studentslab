import socket
from Client0 import *

PRACTICE = 3
EXERCISE = 7
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

# -- Create a client object
SEQ_LIST = ["ACGTGG", "AAGTGG", "AAATGG", "AAAAGG", "AAAAAG"]
c = Client(IP, PORT)
print("\n* Testing PING...")
response = c.talk("PING")
print(response)
print("\n* Testing GET...")

for i in range(0, 5):
    response = c.talk(f"GET {i}")
    print(f"GET {i}: {response}")
print("\n* Testing INFO...")
response = c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(response)
print("\n* Testing COMP...")
response = c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(response)
print("\n* Testing REV...")
response = c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(response, "")
print("\n* Testing GENE...")
for name in ["U5", "ADA", "FRAT1", "FXN", "RNU6_1155P"]:
    print(f"\nGENE {name}")
    response = c.talk(f"GENE {name}")
    print(response)
print("\n* Testing ADD...")
seq1 = cs.decode(seq1)
seq2 = "ACGTGGG"
print("Adding", seq1, "and", seq2, "to the list")
for sequence in SEQ_LIST:
    if seq1 == sequence and (len(seq1) == len(sequence)):
        response = c.talk("The sequence:", seq1, "is already on the list")
        print(response)
    if seq2 == sequence and (len(seq2) == len(sequence)):
        response = c.talk("The sequence:", seq2, "is already on the list")
        print(response)
    else:
        SEQ_LIST = SEQ_LIST.append(seq1)
        SEQ_LIST = SEQ_LIST.append(seq2)
        response = c.talk("The resultance sequence list is:", SEQ_LIST)

response = c.talk("")