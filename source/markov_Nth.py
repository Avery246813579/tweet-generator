"""
TITLE: markov_Nth.py
DESCRIPTION:    This is a functioning class instance of a simple Python hash table
                with Linked List implementation. 
SOURCE: CS2-Tweet-Generator course repository at Make School Product College
AUTHOR: Aakash Sudhakar
"""


# ================================================================================
# ============================== IMPORT STATEMENTS ===============================
# ================================================================================

from pprint import pprint                               # Pretty print library
from time import time as t                              # Time logger library
import random, sys                                      # Random, system libraries


# ================================================================================
# =================== CLASS DEFINITION: Nth ORDER MARKOV CHAIN ===================
# ================================================================================

class MarkovNthOrder(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, order=1):
        self.states = {}

        if order > 0:
            self.order = order
        else:
            raise Exception("\nImproper parameter given: please give integer.")
    
    # ================= HELPER METHOD TO CREATE N-SIZED WINDOW ===================
    def create_window(self):
        n = self.order
        window = []

        for _ in range(n):
            window.append("")

        return tuple(window)

    # ==================== HELPER METHOD TO BUILD EACH WINDOW ====================
    def add_to_window(self, old, step):
        new = old[1:] + (step, )
        return new

    # ================= METHOD TO CREATE DICTOGRAM FROM SENTENCE =================
    def build_states_from_sentence(self, input_sentence):
        prev = self.create_chain()
        tokens = input_sentence.split(" ")

        for token in tokens:
            if not prev in self.states:
                self.states[prev] = []
            curr = self.add_to_window(prev, token)
            self.states[prev].append(curr)
            prev = curr

        print("\INPUT SENTENCE: {}\n".format(input_sentence))
        print("ORDER: {}\n".format(self.order))
        print("TOTAL TOKENS:")
        pprint(tokens)
        print("\nTOTAL STATES:")
        pprint(self.states)

# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================

# ================== FUNCTION TO CREATE AND RUN CLASS INSTANCE ===================
def create_model():
    test_sentence = "will you participate in the conference with new fellows on saturday evening after registration will you participate in the workshops on monday morning interested in sharing a room"
    
    markov = MarkovNthOrder(2)
    markov.build_states_from_sentence(test_sentence)
    return

# ================================== MAIN RUN ====================================
def main():
    t0 = t()
    create_model()
    t1 = t()
    delta = 1000 * (t1 - t0)

    print("\nTotal runtime is {0:.3g} milliseconds.\n".format(delta))


# =========================== PYTHON RUN BOILERPLATE =============================
if __name__ == "__main__":
    main()