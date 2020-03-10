import os
import sys
import markov
import itertools
import random
import tweepy

auth = tweepy.OAuthHandler(
    os.environ['API_KEY'], os.environ['API_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)


if __name__ == "__main__":
    person_list = ["joseph stalin", "john lennon", "steve jobs"]
    state_sizes = [2,3]

    combinations = [list(comb) for comb in itertools.combinations(person_list, 2)]
    combinations.append(person_list)

    person_choice = random.choice(combinations)
    state_choice = random.choice(state_sizes)

    tweet = markov.generate_tweet(person_choice, state_choice)
    api.update_status(tweet)
