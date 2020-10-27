import random
from numpy import zeros, sign
from math import exp, log
from collections import defaultdict

from torch.utils.data import Dataset

import argparse

class SportsDataset(Dataset):
    def __init__(self):
        # Implement this function
        None

def read_dataset(positive, negative, vocab, test_proportion=.1):
    """
    Create a pytorch SportsDataset for the train and test data.

    :param positive: Positive examples
    :param negative: Negative examples
    :param vocab: A list of vocabulary words
    :param test_proprotion: How much of the data should be reserved for test
    """

    # Look at the old dataset loader for hints

    return train, test

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--positive", help="Positive class",
                           type=str, default="positive", required=False)
    argparser.add_argument("--negative", help="Negative class",
                           type=str, default="negative", required=False)
    argparser.add_argument("--vocab", help="Vocabulary that can be features",
                           type=str, default="vocab", required=False)
    argparser.add_argument("--passes", help="Number of passes through train",
                           type=int, default=1, required=False)

    args = argparser.parse_args()
    train, test = read_dataset(args.positive, args.negative, args.vocab)

    print("Read in %i train and %i test" % (len(train), len(test)))

    # Initialize model

    # Iterations

    # Save the model
