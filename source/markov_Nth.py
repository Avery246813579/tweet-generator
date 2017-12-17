"""
TITLE:          markov_Nth.py

DESCRIPTION:    This is a functioning class instance of an adjustable Nth-order
                Markov Chain that accepts a large corpus of words and outputs a 
                histogram-sampled sentence.

TODO:           -> Identify performance analyses (memory) on major class methods.
                -> 

SOURCE:         CS2-Tweet-Generator course repository at Make School Product College

AUTHOR:         Aakash Sudhakar
"""


# ================================================================================
# ============================== IMPORT STATEMENTS ===============================
# ================================================================================


from pprint import pprint                               # Pretty print library
from time import time as t                              # Time logger library
from random import randint as ri                        # Random number library
import sys                                              # System operations library


# ================================================================================
# =================== CLASS DEFINITION: Nth-ORDER MARKOV CHAIN ===================
# ================================================================================


class Markov_Nth_Order(object):

    # =========================== CLASS INITIALIZER(S) ===========================
    def __init__(self, order=1):
        self.states = {}
        # self.histogram = []

        if order > 0:
            self.order = order
        else:
            raise Exception("\nImproper parameter given: please give integer.")
    
    # ================= HELPER METHOD TO CREATE N-SIZED WINDOW ===================
    """
    NOTE: (TIME) Best/Worst Case -> O(n) -> Append N new entries to window
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def initialize_window(self):
        n = self.order
        window = []

        # Create window tuple of size n (inputted order)
        for _ in range(n):
            window.append("")

        return tuple(window)

    # ==================== HELPER METHOD TO BUILD EACH WINDOW ====================
    """
    NOTE: (TIME) Best/Worst Case -> O(1) -> Sum together inputs
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def add_to_window(self, old, step):
        new = old[1:] + (step, )
        return new

    # ================= METHOD TO CREATE DICTOGRAM FROM SENTENCE =================
    """
    NOTE: (TIME) Best/Worst Case -> O(n) -> Create dictogram by iterating through all tokens once
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def build_states_from_sentence(self, tokens):
        prev = self.initialize_window()

        # Create markov model of current and next chained-word states
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
        return

    # ============ METHOD TO SAMPLE DICTOGRAM AND CREATE NEW SENTENCE ============
    """
    NOTE: (TIME) Best Case -> O(1) -> Random samples select few words towards start of markov chain
    NOTE: (TIME) Worst Case -> O(n^2) -> Random samples select many words scattered throughout markov chain
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def construct_sample_sentence(self):
        temp = self.initialize_window()
        current_position = self.select_current_position(temp)
        start, word_break, first = "", " ", True

        # print("temp: {}".format(temp))
        # print("start: {}".format(start))
        # print("word_break: {}".format(word_break))
        # print("histogram: {}".format(self.histogram))

        # Use randomizing library to chain together sentence based on sampling frequencies
        while (current_position in self.states) and (current_position != temp) and (current_position != None):
            if not first:
                start += word_break

            start += current_position[len(current_position) - 1]
            current_position = self.select_current_position(current_position)
            first = False
        
        constructed_walk = start + word_break + current_position[len(current_position) - 1]
        
        return constructed_walk

    # ======== METHOD TO RANDOMLY SELECT CURRENT WORD POSITION IN CORPUS =========
    """
    NOTE: (TIME) Best Case -> O(?) -> ???
    NOTE: (TIME) Worst Case -> O(?) -> ???
    NOTE: (MEMORY) Best Case -> O(?) -> ???
    NOTE: (MEMORY) Worst Case -> O(?) -> ???
    """
    def select_current_position(self, pos):
        current_position = self.states[pos][ri(0, len(self.states[pos]) - 1)]
        return current_position


# ================================================================================
# ============================== MAIN RUN FUNCTIONS ==============================
# ================================================================================


# ================== FUNCTION TO CREATE AND RUN CLASS INSTANCE ===================
def create_model():
    # Create corpus from TCoMC book (over 400,000 words)
    with open("tcomc_unabridged.txt") as f:
        corpus = f.read().split()
    markov = Markov_Nth_Order()

    # Create random walk, then reformat and clean to produce final outputted sentence
    markov.build_states_from_sentence(corpus)
    random_walk = markov.construct_sample_sentence()
    output = random_walk[0].upper() + random_walk[1:]

    print("ORDER OF MARKOV:\nn = {}\n".format(markov.order))
    print("OUTPUT SENTENCE: {}...".format(output[:250]))
    return

# ================================== MAIN RUN ====================================
def main():
    # Benchmark class instance for time complexity
    t0 = t()
    create_model()
    t1 = t()
    delta = t1 - t0

    print("\n\nTotal runtime is {0:.3g} seconds.\n".format(delta))
    return


# =========================== PYTHON RUN BOILERPLATE =============================
if __name__ == "__main__":
    main()
