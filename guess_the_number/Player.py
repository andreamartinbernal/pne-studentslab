import socket
from ClassClient import *


# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080
c = Client(IP, PORT)
chosen_number = "10"
print(f"I'm going to try with {chosen_number}")
response = c.talk(chosen_number)
print(response)