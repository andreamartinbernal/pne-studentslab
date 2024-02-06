from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "sequences/Amphiprion_ocellaris_U5_sequence.fa"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

# -- Print the contents on the console
#print(file_contents)

list_contents = file_contents.split("\n")
#print("The body of the file is: ", list_contents[1:])

for i in range(1, len(list_contents)):
    print(list_contents[i])
