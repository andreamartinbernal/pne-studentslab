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


############################################
print("\n* Testing LIST...")
response = c.talk("LIST")
for seq in SEQ_LIST:
    print(seq)

print("\n* Testing ADD...")
print(f"Adding {seq} to the list")
response = c.talk("ADD AAAAGG")
print(response)
response = c.talk("")

print("\n* Testing CONCATENATE str...")
print(f"Adding {seq1} to {seq2}")
response = c.talk("CONCATENATE AAAAGG and ACGTTC")
print(response)
response = c.talk("")

print("\n* Testing CONCATENATE Seq...")
print(f"Adding {seq1} to {seq2}")
response = c.talk("CONCATENATE AAAAGG and ACGTTC")
print(response)
response = c.talk("")