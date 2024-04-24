import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
first_response = conn.getresponse()

# -- Print the status line
print(f"Response received!: {first_response.status} {first_response.reason}\n")

# -- Read the response's body
response = json.loads(first_response.read().decode("utf-8"))

if response["ping"] == 1:
    print("PING OK! The database is running!")