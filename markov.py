import argparse
import markovify
import sys

parser = argparse.ArgumentParser()
parser.add_argument("person1")
parser.add_argument("person2")
args = parser.parse_args()


text1 = open("./data/{}_quotes.txt".format(
    "_".join(name for name in args.person1.split())), 'r').read()


text2 = open("./data/{}_quotes.txt".format(
    "_".join(name for name in args.person2.split())), 'r').read()

chain_1 = markovify.Text(text1)
chain_2 = markovify.Text(text2)

final_chain = markovify.combine([chain_1, chain_2])

print(final_chain.make_short_sentence(280))