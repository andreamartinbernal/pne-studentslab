from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)


print(c)
print("Sending a message to the server...")
response = c.talk("GET 0")
print(f"Response: {response}")
