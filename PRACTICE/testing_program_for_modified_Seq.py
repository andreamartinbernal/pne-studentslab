from pathlib import Path
from PRACTISE_CLASS_SEQ_MODIFIED import *


# ----------------------------------------------------------------------------------
print("\n* Testing is_ok:  ------------------------------------------------")

seq_null = Seq()
seq_error = Seq("AXXXXA")
seq_ok = Seq("AACTGGA")

print("*** Testing with:", seq_null, "should be NOT OK!:")
if seq_null.is_ok():
     print("OK!")
else:
     print("NOT OK!")
print("*** Testing with:", seq_error, "should be NOT OK!:")
if seq_error.is_ok():
     print("OK!")
else:
     print("NOT OK!")
print("*** Probando con:", seq_ok, "should be OK!!:")
if seq_ok.is_ok():
     print("OK!")
else:
     print("NOT OK!")
  
# ----------------------------------------------------------------------------------
print("\n* Testing is_null:  ------------------------------------------------")
print("*** Testing with:", seq_null, "should be NULL!:")
if seq_null.is_null():
     print("NULL!")
else:
     print("NOT NULL!")
print("*** Testing with:", seq_error, "should be NOT NULL!!:")
if seq_error.is_null():
     print("NULL!")
else:
     print("NOT NULL!")
print("*** Testing with:", seq_ok, "should be NOT NULL!!:")
if seq_ok.is_null():
     print("NULL!")
else:
     print("NOT NULL!")

# ----------------------------------------------------------------------------------
print("\n* Testing read_fasta:  ------------------------------------------------")

ADA_filename = "ADA.txt"
INVALID_DNA_filename = "INVALID_DNA.txt" # tiene contenido que no es ADN
UNEXISTENT_filenam = "NOEXISTE.txt" # no existe
FILES_FOLDER = Path.cwd() # los ficheros estan en el mismo dir que el programa


seq_ada = Seq()
seq_ada.read_fasta (FILES_FOLDER / ADA_filename)
print("*** ADA: debe ser una cadena:", seq_ada)
seq_invalid_dna = Seq()
seq_invalid_dna.read_fasta (FILES_FOLDER / INVALID_DNA_filename)
print("*** INVALID_DNA: debe ser invalid:", seq_invalid_dna)
seq_unexistent = Seq()
seq_unexistent.read_fasta (FILES_FOLDER / UNEXISTENT_filenam)
print("*** UNEXISTENT: debe ser ERROR:", seq_unexistent)

# ----------------------------------------------------------------------------------
print("\n* Testing concat_DNA_string:  ------------------------------------------------")
not_valid_str_to_concat = "AAXXXX"
valid_str_to_concat = "GGGGGTTTTTT"
seq_for_concat_str_test = Seq("AAAAAACCCC")

print("*** Concatenating with BAD string to", seq_for_concat_str_test, "no change should be done.")
concat_return_code = seq_for_concat_str_test.concat_DNA_string(not_valid_str_to_concat)
if concat_return_code == 0:
     print("Concatenation done!")
else:
      print("Concatenation NOT done!")
print("Seq object after concat operation:", seq_for_concat_str_test, "Should be the same as before!")

print("*** Concatenating with VALID string to", seq_for_concat_str_test, "concatenation should be done .")
concat_return_code = seq_for_concat_str_test.concat_DNA_string(valid_str_to_concat)
if concat_return_code == 0:
     print("Concatenation done!")
else:
      print("Concatenation NOT done!")
print("Seq object after concat operation:", seq_for_concat_str_test, "Should be longer than before!")

# ----------------------------------------------------------------------------------
print("\n* Testing concat_DNA_Seq:  ------------------------------------------------")
not_valid_seq_to_concat = Seq("AAXXXX")
valid_seq_to_concat = Seq("GGGGGTTTTTT")
seq_for_concat_seq_test = Seq("AAAAAACCCC")

print("*** Concatenating with BAD Seq to", seq_for_concat_seq_test, "no change should be done.")
concat_return_code = seq_for_concat_seq_test.concat_DNA_Seq(not_valid_seq_to_concat)
if concat_return_code == 0:
     print("Concatenation done!")
else:
      print("Concatenation NOT done!")
print("Seq object after concat operation:", seq_for_concat_seq_test, "Should be the same as before!")

print("*** Concatenating with VALID string to", seq_for_concat_seq_test, "concatenation should be done .")
concat_return_code = seq_for_concat_seq_test.concat_DNA_Seq(valid_seq_to_concat)
if concat_return_code == 0:
     print("Concatenation done!")
else:
      print("Concatenation NOT done!")
print("Seq object after concat operation:", seq_for_concat_seq_test, "Should be longer than before!")

# ----------------------------------------------------------------------------------
print("\n* Testing split_by_pos: ------------------------------------------------")
seq_for_split_by_pos_test = Seq("AACCGGTTAACCGGTT")
print("*** Testing with pos beyond the end of the sequence...")
fragment1, fragment2 = seq_for_split_by_pos_test.split_by_pos(100)
print("Seq object to be split:", seq_for_split_by_pos_test)
print("Fragment 1 must be the whole object:", fragment1, "Fragment 2 must be a null Seq:", fragment2)

print("*** Testing with pos falling inside the sequence pos=5...")
fragment1, fragment2 = seq_for_split_by_pos_test.split_by_pos(5)
print("Seq object to be split:", seq_for_split_by_pos_test)
print("Fragment 1 should be AACCGG:", fragment1, "Fragment 2 should be TTAACCGGTT:", fragment2)

# ----------------------------------------------------------------------------------
print("\n* Testing split_by_fragment: ------------------------------------------------")
seq_for_split_by_fragment_test = Seq("AACCGGTTAACCGGTT")
print("*** Testing with a fragment that is not present in the sequence, fragment = GA...")
fragment1, fragment2 = seq_for_split_by_fragment_test.split_by_fragment("GA")
print("Seq object to be split:", seq_for_split_by_fragment_test)
print("Fragment 1 must be the whole object:", fragment1, "Fragment 2 must be a null Seq:", fragment2)

print("*** Testing with a fragment that is present in the sequence, fragment = GG ...")
fragment1, fragment2 = seq_for_split_by_fragment_test.split_by_fragment("GG")
print("Seq object to be split:", seq_for_split_by_fragment_test)
print("Fragment 1 should be AACC:", fragment1, "Fragment 2 should be TTAACCGGTT:", fragment2)

# ----------------------------------------------------------------------------------
print("\n* Testing get_three_fragments: ------------------------------------------------")

# testing with different fragment lenghts, for each test I use a sequence that let me
# easily see if the method works or not
seq_for_get_three_fragments_test1 = Seq("AACCGGTTAACCGGTT")
print("*** Testing with", seq_for_get_three_fragments_test1, "and fragment length 2")
fragment_list = seq_for_get_three_fragments_test1.get_three_fragments (2)
print("Fragments, should be AA CC and GG, are:", fragment_list)

seq_for_get_three_fragments_test2 = Seq("AAACCCGGGTTAACCGGTT")
print("*** Testing with", seq_for_get_three_fragments_test2, "and fragment length 3")
fragment_list = seq_for_get_three_fragments_test2.get_three_fragments (3)
print("Fragments, should be AAA CCC and GGG, are:", fragment_list)

seq_for_get_three_fragments_test3 = Seq("AAAACCCCGGGGTTAACCGGTT")
print("*** Testing with", seq_for_get_three_fragments_test3, "and fragment length 4")
fragment_list = seq_for_get_three_fragments_test3.get_three_fragments (4)
print("Fragments, should be AAAA CCCC and GGGG, are:", fragment_list)
