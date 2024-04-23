import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-3.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)
for person in people:
    print()
    n = 0
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname', str(n+1)])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age', n+1])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber', n+1]

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
