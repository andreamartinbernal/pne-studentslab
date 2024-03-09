import socket
from pathlib import Path
from Seq2 import *

SEQ_LIST = ["ACGTGG", "AAGTGG", "AAATGG", "AAAAGG", "AAAAAG"]
CONCATENATED_SEQUENCE = ""


def type_seq(seq):
    if not len((seq.remove("A").remove("C").remove("G").remove("T")) == 0):
        return 1
    else:
        return 0


def get_info_from_seq(seq):
    seq = Seq(seq)
    nb_of_each_base = seq.seq_count()
    seq_length = len(seq)
    info_str = f"\nSequence: {seq}\nTotal length: {seq_length}\n"
    for key, number in nb_of_each_base.items():
        info_str += f"{key}: {number} ({round(number/seq_length*100, 1)}%)\n"
    return info_str


def get_comp_from_seq(seq):
    seq = Seq(seq)
    complement_seq = seq.seq_complement()
    return complement_seq


def get_rev_from_seq(seq):
    seq = Seq(seq)
    reverse_seq = seq.seq_reverse()
    return reverse_seq


def get_seq_from_file(seq_name):
    seq = Seq()
    FOLDER = "./../P00/sequences/"
    FILENAME = f"{seq_name}.txt"
    full_filename = Path(FOLDER) / FILENAME
    seq.read_fasta(full_filename)
    return str(seq)
def add_sequence(seq):
    if seq not in SEQ_LIST:
        SEQ_LIST.append(seq)
        return 1
    return 0

def concat_DNA_string(seq1, seq2):
    if seq1.is_ok() is True and seq2.is_ok() is True:
        return 1
    else:
        return 0




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
            cs.send("OK".encode())
        elif "GET" in msg:
            print("GET")
            nb_of_requested_seqs = int(msg.split(" ")[1])
            msg_to_send = SEQ_LIST[nb_of_requested_seqs]
            print(msg_to_send)
            cs.send(msg_to_send.encode())
        elif "INFO" in msg:
            print("INFO")
            nb_seq = msg.split(" ")[1]
            info_from_seq = get_info_from_seq(nb_seq)
            print(info_from_seq)
            cs.send(info_from_seq.encode())
        elif "COMP" in msg:
            print("COMP")
            seq = msg.split(" ")[1]
            seq = type_seq(seq)
            if seq == 1:
                msg_to_send = "Not valid sequence"
                cs.send(msg_to_send.encode())
                ls.close()
            else:
                comp_from_seq = get_comp_from_seq(seq)
                print(comp_from_seq)
                cs.send(comp_from_seq.encode())
        elif "REV" in msg:
            print("REV")
            seq = msg.split(" ")[1]
            seq = type_seq(seq)
            if seq == 1:
                msg_to_send = "Not valid sequence"
                cs.send(msg_to_send.encode())
                ls.close()
            else:
                rev_from_seq = get_rev_from_seq(seq)
                print(rev_from_seq)
                cs.send(rev_from_seq.encode())
        elif "GENE" in msg:
            print("GENE")
            seq_name = msg.split(" ")[1]
            seq_from_file = get_seq_from_file(seq_name)
            print(seq_from_file)
            cs.send(seq_from_file.encode())

#################################################33

        elif "LIST" in msg:
            print("LIST")
            nb_seq = 0
            for seq in SEQ_LIST:
                seq = type_seq(seq)
                if seq == 1:
                    msg_to_send = "Not valid sequence"
                    cs.send(msg_to_send.encode())
                    ls.close()
                else:
                    nb_seq += 1
                    cs.send(seq.encode())

        elif "ADD" in msg:
            print("ADD")
            seq = msg.split(" ")[1]
            seq = type_seq(seq)
            if seq == 0:
                msg_to_send = "Not valid sequence"
                cs.send(msg_to_send.encode())
                ls.close()
            else:
                return_code = add_sequence(seq)
                if return_code == 1:
                    print("Succesfully added")
                    msg_to_send = "Succesfully added"
                else:
                    print("Something went wrong")
                    msg_to_send = "Something went wrong"
                cs.send(msg_to_send.encode())
        elif "CONCATENATE" in msg:
            print("CONCATENATE")
            seq1 = msg.split(" ")[1]
            seq2 = msg.split(" ")[3]
            seq1 = type_seq(seq)
            seq2 = type_seq(seq)
            if seq1 == 0 or seq2 == 0:
                msg_to_send = "Not valid sequence"
                cs.send(msg_to_send.encode())
                ls.close()
            else:
                return_code = concat_DNA_string(seq1, seq2)
                if return_code == 1:
                    print("Succesfully added")
                    msg_to_send = "Succesfully added"
                else:
                    print("Something went wrong")
                    msg_to_send = "Something went wrong"
                cs.send(msg_to_send.encode())

        else:
            error_msg = "Unexpected command"
            print(error_msg)
            cs.send(error_msg.encode())

        # -- Close the data socket
        cs.close()