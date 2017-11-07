# dictionary_example.py (In-class example)

import random, sys, time

t_init = time.time()

# TODO separation of concerns
def give_dictionary_values():
    # Catch case
    # TODO Need to make faster (and functional) (STRETCH challenge)
    input_args = sys.argv[1]
    if (input_args == None):
        return "Please enter a valid input"
    
    f = open("/usr/share/dict/words")
    file_lines = f.readlines()

    # Iterate randomly through dictionary until counter is equal to user's input value
    # TODO Try with a for loop
    counter = 0
    word_list = []
    while (counter < int(input_args)):
        word = random.choice(file_lines).strip()
        word_list.append(word)
        counter += 1

    return " ".join(word_list)

# TODO Refactor code so file only opens once, then preprocesses
if __name__ == "__main__":
    print("\n\nRandom Dictionary Values: \n\n " + give_dictionary_values() + "\n")
    print("\n\nTime elapsed: {} milliseconds".format(1000 * (time.time() - t_init)))  # Prints runtime