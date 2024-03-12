import socket
class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def ping(self):
        print("OK")
    def __str__(self):
        return f"Connection to SERVER at IP: {self.ip}, PORT: {self.port}"
    def talk(self, msg_to_send):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg_to_send))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response
