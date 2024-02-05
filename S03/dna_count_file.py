def read_csv_file(filename):
    list_of_dictionaries = []
    try:

        with open(filename, "r", encoding="latin-1") as f:
            header = next(f).replace("\n", "").split(",")
            for line in f:
                components = line.replace("\n", "").split(",")
                d = dict(zip(header, components))
                list_of_dictionaries.append(d)
        f.close()

    except FileNotFoundError:
        print("ERROR: file", filename, "not found. Exiting.")
        exit()
    except PermissionError:
        print("ERROR: No permissions for file", filename, "Exiting.")
        exit()

    return list_of_dictionaries