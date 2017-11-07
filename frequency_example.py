# frequency_example.py (In-class example)

from functools import reduce
import re, sys, json

# TODO refactor to put all user input/output shit into one function

def program_start():
    # test_string = "this is a test string and I really like it but I really hope that it is a good test string"
    f = open("./the_count_of_monte_cristo.txt", "r").read()
    f = f.replace("\\", "")
    re.sub(r"[^\w]", "", f)

    print("\n\nWelcome to the Plain-Text Word Frequency Analyzer.")

    analyzer_choice(f)
    

def string_cleaner(f):
    pass


def analyzer_choice(f):
    # TODO implement while loop rather than nested ifs (until user inputs correct number, run while loop)
    # Checks user input to print out frequency distribution as histogram

    print("\nChoose a numeric option from below:\n")
    type_choice = input("\nDictionary [1]\nList of Lists [2]\nList of Tuples [3]\n\n>> ")

    if type_choice and type_choice.isnumeric():
        type_choice = int(type_choice)

        if type_choice == 1:
            histogram_as_dictionary(f)
        elif type_choice == 2:
            histogram_as_list_of_lists(f)
        elif type_choice == 3:
            print("\n\nERROR: 'List of Tuples' analyzer is in development. Please select another option.\n")
            analyzer_choice(f)
        else:
            print("\nUser input is invalid. Choose a valid option from the given list.\n")
            analyzer_choice(f)
    else:
        print("\nUser input is invalid. Choose a valid option from the given list.\n")
        analyzer_choice(f)
    

def histogram_as_dictionary(data):
    result = reduce( lambda index, count: index.update([(count, index.get(count, 0) + 1)]) or index, data.split(" "), {})

    with open("logs_dict.txt", "w") as file:
        file.write("WORD FREQUENCY DATA (Type: DICTIONARY)\n\n\n\n\n\n\n\n\n\n" + json.dumps(result) + "\n\n\n\n\n\n\n\n\n\n")
        print("\n\nWord frequency data (type: Dictionary) has been logged successfully.\n")

    continue_program()


def histogram_as_list_of_lists(data):
    result = []  # histogram
    # test = "this is a test string wow look at this string it is such a great test"
    doesExist = True

    # Logic to convert split strings into a word frequency list of lists
    for item in data.lower().split():
        for word in result:
            if word[0] == item:
                word[1] += 1
                doesExist = False
        if doesExist:
            result.append([item, 1])

    with open("logs_lists.txt", "w") as file:
        file.write("WORD FREQUENCY DATA (Type: LIST OF LISTS)\n\n\n\n\n\n\n\n\n\n" + json.dumps(result) + "\n\n\n\n\n\n\n\n\n\n")
        print("\n\nWord frequency data (type: List of Lists) has been logged successfully.\n")

    continue_program()


def histogram_as_list_of_tuples(data):
    result = []

    with open("logs_tuples.txt", "w") as file:
        file.write("WORD FREQUENCY DATA (Type: LIST OF TUPLES)\n\n\n\n\n\n\n\n\n\n" + json.dumps(result) + "\n\n\n\n\n\n\n\n\n\n")
        print("\n\nWord frequency data (type: List of Tuples) has been logged successfully.")

    continue_program()


# Function to continue program so user can repeat or vary simulations 
def continue_program():
    loop_choice = input("\nWould you like to run this program again? (y/n)\n>> ")

    if loop_choice:
        loop_choice.lower()

        if loop_choice[0] == "y":
            print("\nProgram has restarted successfully.\n")
            program_start()
        elif loop_choice[0] == "n":
            print("\nProgram has been exited successfully.\n")
            return
        else:
            print("\nUser input is invalid. Please enter a valid response.\n")
            continue_program()
    else:
        print("\nUser input is invalid. Please enter a valid response.\n")
        continue_program()


if __name__ == "__main__":
    program_start()