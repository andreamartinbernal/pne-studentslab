import socket
SEQ_LIST = ["ACGTGG", "AAGTGG", "AAATGG", "AAAAGG", "AAAAAG"]


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
        msg = msg_raw.decode()
        if msg == "PING":
            print("PING command!")
        elif "GET" in msg:
            print("GET")
            nb_of_requested_seqs = int(msg.split(" ")[1])
            msg_to_send = SEQ_LIST[nb_of_requested_seqs]
            print(msg_to_send)
            cs.send(msg_to_send.encode())


        # -- Print the received message
        #print(f"Message received: {msg}")

        # -- Send a response message to the client
        #response = "HELLO. I am the Happy Server :-)\n"

        # -- The message has to be encoded into bytes
        #cs.send(response.encode())

        # -- Close the data socket
        cs.close()