import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
persons = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
print("total people in the data base:", len(persons["people"]))

for person in persons["people"]:
    print()
    termcolor.cprint("Name: ", 'green', end="", force_color=True)
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="", force_color=True)
    print(person['age'])

# Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

# Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end="", force_color=True)
    print(len(phoneNumbers))

# Print all the numbers
    for i, dictofnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue', force_color=True)

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='', force_color=True)
        print(dictofnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='', force_color=True)
        print(dictofnum['number'])