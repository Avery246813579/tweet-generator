"""
NAME: markov_N.py
"""


from dictogram import Dictogram
from pprint import pprint
from time import time as t
import random, sys


class MarkovNthOrder(object):

    def __init__(self, order=1):
        self.states = {}

        if order > 0:
            self.order = order
            print("\nOrder defined as {}.".format(self.order))
        else:
            raise Exception("\nImproper parameter given: please give integer.")
    
    def create_chain(self):
        n = self.order
        chain_struct = []

        for _ in range(n):
            chain_struct.append("")

        return tuple(chain_struct)

    def build_sequence(self, old, step):
        new = old[1:] + (step, )
        return new

    def build_states_from_sentence(self, input_sentence):
        prev = self.create_chain()
        tokens = input_sentence.split(" ")

        for token in tokens:
            if not prev in self.states:
                self.states[prev] = []
            curr = self.build_sequence(prev, token)
            self.states[prev].append(curr)
            prev = curr

        print("Input Sentence: {}\n\n".format(input_sentence))
        print("Order: {}\n\n".format(self.order))
        pprint("Total Tokens: {}".format(tokens))
        print("\n\n")
        pprint("Total States: {}".format(self.states))
        print("\n\n")

# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================

def create_model():
    test_sentence = "will you participate in the conference with new fellows on saturday evening after registration will you participate in the workshops on monday morning interested in sharing a room"
    
    markov = MarkovNthOrder(2)
    markov.build_states_from_sentence(test_sentence)

    return


def main():
    t0 = t()
    create_model()
    t1 = t()
    delta = 1000 * (t1 - t0)

    print("\nTotal runtime is {0:.3g} milliseconds.\n".format(delta))


if __name__ == "__main__":
    main()