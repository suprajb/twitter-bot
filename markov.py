import argparse
import markovify
import language_check

from helpers import *

tool = language_check.LanguageTool('en-US')

def generate_tweet(persons, chain_state_size=2):
    texts = [open(DATADIR + file_name(person) + DATASUFFIX, 'r').read()
             for person in persons]
    chains = [markovify.Text(text) for text in texts]
    final_chain = markovify.combine(chains)

    tweet = final_chain.make_short_sentence(
        280, state_size=chain_state_size, max_overlap_ratio=0.5)
    matches = tool.check(tweet)
    tweet = language_check.correct(tweet, matches)
    return tweet