from pathlib import Path
seq = ""
DNA_BASES = ["A", "T", "C", "G"]
COMPLEMENTARY_BASES = {"A": "T", "C": "G", "G": "C", "T": "A"}

# como en varios sitios se mira si un string es válido, lo he puesto como 
# una funcion
def is_valid_sequence (seq):
    count = 0
    for base in DNA_BASES:
        count += seq.count(base)
                
    if count != len(seq):
            return False

    return True

class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
        else:
            count = 0
            for base in DNA_BASES:
                count += strbases.count(base)

            if count == len(strbases):
                self.strbases = strbases
                print("New sequence created!")
            else:
                print("INVALID sequence created")
                self.strbases = "ERROR"



    def generate_seqs(pattern, number):
        seq_list = []
        seq = ""
        for i in range(number):
            seq += pattern
            seq_list.append(Seq(seq))
        return seq_list


    def __len__(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)


    def __str__(self):
        return self.strbases

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            number = 0
            for each_base in self.strbases:
                if each_base == base:
                    number += 1
            return number

    def seq_len(self):
        return len(self)

    def seq_count(self):
        bases_dict = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return bases_dict
        else:
            length = self.seq_len()
            if length != 0:
                for base in self.strbases:
                    bases_dict[base] += 1
            return bases_dict

    def seq_reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        else:
            complementary_seq = ""
            for base in self.strbases:
                complementary_seq += COMPLEMENTARY_BASES[base]
            return complementary_seq

    def read_fasta(self, filename):
        with open(filename, "r") as f:
            file_contents = Path(filename).read_text()
            list_contents = file_contents.split("\n")
            complete_seq = ""
            for i in range(1, len(list_contents)):
                complete_seq += (list_contents[i])
            f.close()
            self.strbases = complete_seq

    #NUEVOS MÉTODOS Y MÉTODOS MODIFICADOS
    # Returns False if sequence in the strbases member  is either "ERROR" or it is empty yet, returns 
    # True otherwise.
    # faltaba considerar el caso de que estuviera vacía: self.strbase == None
    def is_ok(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return False
        else:
            return True

    # Returns True if the Seq object does not hold a non empty sequence yet, False otherwise.
    def is_null(self):
        if self.strbases == "NULL":
            return True
        else:
            return False
    
    # Modify the existing read_fasta method in this way: if the provided filename argument does not correspond 
    # to an existing file, the content to put in the strbases member is "ERROR".
    # Modify again the read_fasta method: If filename is an exiting file but its content is not a proper DNA 
    # sequence, set strbases to "INVALID" (este y el anterior los podrían pedir juntos, pero incluso en ese caso 
    # "vamos por partes" y haríamos primero uno y después, cuando el primero funcionase, haríamos el otro ("divide 
    # y vencerás").  
    def read_fasta(self, filename):
        try: 
            with open(filename, "r") as f:
                file_contents = Path(filename).read_text()
                list_contents = file_contents.split("\n")
                complete_seq = ""
                for i in range(1, len(list_contents)):
                    complete_seq += (list_contents[i])
                f.close()
                self.strbases = complete_seq

                # Compruebo que el contenido es una secuencia de ADN (he pillado el trozo del código que hace lo mismo
                # en el constructor (el método __init__()), si no es correcta le pongo "INAVLID"
                count = 0
                for base in DNA_BASES:
                    count += self.strbases.count(base)

                if count != len(self.strbases):
                    self.strbases = "INVALID"

        except FileNotFoundError:
                # si llego hasta aquí es que el fichero no existia o no se pudo abrir:
                self.strbases = "ERROR"

    # The aim of this method is to concatenate the DNA sequence provided as argument to the end of the Seq strbases sequence, 
    # additionally a return code is returned to indicate if the operation was successfully done. If the argument is a valid DNA 
    # chain, make the concatenation and return 0 (that would be the "OK" code). If the argument is not a valid DNA string, leave 
    # untouched the Seq object and return a 1 (tha would be the "NO OK" code).
    def concat_DNA_string(self, str_seq):
        # he llamado str_seq al primer argumento para recordar que lo que me pasan es un string.
        # Para concatenar, veo si lo que me pasan está mal y tambien si tengo "ERROR" o "INVALID" (para ver si lo que me pasan
        # está mal me he hecho una función que mira si una secuencia es correcta o no)
        if self.strbases == "ERROR" or self.strbases == "INVALID" or not is_valid_sequence(str_seq):
            #no es una secuancia valida, asi que no hago la concatenación (no hago nada) y devuelvo 1, para indicar error.
            return 1
        # si he pasado del if anterior es que sí que voy a haer la concatenación, asi que acabaré devolviendo 0 (vamos, que 
        # las cosas fueron bien)

        # si lo que tengo está vacio directamente le pongo el string, si no, entonces concateno lo que me dan a lo que
        # ya tengo:
        if self.strbases == None:
            self.strbases = str_seq
        else:
            self.strbases += str_seq

        return 0
        
    # It is as the previous method but this time the argument is another Seq object instead of a string, apart of that, the behaviour 
    # to implement is the same. Note that to ckeck the validness of the provided seq argument, as it is a Seq object, you can use the 
    # already available methods in the Seq class.  Also, as a good programming practice, does not directly access to the strbases member 
    # of the seq object provided as argument, use an alternative procedure already available in the Seq class.
    def concat_DNA_Seq(self, seq):
        # Para concatenar, veo si lo que me pasan está mal y tambien si tengo "ERROR" o "INVALID", para verlo, como lo que me pasan 
        # es un objeto de la clase Seq puedo usar un método de la clase (el que me pidieron en el primer ejercicio del pdf):
        if not seq.is_ok():
            #no es una secuancia valida, asi que no hago la concatenación (no hago nada) y devuelvo 1, para indicar error.
            return 1
        # si he pasado del if anterior es que sí que voy a haer la concatenación, asi que acabaré devolviendo 0 (vamos, que 
        # las cosas fueron bien)

        # si lo que tengo está vacio directamente le pongo el string, si no, entonces concateno lo que me dan a lo que
        # ya tengo. Para acceder al strbases de la instancia que me pasan como argumento podría usar seq.strbases: eso es valido,
        # pero es mejor no acceder a sus datos directamenete (son embargo si dudas, hazlo directamente con seq.strbases, que no pasa 
        # nada). Para acceder sin usar seq.strbases usamos que __str__() justamente nos devuelve sus strbases:
        if self.strbases == None:
            self.strbases = str(seq)
        else:
            self.strbases += str(seq)

        return 0

    # Returns a tupla with two Seq objects. The first one holds the fragment of the original Seq object with the bases from the 0 
    # position to the pos position, and the second one holds the remainder bases. If pos goes beyond the end of the DNA chain held 
    # into the strbases member, the first Seq object in the tupla must hold the whole chain, and the second one must be a null Seq 
    # object (that is, a Seq object created without a DNA chain).
    def split_by_pos(self, pos):
        if pos >= len(self.strbases)-1:
            return(Seq(self.strbases), Seq())
        else:
            # primer fragmento debe ser de 0 hasta pos, segundo fragmento debe ser desde pos+1 hasta el final:
            return(Seq(self.strbases[0:pos+1]), Seq(self.strbases[pos+1:]))

    # This method is similar to the split_by_pos method, but this time a valid DNA string (the "fragment" argument) sets the point 
    # to use to split in two parts the original Seq instance. As the mentioned method, it also returns a tupla with two Seq objects. 
    # The first one holds the fragment of the original Seq object with the bases from the 0 position to the position in which 
    # "fragment" (the fragment provided as argument) starts, and the second Seq instance in the tupla  holds the bases of the original 
    # Seq object that go from the position after the end of "fragment" up to the end of the original Seq object. Please note that 
    # "fragment" may appear in the Seq instance more than once, in that case just the first occurrence should be taken into account. 
    # If "fragment" is not present in the Seq original object, the first component of the tupla must be a Seq object that holds the 
    # whole DNA chain that was in the original Seq object and the second tupla component must be a null Seq object. NOTE: you can 
    # assume that the provided fragment is valid, so it is not needed to perform any check about wether it is a valid DNA chain or not. 
    def split_by_fragment(self, fragment):
        if fragment not in self.strbases:
            return(Seq(self.strbases), Seq())
        else:
            # aun cuando fragment pueden ser varios caracteres, se puede usar de "separator", el segundo argumento lo que dice es que
            # aunque fragmento aparezca más veces solo se haga una separación, que es lo que nos pide la especificación.
            fragments = self.strbases.split(fragment,1)
            return(Seq(fragments[0]), Seq(fragments[1]))
        
    # It returns a list with the first three fragments (whose lenght is fragment_lenght) of the Seq object. You can assume that the DNA 
    # string held in the Seq object is long enough to contain three fragments with the specified lenght (to have a long DNA chain for the 
    # tests, create the Seq object from a file with the read_fasta method). NOTA: Básate en el ejemplo que te pasé (como una captura de 
    # pantalla) que usaba range para trocear una cadena de ADN.
    def get_three_fragments (self, fragment_length):
        # si los indices de la cadena son 0123456789
        # y fragment_lenght es 2, los índices de los fragmentos serían: 01 23 45 6789
        # me fijo en qué patrones siguen los inicios y finales de los fragmentos y los codificaré
        # siempre empezamos por el indice 0. 
        # en cada fragmento, el punto de inicio es el del anterior mas la longitud de fragmento (2 en el ejemplo)
        # tomamos desde el punto de inicio del fragmento un fragmento de longitud fragment_length
        # tenemos que hacer 3 iteraciones, un range de 0 a 3
        fragment_list = []
        starting_point_for_fragment = 0
        for i in range(0,3):
            fragment_list.append(self.strbases[starting_point_for_fragment:starting_point_for_fragment+fragment_length])
            starting_point_for_fragment += fragment_length
        
        return fragment_list
            

