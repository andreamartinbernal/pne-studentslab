from Seq1 import *
import http.client
import json
import termcolor

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"}

gene_list = list(genes.keys())

correct = False
while not correct:
    for gene_name in gene_list:
        id = genes[gene_name]

        SERVER = "rest.ensembl.org"
        ENDPOINT = "/sequence/id/" + id
        PARAMS = "?content-type=application/json"
        URL = SERVER + ENDPOINT + PARAMS

        print()
        print(f"Server: {SERVER}")
        print(f"URL: {URL}")

        conn = http.client. HTTPConnection(SERVER)

        try:
            conn.request("GET", ENDPOINT + PARAMS)
        except ConnectionRefusedError:
            print("ERROR! Cannot connect to the Server")
            exit()

        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # -- Read the response's body
        response = json.loads(r1.read().decode("utf-8"))

        termcolor.cprint("Gene: ", 'green', end="", force_color=True)
        print(gene_name)

        termcolor.cprint("Description: ", 'green', end="", force_color=True)
        print(response["desc"])

        s = Seq(response["seq"])

        termcolor.cprint("Total length: ", 'green', end="", force_color=True)
        print(s.seq_len())

        bases_dict, percentage_of_each_base = s.percentage_of_bases()
        for e in bases_dict:
            termcolor.cprint(f"{e}: ", 'blue', end="", force_color=True)
            print(bases_dict[e], f"({percentage_of_each_base[e]})")

        termcolor.cprint("Most frequent Base: ", 'green', end="", force_color=True)
        print(s.most_frequent_base())
    correct = True