# rearrange_example.py (In-class example)


import random, re, sys


'''
Function to rearrange user-inputted string
'''
def rearrange_string():
    # Take user arguments and remove junk
    old_string = str(sys.argv[1:])

    # Use regular expressions and .split() method to break string into array of strings (NEED TO POLISH)
    string_vals = re.sub("[^a-z]", " ", old_string).split()

    # Use .shuffle() method to shuffle array values, then return joined array of strings
    random.shuffle(string_vals)
    return(" ".join(string_vals))


if __name__ == "__main__":
    print("\n\nSTRING REARRANGEMENT:\n\n" + rearrange_string() + "\n\n")