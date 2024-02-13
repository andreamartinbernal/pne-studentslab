from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/Homo_sapiens_RNU6_1155P_sequence.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
print(file_contents)