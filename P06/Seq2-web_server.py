import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from pprint import pprint


def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        GENES = ["U5", "ADA", "FRAT1", "RNU6", "FXN"]
        termcolor.cprint(self.requestline, 'green')
        if path == "/":
            contents = Path('html/index.html').read_text()
        elif path == "/ping":
            contents = Path("html/ping.html").read_text()
        elif path == "/get":
            pprint(arguments)
            gene_index = int(arguments["n"][0])
            gene_name = GENES[gene_index]
            sequence = Path("..", "sequences", gene_name + ".txt").read_text().splitlines()
            sequence = sequence[1:]
            msg = ""
            for line in sequence:
                msg += line
            contents = read_html_file("get.html").render(context={"todisplay": msg, "sequence": str(gene_index)})
        elif path == "/gene":
            for gene in GENES:
                if self.path.endswith(f"{gene}"):
                    sequence = Path("..", "sequences", gene + ".txt").read_text().splitlines()
                    sequence = sequence[1:]
                    msg = ""
                    for line in sequence:
                        msg += line
                    contents = read_html_file("gene.html").render(context={"todisplay": str(msg), "gene": str(gene)})
        elif path == "/operation":
            sequence_to_process = arguments['sequence'][0]
            op_to_be_done = arguments['operationType'][0]
            if op_to_be_done == "Info":
                total_len = len(sequence_to_process)
                a_a = f"A: {sequence_to_process.count('A')} ({((sequence_to_process.count('A') / total_len) * 100):.1f}%)"
                a_c = f"C: {sequence_to_process.count('C')} ({((sequence_to_process.count('C') / total_len) * 100):.1f}%)"
                a_g = f"G: {sequence_to_process.count('G')} ({((sequence_to_process.count('G') / total_len) * 100):.1f}%)"
                a_t = f"T: {sequence_to_process.count('T')} ({((sequence_to_process.count('T') / total_len) * 100):.1f}%)"
                info_msg = f"Total length: {len(sequence_to_process)}\n {a_a}\n {a_c}\n {a_g}\n {a_t}"
                contents = read_html_file("operation.html").render(context={"result": info_msg, "operation": "info", "sequence": sequence_to_process})
            elif op_to_be_done == "Comp":
                complement = ""
                for base in sequence_to_process:
                        if base == "A":
                            complement += "T"
                        elif base == "G":
                            complement += "C"
                        elif base == "C":
                            complement += "G"
                        elif base == "T":
                            complement += "A"
                contents = read_html_file("operation.html").render(context={"result": complement, "operation": "comp", "sequence": sequence_to_process})
            elif op_to_be_done == "Rev":
                seq_n = sequence_to_process[:len(sequence_to_process)]
                reverse = seq_n[::-1]
                contents = read_html_file("operation.html").render(context={"result": reverse, "operation": "rev", "sequence": sequence_to_process})
        else:
            contents = Path("html/error.html").read_text()
            self.send_response(404)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()