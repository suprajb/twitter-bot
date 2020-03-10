DATADIR = "./data/"
DATASUFFIX = "_quotes.txt"

CHAINDIR = "./chains/"

def file_name(person):
    return "_".join(name for name in sorted(person.lower().split()))
