import wikiquote
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("person")
args = parser.parse_args()

def download_quotes(person, file):
    with open(file, 'a') as f:
        quotes = wikiquote.quotes(person, max_quotes=200)
        for quote in quotes:
            if quote.find(":")!=-1:
                f.write(quote + '\n')
            else:
                quote = quote.split(":")
                names = [name for name in person.split()]
                i = 0
                for i in range(len(quote)):
                    if quote[i] in names:
                        f.write(quote[i+1] + '\n')

if __name__ == '__main__':
    try:
        person = args.person
        file_name = "./data/{}_quotes.txt".format("_".join(name for name in person.split()))
        download_quotes(person, file_name)
    except Exception as e:
        print(e)
