import pprint
import http.client
import json
import termcolor
from seq1 import *

ENSEMBL_SERVER = "rest.ensembl.org"
PARAMS = "?content-type=application/json"
PARAMS_GENE_LIST = "?feature=gene;content-type=application/json"


ENDPOINT_INFO_SPECIES = "/info/species"
ENDPOINT_GET_GEN_INFO = "/sequence/id/"
# to get chromosome length and karyotype
ENDPOINT_INFO_ASSEMBLY = "/info/assembly/"
# for human genes:
ENDPOINT_GET_GEN_STABLE_ID = "/lookup/symbol/homo_sapiens/"
ENDPOINT_GENE_LIST = "overlap/region/human/"


class GB_ensembl_handler:
    def __init__(self):
        print("GB_ensemble_client initialized. Server:", ENSEMBL_SERVER)

    def send_request(self, service_endpoint, gene_list=False):
        if gene_list:
            full_endpoint = service_endpoint + PARAMS_GENE_LIST
        else:
            full_endpoint = service_endpoint + PARAMS

        conn = http.client.HTTPConnection(ENSEMBL_SERVER)

        # exceptions arisen from request are catched at the calling function:
        print("Endpoint:", full_endpoint)
        conn.request("GET", full_endpoint)

        # -- Read the response message from the server
        r1 = conn.getresponse()

        # -- Print the status line
        print(f"Response received!: {r1.status} {r1.reason}\n")

        # to manage errors returned by ensembl
        ensembl_rest_error = False
        if r1.status == 400:
            ensembl_rest_error = True

        # -- Read the response's body
        response = json.loads(r1.read().decode("utf-8"))

        termcolor.cprint("Received INFO", 'yellow', end="", force_color=True)
        print()
        return ensembl_rest_error, response

    def get_list_of_species(self, limit):
        # no error is expected in this requets as its format is fix
        ensembl_rest_error, ensembl_species = self.send_request(ENDPOINT_INFO_SPECIES)

        ensembl_list_of_species = ensembl_species["species"]

        full_list_of_species = []

        for specie_item in ensembl_list_of_species:
            if specie_item["division"] == "EnsemblVertebrates":
                full_list_of_species.append(specie_item["display_name"])

        # this is the total number of species in ensembl:
        nb_of_species = len(full_list_of_species)
        # gets the ordered list of all species
        full_list_of_species.sort()

        #takes just limit items from the ordered list (or all of them if limit is 0)
        list_of_species = []
        if limit != 0:
            for i in range(0, limit):
                list_of_species.append(full_list_of_species[i])
        else:
            list_of_species = full_list_of_species

        return nb_of_species, list_of_species

    def get_gene_stable_id(self, friendly_gene_name):
        completed_endpoint = ENDPOINT_GET_GEN_STABLE_ID + friendly_gene_name
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint)

        if not ensembl_rest_error:
            stable_id = rest_response["id"]
        else:
            stable_id = None

        return ensembl_rest_error, stable_id

    def get_gene_seq_by_stable_id(self, stable_id):
        completed_endpoint = ENDPOINT_GET_GEN_INFO + stable_id
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint)

        if not ensembl_rest_error:
            seq = rest_response["seq"]
        else:
            seq = None

        return ensembl_rest_error, seq

    def get_gene_seq_by_friendly_name(self, friendly_gene_name):
        ensembl_rest_error, stable_id = self.get_gene_stable_id(friendly_gene_name)

        if ensembl_rest_error:
            return ensembl_rest_error, None

        ensembl_rest_error, seq = self.get_gene_seq_by_stable_id(stable_id)

        if ensembl_rest_error:
            return ensembl_rest_error, None

        return ensembl_rest_error, seq

    def get_chromosome_length(self, friendly_species_name, chromo):
        completed_endpoint = ENDPOINT_INFO_ASSEMBLY + friendly_species_name
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint)

        if ensembl_rest_error:
            return ensembl_rest_error, None

        list = rest_response["top_level_region"]
        chromosome_length = -1
        for item in list:
            if item["name"] == chromo and item["coord_system"] == "chromosome":
                chromosome_length = item["length"]
        if chromosome_length == -1:
            ensembl_rest_error = True

        return ensembl_rest_error, chromosome_length

    def get_karyotype(self, friendly_species_name):
        completed_endpoint = ENDPOINT_INFO_ASSEMBLY + friendly_species_name
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint)

        if ensembl_rest_error:
            return ensembl_rest_error, None

        karyotype = rest_response["karyotype"]

        return ensembl_rest_error, karyotype

    def get_gene_info(self, friendly_gene_name):
        completed_endpoint = ENDPOINT_GET_GEN_STABLE_ID + friendly_gene_name
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint)

        if not ensembl_rest_error:
            stable_id = rest_response["id"]
            start = rest_response["start"]
            end = rest_response["end"]
            chromo = rest_response["seq_region_name"]
            length = str(int(end) - int(start))
        else:
            stable_id = None
            start = None
            end = None
            chromo = None
            length = None

        return ensembl_rest_error, stable_id, start, end, length, chromo

    def get_gene_list(self, chromo, start_int, end_int):
        completed_endpoint = ENDPOINT_GENE_LIST + chromo + ":" + str(start_int) + "-" + str(end_int)
        print(f"endpoint para el gene list {completed_endpoint}")
        ensembl_rest_error, rest_response = self.send_request(completed_endpoint, True)
        gene_list = []
        if not ensembl_rest_error:
            for item_list in rest_response:
                if "external_name" in item_list:
                    gene_list.append(item_list["external_name"])
                else:
                    gene_list.append(item_list["gene_id"])
        else:
            gene_list = None

        return ensembl_rest_error, gene_list
