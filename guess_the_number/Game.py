import socket
total_attempts = 0
from class_NumberGuesser import *
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        print("CLIENT: ", cs, "-", client_ip_port)

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()
        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        chosen_number = msg_raw.decode()
        try:
            guess_number_return_code = chosen_number.guess_number(chosen_number)
            if guess_number_return_code == 0:
                msg_to_send = (f"You won after {total_attempts} attempts!")
            elif guess_number_return_code == 2:
                msg_to_send = ("LOWER, but well tried")
            else:
                msg_to_send = "HIGHER, but well tried"

        except TypeError:
            print("Type error, enter an integer")
            ls.close()
            exit()

