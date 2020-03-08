import wikiquote
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("person")

args = parser.parse_args()



def download_quotes(person, file):
    with open(file, 'w') as f:
        quotes = wikiquote.quotes(person)
        for quote in quotes:
            f.write(quote + '\n')

if __name__ == '__main__':
    try:
        person = args.person
        file_name = "./data/{}_quotes.txt".format("_".join(name for name in person.split()))
        download_quotes(person, file_name)
    except Exception as e:
        print(e)
