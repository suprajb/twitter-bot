import argparse
import markovify
import sys

parser = argparse.ArgumentParser()
parser.add_argument("persons", nargs='+')

args = parser.parse_args()


texts = [ open("./data/{}_quotes.txt".format(
    "_".join(name for name in person.split())), 'r').read() for person in args.persons]


chains = [markovify.Text(text) for text in texts]

final_chain = markovify.combine(chains)

print(final_chain.make_short_sentence(280, max_overlap_ratio=0.5))