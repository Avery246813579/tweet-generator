"""
TITLE: markov_Nth.py
DESCRIPTION:    This is a functioning class instance of an adjustable Nth-order
                Markov Chain that accepts a large corpus of words and outputs a 
                histogram-sampled sentence. 
SOURCE: CS2-Tweet-Generator course repository at Make School Product College
AUTHOR: Aakash Sudhakar
"""


# ================================================================================
# ============================== IMPORT STATEMENTS ===============================
# ================================================================================


from pprint import pprint                               # Pretty print library
from time import time as t                              # Time logger library
from random import randint as ri                        # Random number library
import sys                                              # System operations library


# ================================================================================
# =================== CLASS DEFINITION: Nth ORDER MARKOV CHAIN ===================
# ================================================================================


class MarkovNthOrder(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, order=1):
        self.states = {}
        # self.histogram = []

        if order > 0:
            self.order = order
        else:
            raise Exception("\nImproper parameter given: please give integer.")
    
    # ================= HELPER METHOD TO CREATE N-SIZED WINDOW ===================
    def initialize_window(self):
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
    def build_states_from_sentence(self, tokens):
        prev = self.initialize_window()

        for token in tokens:
            if not prev in self.states:
                self.states[prev] = []

            curr = self.add_to_window(prev, token)
            self.states[prev].append(curr)

            prev = curr

        input_sentence = " ".join(tokens)

        print("\nINPUT SENTENCE: {}...\n".format(input_sentence[:250]))
        print("WORD COUNT OF CORPUS: >400,000\n")
        # print("ORDER: {}\n".format(self.order))
        # print("TOTAL TOKENS:")
        # pprint(tokens)
        # print("\nTOTAL STATES:")
        # pprint(self.states)

    # ============ METHOD TO SAMPLE DICTOGRAM AND CREATE NEW SENTENCE ============
    def construct_sample_sentence(self):
        temp = self.initialize_window()
        current_position = self.states[temp][ri(0, len(self.states[temp]) - 1)]
        start, breaker, first = "", " ", True

        # print("temp: {}".format(temp))
        # print("start: {}".format(start))
        # print("breaker: {}".format(breaker))
        # print("histogram: {}".format(self.histogram))

        while (current_position in self.states) and (current_position != temp) and (current_position != None):
            if not first:
                start += breaker

            start += current_position[len(current_position) - 1]
            current_position = self.states[current_position][ri(0, len(self.states[current_position]) - 1)]
            first = False
        
        return start + breaker + current_position[len(current_position) - 1]


# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================


# ================== FUNCTION TO CREATE AND RUN CLASS INSTANCE ===================
def create_model():
    # corpus = "will you participate in the conference with new fellows on saturday evening after registration will you participate in the workshops on monday morning interested in sharing a room"
    with open("tcomc_unabridged.txt") as f:
        corpus = f.read().split()
    markov = MarkovNthOrder(3)

    markov.build_states_from_sentence(corpus)
    random_walk = markov.construct_sample_sentence()
    output = random_walk[0].upper() + random_walk[1:]

    print("OUTPUT SENTENCE: {}...".format(output[:250]))
    return

# ================================== MAIN RUN ====================================
def main():
    t0 = t()
    create_model()
    t1 = t()
    delta = t1 - t0

    print("\n\nTotal runtime is {0:.3g} seconds.\n".format(delta))


# =========================== PYTHON RUN BOILERPLATE =============================
if __name__ == "__main__":
    main()
