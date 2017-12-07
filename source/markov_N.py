from dictogram import Dictogram
from pprint import pprint
from time import time as t
import random, sys


class MarkovNthOrder(object):

    def __init__(self, order=1):
        self.states = {}

        if (len(sys.argv) > 1):
            if order > 0:
                self.order = sys.argv[1]
                print("\nOrder defined as {}.".format(self.order))
            else:
                raise Exception("\nImproper parameter given: please give integer.")
        else:
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



# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================

def create_model():
    separator = " "

    test_sentence = "will you participate in the conference with new fellows on saturday evening after registration will you participate in the workshops on monday morning interested in sharing a room"
    markov = MarkovNthOrder()
    return


def main():
    t0 = t()
    create_model()
    t1 = t()
    delta = 1000 * (t1 - t0)

    print("\nTotal runtime is {0:.3g} milliseconds.\n".format(delta))


if __name__ == "__main__":
    main()